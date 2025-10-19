#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generador de resúmenes por lotes (sin input) — Versión separada por asignaturas.

Cambios clave vs. versión original:
- Acepta SOLO la playlist indicada por el usuario.
- En lugar de un único .md por playlist, genera VARIOS .md: uno por subjectKey
  del TIMETABLE (p.ej. 'DAM1 - Programación.md'), agrupando los vídeos que
  caen en sus franjas según la fecha/hora del título.
- Los vídeos sin fecha o que no encajan en ninguna franja se guardan en 'Otros.md'.

Requisitos:
  pip install -U yt-dlp requests
  ollama serve
  (opcional) cookies.txt junto al script

Ejecución:
  python genera.py
"""

import json
import re
import sys
import time
import subprocess
from pathlib import Path
from datetime import datetime, time as dtime
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse, parse_qs

# =======================
# LISTA HARDCODEADA (SOLO ESTA)
# =======================
PLAYLIST_URLS = [
    "https://www.youtube.com/watch?v=7u86RY0F2pg&list=PLWKjZdWQCDC5cNBAOFGVR9_u64pZ5MbB0&index=1"
]

# =======================
# CONFIG
# =======================
USER_AGENT           = "Mozilla/5.0"
COOKIES_FILE         = Path("cookies.txt")  # opcional
PLAYER_CLIENTS       = ["mweb", "tv", "web", "android"]
SLEEP_BETWEEN_VIDEOS = 0.8
SLEEP_BETWEEN_OLLAMA = 0.4
SLEEP_BETWEEN_PLAYLISTS = 0.8

OUT_ROOT             = Path("salida")
SUBS_DIR             = OUT_ROOT / "subs"
TEXT_DIR             = OUT_ROOT / "textos"

OLLAMA_MODEL         = "llama3.1:8b-instruct-q4_0"
OLLAMA_URL_CHAT      = "http://localhost:11434/api/chat"
OLLAMA_TIMEOUT       = 9000  # s

SAFE_CHARS = r"[^A-Za-z0-9áéíóúÁÉÍÓÚñÑüÜ()_. -]"
FALLBACK_TO_ANY_AUTO = True
FALLBACK_AUTO_PRIORITY = ["es-ES", "es-419", "es", "pt", "en"]

# =======================
# TIMETABLE (se agrupa por subjectKey)
# =======================
TIMETABLE: Dict[str, List[Dict[str, str]]] = {
  'lunes': [
    {'label':'DAM1 - Lenguajes de marcas - lunes 13:00-14:00',            'start':'13:00', 'end':'14:00', 'subjectKey':'DAM1 - Lenguajes de marcas'},
    {'label':'DAM1 - Sistemas informáticos - lunes 14:00 - 15:00',         'start':'14:00', 'end':'15:00', 'subjectKey':'DAM1 - Sistemas informáticos'},
    {'label':'DAM1 - Entornos de desarrollo - lunes 15:00 - 16:00',        'start':'15:00', 'end':'16:00', 'subjectKey':'DAM1 - Entornos de desarrollo'},
    {'label':'DAM1 - Proyecto interdisciplinar - lunes 16:00 - 17:00',     'start':'16:00', 'end':'17:00', 'subjectKey':'DAM1 - Proyecto interdisciplinar'},
    {'label':'DAM1 - Sistemas informáticos - lunes 17:00 - 18:00',         'start':'17:00', 'end':'18:00', 'subjectKey':'DAM1 - Sistemas informáticos'},
    {'label':'DAM2 - Programación multimedia - lunes 18:00 - 19:30',       'start':'18:00', 'end':'19:30', 'subjectKey':'DAM2 - Programación multimedia'},
    {'label':'DAM2 - Desarrollo de interfaces - lunes 19:30 - 21:30',      'start':'19:30', 'end':'21:30', 'subjectKey':'DAM2 - Desarrollo de interfaces'},
  ],
  'jueves': [
    {'label':'DAM1 - Lenguajes de marcas - jueves  14:00 - 15:00',         'start':'14:00', 'end':'15:00', 'subjectKey':'DAM1 - Lenguajes de marcas'},
    {'label':'DAM1 - Programación - jueves  15:00 - 17:00',                'start':'15:00', 'end':'17:00', 'subjectKey':'DAM1 - Programación'},
    {'label':'DAM1 - Bases de datos - jueves  17:00 - 19:00',              'start':'17:00', 'end':'19:00', 'subjectKey':'DAM1 - Bases de datos'},
    {'label':'DAM2 - Procesos y servicios - jueves  19:00 - 20:30',        'start':'19:00', 'end':'20:30', 'subjectKey':'DAM2 - Procesos y servicios'},
    {'label':'DAM2 - Acceso a datos - jueves  20:30 - 21:30',              'start':'20:30', 'end':'21:30', 'subjectKey':'DAM2 - Acceso a datos'},
  ],
  'viernes': [
    {'label':'DAM2 - Proyecto intermodular - viernes   13:30 - 14:30',     'start':'13:30', 'end':'14:30', 'subjectKey':'DAM2 - Proyecto intermodular'},
    {'label':'DAM2 - Sistemas de gestión empresarial - viernes 15:00-17:00','start':'15:00', 'end':'17:00', 'subjectKey':'DAM2 - Sistemas de gestión empresarial'},
  ],
}

# ===== Utilidades =====
def safe_filename(name: str) -> str:
    name = name.strip().replace("/", "-").replace("\\", "-")
    name = re.sub(SAFE_CHARS, "", name)
    name = re.sub(r"\s+", " ", name)
    return name[:200] if len(name) > 200 else name

WS_RE   = re.compile(r"\s+")
_TS_RE  = re.compile(r"-->\s")
_NUM_RE = re.compile(r"^\d+$")
_TAG_RE = re.compile(r"<[^>]+>")
IGNORE_PREFIXES = (
    "WEBVTT", "NOTE", "X-TIMESTAMP-MAP", "Kind:", "Language:",
    "STYLE", "REGION", "##", "align:", "position:", "line:", "size:"
)
NOISE_TOKENS = ("♪", "♫")

def normalize_line(s: str) -> str:
    s = _TAG_RE.sub("", s)
    for tok in NOISE_TOKENS:
        s = s.replace(tok, "")
    s = s.strip()
    s = WS_RE.sub(" ", s)
    return s

def vtt_to_solid_text(vtt_path: Path) -> str:
    if not vtt_path.exists():
        return ""
    lines_clean: List[str] = []
    last_seen: List[str] = []
    with vtt_path.open("r", encoding="utf-8", errors="ignore") as f:
        for raw in f:
            s = raw.strip()
            if not s:
                continue
            if s.startswith(IGNORE_PREFIXES):
                continue
            if _NUM_RE.fullmatch(s):
                continue
            if _TS_RE.search(s):
                continue
            s = normalize_line(s)
            if not s:
                continue
            if s in last_seen[-3:]:
                continue
            lines_clean.append(s)
            last_seen.append(s)
    if not lines_clean:
        return ""
    text = " ".join(lines_clean)
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    text = re.sub(WS_RE, " ", text).strip()
    return text

def ensure_dirs():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    SUBS_DIR.mkdir(parents=True, exist_ok=True)
    TEXT_DIR.mkdir(parents=True, exist_ok=True)

def yt_cmd_base() -> List[str]:
    cmd = ["yt-dlp", "--user-agent", USER_AGENT]
    if COOKIES_FILE.exists():
        cmd += ["--cookies", str(COOKIES_FILE)]
    return cmd

# ===== Playlist (con fix a --flat-playlist) =====
def fetch_playlist_items(playlist_code: str) -> Tuple[str, List[Dict[str, str]]]:
    """Devuelve (playlist_title, items=[{id,title,url}])"""
    url = f"https://www.youtube.com/playlist?list={playlist_code}"

    def run_cmd(extra_flags: List[str]) -> dict:
        cmd = yt_cmd_base() + extra_flags + ["-J", url]
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if p.returncode != 0:
            msg = (p.stderr.decode("utf-8", "ignore") or p.stdout.decode("utf-8", "ignore")).strip()
            raise RuntimeError(msg)
        return json.loads(p.stdout.decode("utf-8", "ignore"))

    try:
        info = run_cmd(["--flat-playlist", "--skip-download", "--quiet"])
    except RuntimeError:
        info = run_cmd(["--skip-download", "--quiet"])

    title = info.get("title") or f"Playlist {playlist_code}"
    entries = info.get("entries") or []

    items = []
    for e in entries:
        vid = e.get("id")
        vtitle = e.get("title") or e.get("fulltitle") or ""
        if not vid or not vtitle or "[Deleted video]" in vtitle:
            continue
        vurl = f"https://www.youtube.com/watch?v={vid}"
        items.append({"id": vid, "title": vtitle, "url": vurl})
    return title, items

# ===== Subtítulos =====
def _lang_from_filename(path: Path, base_stem: str) -> str:
    name = path.name
    if name.startswith(base_stem + "."):
        rest = name[len(base_stem) + 1 :]
    else:
        rest = name
    if rest.lower().endswith(".vtt"):
        rest = rest[:-4]
    return rest

def pick_best_spanish_vtt(base_out: Path) -> Optional[Tuple[Path, str]]:
    pattern = base_out.name + ".es*.vtt"
    candidates = sorted(base_out.parent.glob(pattern))
    if not candidates:
        return None
    LANG_PRIORITY = ["es-ES", "es-419", "es"]
    def score(p: Path) -> Tuple[int, str]:
        lang = _lang_from_filename(p, base_out.name)
        for idx, tag in enumerate(LANG_PRIORITY):
            if lang == tag:
                return (idx, lang)
        if lang.startswith("es.") or lang.startswith("es-"):
            return (len(LANG_PRIORITY), lang)
        if lang == "es":
            return (2, lang)
        return (999, lang)
    ranked = sorted(((score(p), p) for p in candidates), key=lambda x: x[0])
    best = ranked[0][1]
    best_lang = _lang_from_filename(best, base_out.name)
    return best, best_lang

def download_best_subs(url: str, base_out: Path) -> Optional[Tuple[Path, str, str]]:
    """Intentos: español -> fallback auto -> all-subs. Devuelve (ruta_vtt, lang, client)"""
    def run_with_langs(langs, client):
        cmd = yt_cmd_base() + [
            "--skip-download",
            "--write-subs", "--write-auto-subs",
            "--sub-format", "vtt/srv3",
            "--convert-subs", "vtt",
            "--sub-langs", ",".join(langs),
            "--output", str(base_out) + ".%(ext)s",
            "--extractor-args", f"youtube:player_client={client}",
            url,
        ]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            pick = pick_best_spanish_vtt(base_out)
            if pick:
                p, lang = pick
                return p, lang, client
            for lang in langs:
                maybe = base_out.with_name(base_out.name + f".{lang}.vtt")
                if maybe.exists():
                    return maybe, lang, client
        except subprocess.CalledProcessError:
            pass
        return None

    def probe_info(client: str) -> dict:
        cmd = yt_cmd_base() + ["-J", "--extractor-args", f"youtube:player_client={client}", url]
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if p.returncode != 0:
            return {}
        try:
            return json.loads(p.stdout.decode("utf-8", "ignore"))
        except Exception:
            return {}

    def pick_spanish_keys(info: dict) -> List[str]:
        keys = set()
        for field in ("subtitles", "automatic_captions"):
            d = info.get(field) or {}
            for lang in d.keys():
                if lang == "es" or lang.startswith("es-") or lang.startswith("es.") or lang == "spa":
                    keys.add(lang)
        ordered = ["es-ES", "es-419", "es", *sorted([k for k in keys if k not in {"es-ES","es-419","es"}])]
        return [k for k in ordered if k in keys]

    def pick_fallback_auto(info: dict) -> Optional[str]:
        auto = info.get("automatic_captions") or {}
        if not auto:
            return None
        for pref in FALLBACK_AUTO_PRIORITY:
            for lang in auto.keys():
                if lang == pref or lang.startswith(pref + ".") or (pref == "es" and (lang.startswith("es-") or lang.startswith("es."))):
                    return lang
        for lang in auto.keys():
            return lang
        return None

    def all_subs(client: str):
        cmd = yt_cmd_base() + [
            "--skip-download",
            "--all-subs",
            "--sub-format", "vtt/srv3",
            "--convert-subs", "vtt",
            "--output", str(base_out) + ".%(ext)s",
            "--extractor-args", f"youtube:player_client={client}",
            url,
        ]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            pick = pick_best_spanish_vtt(base_out)
            if pick:
                p, l = pick
                return p, l, client
            vtts = sorted(base_out.parent.glob(base_out.name + ".*.vtt"))
            if vtts:
                for pref in FALLBACK_AUTO_PRIORITY:
                    for pth in vtts:
                        lang = _lang_from_filename(pth, base_out.name)
                        if lang == pref or lang.startswith(pref + "."):
                            return pth, lang, client
                return vtts[0], _lang_from_filename(vtts[0], base_out.name), client
        except subprocess.CalledProcessError:
            return None

    for client in PLAYER_CLIENTS:
        info = probe_info(client)
        es_langs = pick_spanish_keys(info)
        if es_langs:
            got = run_with_langs(es_langs, client)
            if got:
                return got
        if FALLBACK_TO_ANY_AUTO:
            fb = pick_fallback_auto(info)
            if fb:
                got = run_with_langs([fb], client)
                if got:
                    return got
        got = all_subs(client)
        if got:
            return got

    for client in PLAYER_CLIENTS:
        got = all_subs(client)
        if got:
            return got
    return None

# ===== Ollama =====
def ensure_ollama_alive():
    try:
        p = subprocess.run(
            ["curl", "-sS", "http://localhost:11434/api/tags"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5
        )
        if p.returncode != 0:
            raise RuntimeError
    except Exception:
        raise RuntimeError("No puedo conectar con Ollama en http://localhost:11434. ¿Está ejecutándose 'ollama serve'?")

def ollama_summarize_long(title: str, raw_text: str) -> str:
    """Resumen EXTENSO en español (450–700 palabras) con bullets y código cuando aplique."""
    import requests as _rq
    system = (
        "Eres un profesor experto de programación para alumnado de FP. "
        "Elabora resúmenes extensos, claros, en ESPAÑOL neutro, con rigor y ejemplos concisos."
    )
    user = (
        f"Título de la clase: {title}\n\n"
        "TRANSCRIPCIÓN LIMPIA:\n"
        f"{raw_text}\n\n"
        "TAREA:\n"
        "- Escribe un resumen EXTENSO (aprox. 450–700 palabras).\n"
        "- Incluye: objetivos, conceptos clave, explicación didáctica, pasos/comandos si aparecen, y buenas prácticas.\n"
        "- Usa bullets cuando mejore la claridad.\n"
        "- Si hay fragmentos de código, usa bloques con triple backtick y el lenguaje correcto (```python```, ```bash```, ```js```, etc.).\n"
        "- No inventes APIs ni resultados; si algo es incompleto, indícalo brevemente.\n"
    )
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user}
        ],
        "stream": False,
        "options": {
            "temperature": 0.35,
            "num_ctx": 12288
        }
    }
    r = _rq.post(OLLAMA_URL_CHAT, json=payload, timeout=OLLAMA_TIMEOUT)
    r.raise_for_status()
    data = r.json()
    return (data.get("message") or {}).get("content") or ""

# ===== Fechas en título =====
DATE_PREFIX_RE = re.compile(
    r"^(?P<y>\d{4})[\s_](?P<m>\d{2})[\s_](?P<d>\d{2})[\s_](?P<H>\d{2})[\s_](?P<M>\d{2})[\s_](?P<S>\d{2})\s*-?\s*(?P<rest>.*)$"
)

def parse_datetime_from_title(title: str) -> Optional[datetime]:
    m = DATE_PREFIX_RE.match(title)
    if not m:
        return None
    try:
        return datetime(int(m["y"]), int(m["m"]), int(m["d"]), int(m["H"]), int(m["M"]), int(m["S"]))
    except ValueError:
        return None

# ===== Helpers para timetable =====
WEEKDAY_ES = {0: 'lunes', 1: 'martes', 2: 'miércoles', 3: 'jueves', 4: 'viernes', 5: 'sábado', 6: 'domingo'}

def parse_hhmm(s: str) -> dtime:
    h, m = s.strip().split(":")
    return dtime(int(h), int(m))

def match_subject(dt: Optional[datetime]) -> Optional[str]:
    """Devuelve subjectKey según TIMETABLE o None si no encaja."""
    if dt is None:
        return None
    day_es = WEEKDAY_ES[dt.weekday()]
    slots = TIMETABLE.get(day_es, [])
    t = dtime(dt.hour, dt.minute, dt.second)
    for slot in slots:
        start = parse_hhmm(slot['start'])
        end   = parse_hhmm(slot['end'])
        if start <= t < end:
            return slot['subjectKey']
    return None

# ===== Informe Markdown (por subjectKey) =====
def build_md_report_subject(subject_key: str, rows: List[Dict]) -> str:
    parts = [
        f"# Informe de clases – {subject_key}\n",
        f"_Generado automáticamente. Vídeos incluidos: {len(rows)}._\n",
        "## Índice\n"
    ]
    for i, r in enumerate(rows, start=1):
        t = r.get("title", "")
        anchor = re.sub(r'[^a-z0-9\- ]', '', t.lower()).replace(" ", "-")
        parts.append(f"{i}. [{t}](#{anchor})")
    parts.append("\n---\n")

    for r in rows:
        d = r.get("date_str") or ""
        t = r.get("title") or ""
        u = r.get("url") or ""
        s = (r.get("summary") or "").strip()
        parts.append(f"## {t}\n")
        if d:
            parts.append(f"**Fecha/Hora:** {d}\n")
            parts.append(f"**Día (ES):** {WEEKDAY_ES[r['date'].weekday()] if r.get('date') else ''}\n")
        if u:
            parts.append(f"**Enlace:** {u}\n")
        if not s:
            s = "_Sin resumen disponible._"
        parts.append(s + "\n")
        parts.append("---\n")
    return "\n".join(parts).strip() + "\n"

# =======================
# Helpers de lote
# =======================
PLAYLIST_CODE_RE = re.compile(r"^[A-Za-z0-9_-]{18,}")  # p.ej. PL... de YouTube

def extract_playlist_code(url_or_code: str) -> Optional[str]:
    s = url_or_code.strip()
    if PLAYLIST_CODE_RE.fullmatch(s):
        return s
    try:
        pr = urlparse(s)
        qs = parse_qs(pr.query)
        code = (qs.get("list") or [None])[0]
        if code:
            return code
    except Exception:
        pass
    return None

# =======================
# PROCESO DE UNA PLAYLIST
# =======================
def process_one_playlist(playlist_code: str) -> Dict[str, Path]:
    """
    Procesa la playlist y devuelve {subjectKey: ruta_md} con los .md generados.
    """
    ensure_dirs()
    print("→ Obteniendo vídeos de la playlist…")
    try:
        playlist_title, videos = fetch_playlist_items(playlist_code)
    except Exception as e:
        print(f"Error extrayendo playlist: {e}")
        return {}

    if not videos:
        print("La playlist no contiene vídeos válidos.")
        return {}

    # Agrupación por subjectKey
    grouped: Dict[str, List[Dict]] = {}
    OTHER_BUCKET = "Otros"

    for idx, v in enumerate(videos, start=1):
        title = v["title"]
        url   = v["url"]
        vid   = v["id"]
        print(f"[{idx:03d}/{len(videos)}] {title}")

        base_name = safe_filename(title)
        base_out  = SUBS_DIR / base_name
        text_path = TEXT_DIR / f"{base_name}.txt"
        sum_path  = TEXT_DIR / f"{base_name}.md"  # caché de resumen extenso

        # Fecha del título
        dt = parse_datetime_from_title(title)
        subject_key = match_subject(dt)

        # 1) Si hay resumen en caché → reusar
        if sum_path.exists():
            summary_md = sum_path.read_text(encoding="utf-8")
        else:
            # 2) Subtítulos
            pick = download_best_subs(url, base_out)
            if not pick:
                summary_md = "_No hay subtítulos disponibles._"
            else:
                vtt_path, lang_code, client_used = pick
                # 3) VTT → texto
                txt = vtt_to_solid_text(vtt_path)
                if not txt:
                    summary_md = "_No se pudo convertir el VTT a texto._"
                else:
                    text_path.write_text(txt, encoding="utf-8")
                    # 4) Resumen EXTENSO con Ollama
                    try:
                        ensure_ollama_alive()
                        summary_md = ollama_summarize_long(title, txt)
                        if not summary_md.strip():
                            summary_md = "_El modelo no devolvió contenido._"
                        sum_path.write_text(summary_md, encoding="utf-8")  # cache
                    except Exception as e:
                        print(f"   × Error con Ollama: {e}")
                        summary_md = "_Error generando el resumen con Ollama._"

        row = {
            "date": dt,
            "date_str": dt.strftime("%Y-%m-%d %H:%M:%S") if dt else "",
            "title": title,
            "url": url,
            "summary": summary_md
        }

        bucket = subject_key if subject_key else OTHER_BUCKET
        grouped.setdefault(bucket, []).append(row)

        time.sleep(SLEEP_BETWEEN_VIDEOS + SLEEP_BETWEEN_OLLAMA)

    # Ordenar dentro de cada bucket: cronológico primero y luego sin fecha
    for bucket, rows in grouped.items():
        with_date   = [r for r in rows if r["date"] is not None]
        withoutdate = [r for r in rows if r["date"] is None]
        with_date.sort(key=lambda r: r["date"])
        grouped[bucket] = with_date + withoutdate

    # Escribir un .md por subjectKey
    generated_paths: Dict[str, Path] = {}
    for subject_key, rows in grouped.items():
        subject_slug = safe_filename(subject_key)
        report_md_path = OUT_ROOT / f"{subject_slug}.md"
        md_str = build_md_report_subject(subject_key, rows)
        report_md_path.write_text(md_str, encoding="utf-8")
        generated_paths[subject_key] = report_md_path
        print(f"· Generado: {report_md_path.resolve()}")

    print("\n=== LISTO ===")
    print(f"Documentos generados: {len(generated_paths)}")
    return generated_paths

# =======================
# MAIN (automático, sin input)
# =======================
def main():
    print("\n=== Procesamiento AUTOMÁTICO de playlist única (hardcoded) ===\n")

    # Normaliza a un único código válido
    codes: List[str] = []
    for url in PLAYLIST_URLS:
        code = extract_playlist_code(url)
        if not code:
            print(f"· Aviso: no pude extraer código de: {url}")
            continue
        if code not in codes:
            codes.append(code)

    if not codes:
        print("No hay código de playlist válido para procesar.")
        sys.exit(1)

    generated_all: Dict[str, Path] = {}
    for i, code in enumerate(codes, start=1):
        print("\n" + "="*60)
        print(f"[{i:02d}/{len(codes)}] Procesando playlist: {code}")
        print("="*60)
        out = process_one_playlist(code)
        generated_all.update(out)
        time.sleep(SLEEP_BETWEEN_PLAYLISTS)

    print("\n===== RESUMEN =====")
    if not generated_all:
        print("No se generó ningún Markdown.")
    else:
        for subj, p in generated_all.items():
            print(f"· {subj}: {p}")

if __name__ == "__main__":
    main()

