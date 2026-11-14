"""The wiki's languages, in the order of the language selector.

code: folder of content/ and docs/; html: the lang attribute; game: folder in base/strings;
name: the language's own name; dec: decimal separator; cjk: text measured as double width.
A language is built only when content/<code>/ exists, so languages can be added one by one.
"""
import json
import os

ALL = [
    {"code": "en", "html": "en", "game": "en", "name": "English", "dec": "."},
    {"code": "fr", "html": "fr", "game": "fr", "name": "Français", "dec": ","},
    {"code": "de", "html": "de", "game": "de", "name": "Deutsch", "dec": ","},
    {"code": "es", "html": "es", "game": "es", "name": "Español", "dec": ","},
    {"code": "it", "html": "it", "game": "it", "name": "Italiano", "dec": ","},
    {"code": "nl", "html": "nl", "game": "nl", "name": "Nederlands", "dec": ","},
    {"code": "pl", "html": "pl", "game": "pl", "name": "Polski", "dec": ","},
    {"code": "pt-br", "html": "pt-BR", "game": "pt_BR", "name": "Português (Brasil)", "dec": ","},
    {"code": "ru", "html": "ru", "game": "ru", "name": "Русский", "dec": ","},
    {"code": "ja", "html": "ja", "game": "ja", "name": "日本語", "dec": ".", "cjk": True},
    {"code": "ko", "html": "ko", "game": "ko", "name": "한국어", "dec": ".", "cjk": True},
    {"code": "zh-cn", "html": "zh-Hans", "game": "zh_CN", "name": "简体中文", "dec": ".", "cjk": True},
    {"code": "zh-tw", "html": "zh-Hant", "game": "zh_TW", "name": "繁體中文", "dec": ".", "cjk": True},
]
BY_CODE = {l["code"]: l for l in ALL}
HERE = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(HERE, "content")
I18N = os.path.join(HERE, "i18n")  # i18n/<code>.json: texts of the translated languages (en, fr, de are in the code)


SOURCE = ("en", "fr", "de")  # texts in the code; the others come from i18n/<code>.json


def present():
    """Languages with a content folder and their texts (code or i18n file), in selector order.
    WIKI_LANGS=en,ru limits a build or check to some languages (used while translating)."""
    only = [c for c in os.environ.get("WIKI_LANGS", "").split(",") if c]
    return [l["code"] for l in ALL
            if os.path.isdir(os.path.join(CONTENT, l["code"]))
            and (l["code"] in SOURCE or os.path.exists(os.path.join(I18N, l["code"] + ".json")))
            and (not only or l["code"] in only or l["code"] == "en")]


def num(value, lang, digits=None):
    """A number written the way the language writes it (decimal separator only)."""
    s = f"{value:.{digits}f}" if digits is not None else str(value)
    return s.replace(".", BY_CODE[lang]["dec"])


def is_cjk(lang):
    return BY_CODE[lang].get("cjk", False)


def texts(code):
    """i18n/<code>.json -> {"ui": {...}, "diagrams": {"T_X": {...}}, "cargo": {...}, "domains": {id: {...}}}, or {}."""
    p = os.path.join(I18N, code + ".json")
    if not os.path.exists(p):
        return {}
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def translated():
    """Codes that have an i18n file."""
    return [l["code"] for l in ALL if os.path.exists(os.path.join(I18N, l["code"] + ".json"))]
