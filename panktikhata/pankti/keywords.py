from typing import Set

KEYWORDS = {
    "let",
    "dhori",
    "ধরি",
    "and",
    "ebong",
    "এবং",
    "or",
    "ba",
    "বা",
    "end",
    "sesh",
    "শেষ",
    "if",
    "jodi",
    "যদি",
    "then",
    "tahole",
    "তাহলে",
    "while",
    "jotokhon",
    "যখন",
    "return",
    "ferao",
    "ফেরাও",
    "func",
    "kaj",
    "কাজ",
    "import",
    "anoyon",
    "আনয়ন",
    "do",
    "koro",
    "করো",
    "break",
    "bhango",
    "ভাঙো",
}  # type: Set[str]

LITERALS = {
    "true",
    "sotti",
    "সত্যি",
    "false",
    "mittha",
    "মিথ্যা",
    "nil",
    "নিল",
}  # type: Set[str]

BUILTINS = {
    "len",
    "ayoton",
    "আয়তন",
    "show",
    "dekhao",
    "দেখাও",
}  # type: Set[str]

_token_specs = [
    ("STRING", r"\".+\""),
    ("IDENT", r"[a-zA-Z\u0981-\u09e0][a-zA-Z0-9\u0981-\u09e0]+"),
    # ("SKIP", r'[ \t]+'),
    ("NUMBER", r"[0-9\u09e6-\u09ef]+"),
]  # type : List[Tuple[str]]


def get_patterns() -> str:
    return "|".join("(?P<%s>%s)" % pair for pair in _token_specs)
