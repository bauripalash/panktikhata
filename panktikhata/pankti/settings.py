from enum import Enum

from themes.syntaxclass import SyntaxStyle
from themes.syntaxstyle import *


class AppTheme(Enum):
    LIGHT = 1
    DARK = 2
    AUTO = 3


def app_theme_to_str(a : AppTheme) -> str:
    if a.value == 1:
        return "light"
    elif a.value == 2:
        return "dark"
    else:
        return "auto"



class AppLanguage(Enum):
    ENGLISH = 1
    BENGALI = 2


class PanktiSettings:
    app_theme: AppTheme
    editor_theme: SyntaxStyle
    language: AppLanguage
    pankti_path: str
    font_size: int
    autosave: bool

    def __init__(self) -> None:
        self.app_theme = AppTheme.AUTO
        self.editor_theme = atom_one_dark.atom_one_dark_theme
        self.language = AppLanguage.ENGLISH
        self.pankti_path = "pankti"
        self.font_size = 20
        self.autosave = True

    def __repr__(self) -> str:
        return f"S<|{self.app_theme}|{self.font_size}|{self.language}|{self.pankti_path}|{self.autosave}|>"
