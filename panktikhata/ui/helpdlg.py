from PySide6 import QtWidgets, QtGui, QtCore

help_text = """ # Help
#### Running Code
* Write code here
* Click Run"""


class PanktiHelpDialog(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.resize(726, 621)
        self.main_layout = QtWidgets.QGridLayout(self)
        self.grid_layout = QtWidgets.QGridLayout()
        self.scroll_area = QtWidgets.QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_contents = QtWidgets.QWidget()
        self.scroll_area_contents.setGeometry(QtCore.QRect(0, 0, 708, 603))
        self.grid_layout_2 = QtWidgets.QGridLayout(self.scroll_area_contents)
        self.label = QtWidgets.QLabel(self.scroll_area_contents)
        self.label.setTextFormat(QtGui.Qt.TextFormat.MarkdownText)
        sp = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(0)
        sp.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sp)
        self.label.setAlignment(
            QtGui.Qt.AlignmentFlag.AlignLeading
            | QtGui.Qt.AlignmentFlag.AlignLeft
            | QtGui.Qt.AlignmentFlag.AlignTop
        )
        self.grid_layout_2.addWidget(self.label, 0, 0, 1, 1)
        self.scroll_area.setWidget(self.scroll_area_contents)
        self.grid_layout.addWidget(self.scroll_area, 0, 0, 1, 1)
        self.main_layout.addLayout(self.grid_layout, 0, 0, 1, 1)

        self.label.setText(help_text)
