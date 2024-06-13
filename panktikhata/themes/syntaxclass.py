from dataclasses import dataclass


@dataclass
class SyntaxStyle:
    """
    A class representing syntax style

    Attributes:
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


def get_stylesheet(s: SyntaxStyle, fontsize : int) -> str:
    return "QPlainTextEdit { font-size: %d; color: %s; background-color: %s }" % (fontsize, s.fg, s.bg)
