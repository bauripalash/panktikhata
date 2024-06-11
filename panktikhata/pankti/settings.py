from enum import Enum

class AppTheme(Enum):
    LIGHT = 1
    DARK = 2
    AUTO = 3

class EditorTheme(Enum):
    ATOM_LIGHT = 1
    ATOM_DARK = 2

class AppLanguage(Enum):
    ENGLISH = 1
    BENGALI = 2

class PanktiSettings:
    app_theme : AppTheme
    editor_theme : EditorTheme
    language: AppLanguage
    pankti_path : str
    autosave : bool

    def __init__(self) -> None:
        self.app_theme = AppTheme.AUTO
        self.editor_theme = EditorTheme.ATOM_LIGHT
        self.language = AppLanguage.ENGLISH
        self.pankti_path = "pankti"
        self.autosave = True

    def __repr__(self) -> str:
        return f'S<|{self.app_theme}|{self.editor_theme}|{self.language}|{self.pankti_path}|{self.autosave}|>'

