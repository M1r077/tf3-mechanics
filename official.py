"""Official Transport Fever 3 wiki (wiki.transportfever3.com): page list and local cache.

Page ids are read from the wiki's own navigation (the sidebar of the Game Manual), never guessed.
Each page is fetched as plain XHTML (do=export_xhtml) and stored as text in cache/official/<id>.txt.
The cache is local only (not published): our pages link to the official page and summarise it in our words.

    python official.py            # refresh the page list and every cached page
    python official.py --list     # print the page list
"""
import html
import json
import os
import re
import sys
import time
import urllib.request

BASE = "https://wiki.transportfever3.com/doku.php"
HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache", "official")
PAGES = os.path.join(HERE, "data", "official_pages.json")
UA = {"User-Agent": "tf3-mechanics-wiki/1.0 (fan project; reads public pages)"}


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def page_url(page_id, export=False):
    return f"{BASE}?id={page_id}" + ("&do=export_xhtml" if export else "")


def list_pages():
    """(id, title) of every page in the Game Manual navigation."""
    doc = fetch(page_url("gamemanual"))
    nav = doc.split('class="plugin__navi', 1)[-1]
    out, seen = [], set()
    for pid, title in re.findall(r'href="/doku\.php\?id=([\w:]+)"[^>]*>([^<]+)</a>', nav):
        if pid.count(":") >= 2 and pid not in seen:
            seen.add(pid)
            out.append({"id": pid, "title": html.unescape(title).strip(), "url": page_url(pid)})
    return out


def to_text(xhtml):
    body = xhtml.split("<body", 1)[-1]
    body = re.sub(r"(?is)<(script|style)\b.*?</\1>", "", body)
    body = re.sub(r"(?i)<h([1-6])[^>]*>", lambda m: "\n\n" + "#" * int(m.group(1)) + " ", body)
    body = re.sub(r"(?i)<(br|/p|/li|/tr|/h[1-6]|/div)[^>]*>", "\n", body)
    body = re.sub(r"(?i)<li[^>]*>", "- ", body)
    body = re.sub(r"(?i)<t[dh][^>]*>", " | ", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = html.unescape(body)
    body = re.sub(r"[ \t]+", " ", body)
    body = re.sub(r"\n\s*\n\s*\n+", "\n\n", body)
    return body.strip() + "\n"


def cache_path(page_id):
    return os.path.join(CACHE, page_id.replace(":", "__") + ".txt")


def read_cached(page_id):
    p = cache_path(page_id)
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def main():
    pages = list_pages()
    os.makedirs(CACHE, exist_ok=True)
    os.makedirs(os.path.dirname(PAGES), exist_ok=True)
    if "--list" in sys.argv:
        for p in pages:
            print(f"{p['id']:55} {p['title']}")
        return 0
    for p in pages:
        text = to_text(fetch(page_url(p["id"], export=True)))
        if "Permission Denied" in text[:400]:
            print(f"  ! {p['id']}: permission denied (skipped)")
            continue
        with open(cache_path(p["id"]), "w", encoding="utf-8", newline="\n") as f:
            f.write(f"# source: {p['url']}\n# fetched: {time.strftime('%Y-%m-%d')}\n\n{text}")
        print(f"  {p['id']:55} {len(text):6} chars")
        time.sleep(0.5)  # be polite
    with open(PAGES, "w", encoding="utf-8", newline="\n") as f:
        json.dump(pages, f, indent=1, ensure_ascii=False)
    print(f"{len(pages)} pages -> {os.path.relpath(PAGES, HERE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
