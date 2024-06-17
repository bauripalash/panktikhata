from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtCore import QRect, QStringListModel, Qt, QSize, Slot
from PySide6.QtGui import (
    QColor,
    QKeyEvent,
    QPainter,
    QTextCursor,
    QPaintEvent,
    QResizeEvent,
)
from PySide6.QtWidgets import QCompleter, QPlainTextEdit, QWidget
from pankti.keywords import KEYWORDS, LITERALS, BUILTINS
from themes.syntaxclass import SyntaxStyle, dummy_syntaxstyle


class EditorLineNumberArea(QtWidgets.QWidget):
    def __init__(self, editor) -> None:
        QWidget.__init__(self, editor)
        self._code_editor = editor

    def sizeHint(self) -> QSize:
        return QSize(self._code_editor.line_number_area_width(), 0)

    def paintEvent(self, event: QPaintEvent) -> None:
        self._code_editor.line_number_area_pain_event(event)


class PanktiEditor(QPlainTextEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.line_number_area: QtWidgets.QWidget = EditorLineNumberArea(self)
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.update_line_number_area_width(0)

        self.comp_words = []
        self.comp_words.extend(KEYWORDS)
        self.comp_words.extend(LITERALS)
        self.comp_words.extend(BUILTINS)

        self.comps = QStringListModel(self.comp_words)
        self.completer = QCompleter(self.comps, self)
        self.completer.setWidget(self)

        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.activated.connect(self.insert_completion)

        # self.setFont(QFont("Noto Serif Bengali", 14))
        self.syntaxstyle: SyntaxStyle = dummy_syntaxstyle()
        self.use_space_indent: bool = True
        self.tab_width: int = 4

        self.tail: str = " "
        self.ignore_return: bool = False

    def line_number_area_width(self):
        digits = 1
        max_num = max(1, self.blockCount())

        while max_num >= 10:
            max_num *= 0.1
            digits += 1
        space = 3 + self.fontMetrics().horizontalAdvance("9") * digits
        return space

    def resizeEvent(self, e: QResizeEvent) -> None:
        super().resizeEvent(e)
        cr = self.contentsRect()
        width = self.line_number_area_width()
        rect = QRect(cr.left(), cr.top(), width, cr.height())
        self.line_number_area.setGeometry(rect)

    def line_number_area_pain_event(self, event) -> None:
        painter = QPainter(self.line_number_area)
        painter.setFont(self.font())
        painter.fillRect(event.rect(), QColor(self.syntaxstyle.bg))
        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        offset = self.contentOffset()
        top = self.blockBoundingGeometry(block).translated(offset).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(QColor(self.syntaxstyle.fg))
                width = self.line_number_area.width()
                height = self.fontMetrics().height()

                painter.drawText(
                    0,
                    int(top),
                    width,
                    height,
                    Qt.AlignmentFlag.AlignRight,
                    number,
                )

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

        painter.end()

    @Slot()
    def update_line_number_area_width(self, _):
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    @Slot()
    def update_line_number_area(self, rect, dy):
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            width = self.line_number_area.width()
            self.line_number_area.update(0, rect.y(), width, rect.height())
        if rect.contains(self.viewport().rect()):
            self.update_line_number_area_width(0)

    def complete(self):
        cur = self.textCursor()
        cur.select(QTextCursor.SelectionType.WordUnderCursor)

        selected = cur.selectedText()

        if selected:
            self.completer.setCompletionPrefix(selected)
            popup = self.completer.popup()

            popup.setCurrentIndex(self.completer.completionModel().index(0, 0))
            cr = self.cursorRect()
            cr.setWidth(
                popup.sizeHintForColumn(0)
                + popup.verticalScrollBar().sizeHint().width()
            )

            self.completer.complete(cr)
        else:
            self.completer.popup().hide()

    def insert_completion(self, comp) -> None:
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
            if self.use_space_indent:
                self.insertPlainText(self.tab_width * " ")
                e.accept()
                # e.ignore()
                return
            else:
                e.ignore()
        elif e.key() == Qt.Key.Key_Backtab:
            e.ignore()
            return

        if self.ignore_return and e.key() in [
            Qt.Key.Key_Enter,
            Qt.Key.Key_Return,
        ]:
            e.ignore()
            return

        old_len = self.document().characterCount()
        super().keyPressEvent(e)

        if e.text().strip() and self.document().characterCount() > old_len:
            self.complete()
        elif self.completer.popup().isVisible():
            self.completer.popup().hide()
