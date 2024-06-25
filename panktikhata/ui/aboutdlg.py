from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QPixmap

import pankti


class PanktiAboutDialog(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.logo = QPixmap(":/appicons/icon.ico")
        self.setup_ui()

    def setup_ui(self) -> None:
        self.setFixedSize(500, 400)
        self.setWindowIcon(self.logo)
        self.setWindowTitle("About PanktiKhata")

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.title_label = QtWidgets.QLabel(self)

        sp = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(0)
        sp.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sp)
        self.title_label.setTextFormat(QtGui.Qt.TextFormat.MarkdownText)
        self.title_label.setAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)

        self.vertical_layout.addWidget(self.title_label)

        self.info_label = QtWidgets.QLabel(self)
        sp.setHeightForWidth(self.info_label.sizePolicy().hasHeightForWidth())
        self.info_label.setSizePolicy(sp)
        self.info_label.setTextFormat(QtGui.Qt.TextFormat.MarkdownText)
        self.info_label.setWordWrap(True)

        self.vertical_layout.addWidget(self.info_label)

        self.version_label = QtWidgets.QLabel(self)
        sp.setHeightForWidth(
            self.version_label.sizePolicy().hasHeightForWidth()
        )
        self.version_label.setSizePolicy(sp)
        self.version_label.setAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)

        self.vertical_layout.addWidget(self.version_label)

        self.copyright_label = QtWidgets.QLabel(self)
        sp.setHeightForWidth(
            self.copyright_label.sizePolicy().hasHeightForWidth()
        )
        self.copyright_label.setSizePolicy(sp)
        self.copyright_label.setAlignment(QtGui.Qt.AlignmentFlag.AlignCenter)

        self.vertical_layout.addWidget(self.copyright_label)

        self.main_layout.addLayout(self.vertical_layout)
        self.title_label.setText(
            """<div>
                <img src=":/appicons/logo_96x.png"></img>
                <h3>Pankti Khata</h3>
            </div>
            """
        )
        self.info_label.setText(
            "Fully Featured IDE for Pankti Programming Language, a real and practical programming language"
        )
        self.version_label.setText(f"Version: {pankti.version}")
        self.copyright_label.setText("Copyright (C) 2024 Palash Bauri.")
