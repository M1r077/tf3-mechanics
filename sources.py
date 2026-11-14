"""Read-only access to every Lua / Teal file of the game (zipped or loose), without extracting anything.

A source file is named by an id: "<zip>!<path inside the zip>" for zipped files (zip path relative to
base/content, with forward slashes) or "<path>" for loose files under base/content.
Examples: "game_mechanics.zip!game_mechanics/towns/town_growth.script.tl", "industries/industryutil.lua".
"""
import os
import zipfile
from functools import lru_cache

GAME = os.environ.get("TF3_GAME", r"A:\SteamLibrary\steamapps\common\Transport Fever 3")
CONTENT = os.path.join(GAME, "base", "content")
EXTS = (".lua", ".tl")


def _rel(path):
    return os.path.relpath(path, CONTENT).replace("\\", "/")


@lru_cache(maxsize=None)
def _zip(rel_zip):
    return zipfile.ZipFile(os.path.join(CONTENT, rel_zip))


def iter_sources():
    """Yield (source_id, size) for every .lua / .tl file under base/content, zips included."""
    for root, _dirs, files in os.walk(CONTENT):
        for name in sorted(files):
            full = os.path.join(root, name)
            rel = _rel(full)
            if name.endswith(EXTS):
                yield rel, os.path.getsize(full)
            elif name.endswith(".zip"):
                try:
                    z = _zip(rel)
                except zipfile.BadZipFile:
                    continue
                for info in z.infolist():
                    if info.filename.endswith(EXTS):
                        yield f"{rel}!{info.filename}", info.file_size


def read(source_id):
    """Text of one source file (UTF-8, undecodable bytes replaced)."""
    if "!" in source_id:
        rel_zip, inner = source_id.split("!", 1)
        data = _zip(rel_zip).read(inner)
    else:
        with open(os.path.join(CONTENT, source_id), "rb") as f:
            data = f.read()
    return data.decode("utf-8", "replace")


def short(source_id):
    """Path shown to readers: the path inside the zip (the zip name is in the index)."""
    return source_id.split("!", 1)[-1]
