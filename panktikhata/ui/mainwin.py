# -*- coding: utf-8 -*-
from PySide6 import QtCore, QtGui, QtWidgets  # type: ignore
from PySide6.QtGui import QAction, QIcon  # type: ignore
from PySide6.QtWidgets import QStyle  # type: ignore
import qdarktheme

from ui.highlighter import PanktiSyntaxHighlighter
from ui.settingsdlg import PanktiSettingsDialog
from assets import resources


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()
        self.setup_theme()

    def setup_theme(self) -> None:
        qdarktheme.setup_theme()

    def setup_ui(self) -> None:
        if not self.objectName():
            self.setObjectName("MainWindow")

        # self.setStyleSheet(defaultLight.themeDefaultLight)

        self.resize(800, 600)
        self.root_widget = QtWidgets.QWidget()
        self.root_widget.setObjectName("rootWidget")
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.root_widget)
        self.horizontal_layout.setObjectName("horizontalLayout_3")
        self.main_box = QtWidgets.QHBoxLayout()
        self.main_box.setObjectName("mainBox")
        self.editor_box = QtWidgets.QHBoxLayout()
        self.editor_box.setObjectName("EditorBox")
        self.button_frame = QtWidgets.QFrame(self.root_widget)
        self.button_frame.setObjectName("ButtonFrame")
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.button_frame.sizePolicy().hasHeightForWidth()
        )
        self.button_frame.setSizePolicy(size_policy)

        self.button_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.button_frame.setFrameShadow(
            QtWidgets.QFrame.Shadow.Raised
        )  # QFrame.Raised)
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.button_frame)
        self.vertical_layout_2.setObjectName("verticalLayout_2")
        self.button_box = QtWidgets.QVBoxLayout()
        self.button_box.setObjectName("ButtonBox")

        self.run_pm = QStyle.StandardPixmap.SP_MediaPlay

        self.run_icon = self.style().standardIcon(self.run_pm)

        self.run_button = QtWidgets.QPushButton(self.button_frame)
        self.run_button.setObjectName("RunButton")
        self.run_button.setIcon(self.run_icon)
        self.run_button.clicked.connect(self.btn_click)
        self.button_box.addWidget(
            self.run_button, 0, QtGui.Qt.AlignmentFlag.AlignTop
        )
        self.vertical_layout_2.addLayout(self.button_box)

        self.editor_box.addWidget(
            self.button_frame, 0, QtGui.Qt.AlignmentFlag.AlignTop
        )

        self.editor_splitter = QtWidgets.QSplitter(self.root_widget)
        self.editor_splitter.setObjectName("EditorSplitter")
        self.editor_splitter.setOrientation(QtGui.Qt.Orientation.Vertical)
        self.input_edit = QtWidgets.QPlainTextEdit(self.editor_splitter)

        self.highligher = PanktiSyntaxHighlighter(self.input_edit.document())

        self.input_edit.setObjectName("InputEdit")
        self.editor_splitter.addWidget(self.input_edit)

        self.output_edit = QtWidgets.QPlainTextEdit(self.editor_splitter)
        self.output_edit.setObjectName("OutputEdit")
        self.editor_splitter.addWidget(self.output_edit)

        self.editor_box.addWidget(self.editor_splitter)

        self.main_box.addLayout(self.editor_box)

        self.horizontal_layout.addLayout(self.main_box)

        self.setCentralWidget(self.root_widget)
        self.menubar = QtWidgets.QMenuBar()
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslate_ui()
        self.setup_menu()

        QtCore.QMetaObject.connectSlotsByName(self)

    def setup_menu(self):
        self.new_menu_action = QAction(
            QIcon(":/icons/description.svg"), "&New", self
        )
        self.open_menu_action = QAction(
            QIcon(":/icons/folder_open.svg"), "&Open", self
        )
        self.save_menu_action = QAction(
            QIcon(":/icons/save.svg"), "&Save", self
        )

        self.quit_menu_action = QAction(
            QIcon(":/icons/power_settings_new.svg"), "&Quit", self
        )

        self.file_menu = self.menubar.addMenu("&File")
        self.file_menu.addAction(self.new_menu_action)
        self.file_menu.addAction(self.open_menu_action)
        self.file_menu.addAction(self.save_menu_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.quit_menu_action)

        self.undo_menu_action = QAction()
        self.redo_menu_action = QAction()
        self.cut_menu_action = QAction()

        self.copy_menu_action = QAction()
        self.paste_menu_action = QAction()
        self.select_all_menu_action = QAction()

        self.find_menu_action = QAction()
        self.find_and_replace_menu_ction = QAction()

        self.setMenuBar(self.menubar)

    def btn_click(self, s):
        dlg = PanktiSettingsDialog()
        dlg.exec()

    def retranslate_ui(self):
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Pankti Khata", None
            )
        )
