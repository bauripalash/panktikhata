from dataclasses import dataclass
import re
from PySide6 import QtGui # type: ignore
from PySide6.QtGui import (QBrush, QColor,QSyntaxHighlighter, QTextCharFormat) # type: ignore

from pankti import keywords
from themes.syntaxstyle import atom_one_light

@dataclass
class HighlightRule:
    keyword: QtGui.QTextCharFormat
    literal: QtGui.QTextCharFormat
    string: QtGui.QTextCharFormat
    number: QtGui.QTextCharFormat
    builtin: QtGui.QTextCharFormat
    bg: QtGui.QTextCharFormat|None = None
    fg: QtGui.QTextCharFormat|None = None

class PanktiSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(QBrush(QColor(atom_one_light.theme.keyword)))

        literalFormat = QTextCharFormat()
        literalFormat.setForeground(QBrush(QColor(atom_one_light.theme.literal)))

        stringFormat = QTextCharFormat()
        stringFormat.setForeground(QBrush(QColor(atom_one_light.theme.string)))


        numberFormat = QTextCharFormat()
        numberFormat.setForeground(QBrush(QColor(atom_one_light.theme.number)))

        builtinFormat = QTextCharFormat()
        builtinFormat.setForeground(QBrush(QColor(atom_one_light.theme.builtin)))

       
        self.highlightRule = HighlightRule(
            keyword=keywordFormat,
            literal=literalFormat,
            string=stringFormat,
            number=numberFormat,
            builtin=builtinFormat
        )

        self.tokregex = keywords.getPatterns()
        


    def highlightBlock(self, text: str) -> None:
        for mo in re.finditer(self.tokregex, text):
            kind = mo.lastgroup
            value = mo.group()
            start = mo.start()
            length = mo.end() - start

            if kind == 'IDENT':
                if value in keywords.KEYWORDS:
                    self.setFormat(start, length, self.highlightRule.keyword)
                elif value in keywords.LITERALS:
                    self.setFormat(start, length, self.highlightRule.literal)
                elif value in keywords.BUILTINS:
                    self.setFormat(start, length, self.highlightRule.builtin)
            elif kind == "STRING":
                self.setFormat(start, length, self.highlightRule.string)
            elif kind == "NUMBER":
                self.setFormat(start, length, self.highlightRule.number)
            elif kind == "SKIP":
                continue

