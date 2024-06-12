from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtGui import QFont, QFontDatabase, QKeyEvent, QTextCursor
from PySide6.QtWidgets import QCompleter, QPlainTextEdit
from pankti.keywords import KEYWORDS, LITERALS, BUILTINS


class PanktiEditor(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.comp_words = []
        self.comp_words.extend(KEYWORDS)
        self.comp_words.extend(LITERALS)
        self.comp_words.extend(BUILTINS)

        self.comps = QStringListModel(self.comp_words)
        self.completer =  QCompleter(self.comps, self)
        self.completer.setWidget(self)

        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.activated.connect(self.insert_completion)

        
        self.setFont(QFont("Noto Serif Bengali", 14))

        self.tail : str = " "
        self.ignore_return : bool = False


    def complete(self):
        cur = self.textCursor()
        cur.select(QTextCursor.SelectionType.WordUnderCursor)

        selected = cur.selectedText()

        if selected:
            self.completer.setCompletionPrefix(selected)
            popup = self.completer.popup()

            popup.setCurrentIndex(self.completer.completionModel().index(0, 0))
            cr = self.cursorRect()
            cr.setWidth(popup.sizeHintForColumn(0)
                        + popup.verticalScrollBar().sizeHint().width())

            self.completer.complete(cr)
        else:
            self.completer.popup().hide()

    def insert_completion(self , comp) -> None:
        cur = self.textCursor()
        cur.select(QTextCursor.SelectionType.WordUnderCursor)
        cur.insertText(comp + self.tail)

    def keyPressEvent(self, e: QKeyEvent) -> None:
        if self.completer.popup().isVisible() and e.key() in [
                Qt.Key.Key_Up,
                Qt.Key.Key_Down,
                Qt.Key.Key_Enter,
                Qt.Key.Key_Return,
                Qt.Key.Key_Tab,
                Qt.Key.Key_Backtab,

        ]:
            e.ignore()
            return

        if e.key() == Qt.Key.Key_Tab:
            e.ignore()
        elif e.key() == Qt.Key.Key_Backtab:
            e.ignore()
            return

        if self.ignore_return and e.key() in [
                Qt.Key.Key_Enter,
                Qt.Key.Key_Return
        ]:
            e.ignore()
            return

        old_len = self.document().characterCount()
        super().keyPressEvent(e)

        if e.text().strip() and self.document().characterCount() > old_len:
            self.complete()
        elif self.completer.popup().isVisible():
            self.completer.popup().hide()
