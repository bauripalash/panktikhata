from enum import Enum
import pickle
import os

from themes.syntaxclass import SyntaxStyle
from themes.syntaxstyle import atom_one_dark


class AppTheme(Enum):
    LIGHT = 1
    DARK = 2
    AUTO = 3


def app_theme_to_str(a: AppTheme) -> str:
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
        self.app_theme = AppTheme.DARK
        self.editor_theme = atom_one_dark.atom_one_dark_theme
        self.language = AppLanguage.ENGLISH
        self.pankti_path = "pankti"
        self.font_size = 20
        self.autosave = True

    def to_pickle(self) -> bytes:
        return pickle.dumps(self)

    def dump_settings(self, filepath: str) -> bool:
        if not os.path.isdir(os.path.dirname(filepath)):
            return False

        with open(filepath, "wb") as f:
            f.write(self.to_pickle())

        return True

    def __repr__(self) -> str:
        return "S<|{0}|{1}|{2}|{3}|{4}|>".format(
            self.app_theme,
            self.font_size,
            self.language,
            self.pankti_path,
            self.autosave,
        )


def get_settings_from_conf(filepath: str) -> tuple[PanktiSettings, bool]:
    if os.path.exists(filepath):
        f = open(filepath, "rb")
        return pickle.load(f), True
    return PanktiSettings(), False
