"""The game's own translations (base/strings/<lang>/LC_MESSAGES/base.mo), read-only.

    python gamestrings.py "Specialized Warehouse: {boost}" [more msgids...]   # print en / fr / de
    python gamestrings.py --find "Warehouse"                                 # search msgids
Used to quote the in-game labels exactly in each language of the wiki.
"""
import gettext
import os
import sys

from sources import GAME

STRINGS = os.path.join(GAME, "base", "strings")
LANGS = ["en", "fr", "de"]
_cat = {}


def catalog(lang):
    if lang not in _cat:
        with open(os.path.join(STRINGS, lang, "LC_MESSAGES", "base.mo"), "rb") as f:
            _cat[lang] = gettext.GNUTranslations(f)
    return _cat[lang]


def tr(msgid, lang):
    return catalog(lang).gettext(msgid)


def main():
    args = sys.argv[1:]
    if args and args[0] == "--find":
        needle = args[1].lower()
        for k in sorted(catalog("fr")._catalog):
            if isinstance(k, str) and needle in k.lower():
                print(f"{k!r:60} fr={tr(k, 'fr')!r}  de={tr(k, 'de')!r}")
        return
    for msgid in args:
        print(msgid)
        for lang in LANGS:
            print(f"   {lang}: {tr(msgid, lang)}")


if __name__ == "__main__":
    main()
