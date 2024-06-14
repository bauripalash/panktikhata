from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass(init=True)
class SyntaxStyle:
    """
    A class representing syntax style

    Attributes:
        name (str): Name of Theme
        bg (str): Background Color
        fg (str): Foreground Color
        keyword (str): Keyword Color
        literal (str): literal items color
        string (str): String Color
        number (str): Number Color
        builtin (str): Builtin function Color
        comment (str): Comments Color
    """

    bg: str
    fg: str
    keyword: str
    literal: str
    string: str
    number: str
    builtin: str
    comment: str
    tname: str


def get_syntaxstyle_as_dict(s: SyntaxStyle) -> Dict[str, Any]:
    return asdict(s)


def get_syntaxstyle_from_dict(s: Dict[str, str]) -> SyntaxStyle:
    st = SyntaxStyle(
        bg=s["bg"],
        fg=s["fg"],
        keyword=s["keyword"],
        literal=s["literal"],
        string=s["string"],
        number=s["number"],
        builtin=s["builtin"],
        comment=s["comment"],
        tname=s["tname"],
    )

    return st


def get_stylesheet(s: SyntaxStyle, fontsize: int) -> str:
    return (
        "QPlainTextEdit { font-size: %d; color: %s; background-color: %s }"
        % (fontsize, s.fg, s.bg)
    )
