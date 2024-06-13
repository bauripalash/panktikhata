from dataclasses import dataclass
import re
from PySide6 import QtGui  # type: ignore
from PySide6.QtGui import (
    QBrush,
    QColor,
    QSyntaxHighlighter,
    QTextCharFormat,
)  # type: ignore

from pankti import keywords
from themes.syntaxstyle import *
from themes.syntaxclass import *


@dataclass
class HighlightRule:
    keyword: QtGui.QTextCharFormat
    literal: QtGui.QTextCharFormat
    string: QtGui.QTextCharFormat
    number: QtGui.QTextCharFormat
    builtin: QtGui.QTextCharFormat
    bg: QtGui.QTextCharFormat | None = None
    fg: QtGui.QTextCharFormat | None = None


class PanktiSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent) -> None:
        super().__init__(parent)

    def set_theme(self, theme: SyntaxStyle) -> None:
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QBrush(QColor(theme.keyword)))

        literal_format = QTextCharFormat()
        literal_format.setForeground(QBrush(QColor(theme.literal)))

        string_format = QTextCharFormat()
        string_format.setForeground(QBrush(QColor(theme.string)))

        number_format = QTextCharFormat()

        number_format.setForeground(QBrush(QColor(theme.number)))

        builtin_format = QTextCharFormat()
        builtin_format.setForeground(QBrush(QColor(theme.builtin)))

        self.highlight_rule = HighlightRule(
            keyword=keyword_format,
            literal=literal_format,
            string=string_format,
            number=number_format,
            builtin=builtin_format,
        )

        self.tokregex = keywords.get_patterns()

    def highlightBlock(self, text: str) -> None:
        for mo in re.finditer(self.tokregex, text):
            kind = mo.lastgroup
            value = mo.group()
            start = mo.start()
            length = mo.end() - start

            if kind == "IDENT":
                if value in keywords.KEYWORDS:
                    self.setFormat(start, length, self.highlight_rule.keyword)
                elif value in keywords.LITERALS:
                    self.setFormat(start, length, self.highlight_rule.literal)
                elif value in keywords.BUILTINS:
                    self.setFormat(start, length, self.highlight_rule.builtin)
            elif kind == "STRING":
                self.setFormat(start, length, self.highlight_rule.string)
            elif kind == "NUMBER":
                self.setFormat(start, length, self.highlight_rule.number)
            elif kind == "SKIP":
                continue
