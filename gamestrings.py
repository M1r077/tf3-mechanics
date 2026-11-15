"""The game's own translations (base/strings/<lang>/LC_MESSAGES/base.mo), read-only.

    python gamestrings.py "Specialized Warehouse: {boost}" [more msgids...]   # print every wiki language
    python gamestrings.py --lang ru,zh-cn "Cargo Income" ...                 # only some languages
    python gamestrings.py --find "Warehouse" [--lang ...]                    # search msgids
    python gamestrings.py "vehicle-condition|Very Good"                      # string with a pGetText context
Used to quote the in-game labels exactly in each language of the wiki.
"""
import gettext
import os
import sys

import langs as L
from sources import GAME

STRINGS = os.path.join(GAME, "base", "strings")
LANGS = [l["code"] for l in L.ALL]
_cat = {}


def catalog(lang):
    if lang not in _cat:
        with open(os.path.join(STRINGS, L.BY_CODE[lang]["game"], "LC_MESSAGES", "base.mo"), "rb") as f:
            _cat[lang] = gettext.GNUTranslations(f)
    return _cat[lang]


def tr(msgid, lang):
    # "context|msgid" looks up a pGetText string (key "context\x04msgid" in the .mo)
    if "|" in msgid:
        ctx, mid = msgid.split("|", 1)
        return catalog(lang)._catalog.get(f"{ctx}\x04{mid}", mid)
    return catalog(lang).gettext(msgid)


def main():
    args = sys.argv[1:]
    langs = LANGS
    if "--lang" in args:
        i = args.index("--lang")
        langs = args[i + 1].split(",")
        del args[i:i + 2]
    if args and args[0] == "--find":
        needle = args[1].lower()
        for k in sorted(catalog("fr")._catalog, key=str):
            if isinstance(k, str) and needle in k.lower():
                print(repr(k))
                for lang in langs:
                    if lang != "en":
                        print(f"   {lang}: {catalog(lang)._catalog.get(k)!r}")
        return
    for msgid in args:
        print(msgid)
        for lang in langs:
            print(f"   {lang}: {tr(msgid, lang)}")


if __name__ == "__main__":
    main()
