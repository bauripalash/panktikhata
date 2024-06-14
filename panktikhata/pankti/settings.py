from enum import Enum
import json
import pickle
import os
from pathlib import Path
import platform
from typing import Dict, Any

from themes.syntaxclass import (
    SyntaxStyle,
    get_syntaxstyle_as_dict,
    get_syntaxstyle_from_dict,
)
from themes.syntaxstyle import atom_one_dark

CONFIG_FILE = "panktikhata.conf.pickle"

HOME_DIR = str(Path.home().absolute())

LINUX_CONF_DIR = os.path.join(HOME_DIR, ".config", "panktikhata")
WINDOWS_CONF_DIR = os.path.join(HOME_DIR, "panktikhata")


def get_conf_dir() -> str:
    osname = platform.system().lower()
    if osname == "windows":
        return WINDOWS_CONF_DIR
    else:
        return LINUX_CONF_DIR


class AppTheme(int, Enum):
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


class AppLanguage(int, Enum):
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

    def as_dict(self) -> Dict[str, Any]:
        result = {}
        result["app_theme"] = self.app_theme
        result["editor_theme"] = get_syntaxstyle_as_dict(self.editor_theme)
        result["language"] = self.language
        result["font_size"] = self.font_size
        result["autosave"] = self.autosave
        result["pankti_path"] = self.pankti_path

        return result

    def to_pickle(self) -> bytes:
        return pickle.dumps(self)

    def dump_settings(self, filepath: str) -> bool:
        if not os.path.isdir(os.path.dirname(filepath)):
            return False

        with open(filepath, "wb") as f:
            f.write(self.to_pickle())

        return True

    def __repr__(self) -> str:
        return "S<|{0}|{1}|{2}|{3}|{4}|{5}|>".format(
            self.app_theme,
            self.editor_theme.tname,
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


def _make_dir(p: Path) -> bool:
    if p.exists():
        return False
    else:
        p.mkdir()
        return True


def config_save_path(makedirs: bool) -> tuple[str, bool]:
    cdir = get_conf_dir()
    if makedirs:
        _make_dir(Path(cdir))

    return os.path.join(cdir, CONFIG_FILE), True


class EncoderPanktiSettings(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        print("OJ->", o)
        if isinstance(o, SyntaxStyle):
            return get_syntaxstyle_as_dict(o)
        elif isinstance(o, PanktiSettings):
            ob: PanktiSettings = o
            return ob.as_dict()
        return super().default(o)


def decoder_pankti_settings(dct: Dict[Any, Any]) -> Any:
    s = PanktiSettings()
    if "app_theme" in dct:
        s.app_theme = AppTheme(int(dct["app_theme"]))
    if "language" in dct:
        s.language = AppLanguage(int(dct["language"]))
    if "font_size" in dct:
        s.font_size = int(dct["font_size"])
    if "pankti_path" in dct:
        s.pankti_path = dct["pankti_path"]
    if "autosave" in dct:
        a = dct["autosave"]
        if a == "true":
            s.autosave = True
        else:
            s.autosave = False
    if "editor_theme" in dct:
        print(">>>>>>>>>>", dct["editor_theme"])
        s.editor_theme = get_syntaxstyle_from_dict(dct["editor_theme"])

    return s
