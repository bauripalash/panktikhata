# -*- coding: utf-8 -*-
from PySide6 import QtCore, QtGui, QtWidgets  # type: ignore
from PySide6.QtGui import QAction, QFont, QFontDatabase, QIcon  # type: ignore
from PySide6.QtWidgets import QStyle  # type: ignore
import qdarktheme

from pankti import settings
from ui.editor import PanktiEditor
from themes import syntaxclass
from ui.highlighter import PanktiSyntaxHighlighter
from ui.settingsdlg import PanktiSettingsDialog

try:
    from assets import resources  # noqa: F401
except ImportError:
    pass


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = self.load_settings()

        self.setup_theme()
        self.setup_ui()
        self.setup_font()

    def load_settings(self) -> settings.PanktiSettings:
        configpath, ok = settings.config_save_path(False)
        print(ok)
        s, _ = settings.get_settings_from_conf(configpath)
        return s

    def setup_theme(self) -> None:
        self.fontdb = QFontDatabase()

        self.fontdb.addApplicationFont(":/fonts/noto_regular.ttf")
        self.fontdb.addApplicationFont(":/fonts/noto_bold.ttf")
        self.editor_stylesheet = syntaxclass.get_stylesheet(
            self.settings.editor_theme, self.settings.font_size
        )
        qdarktheme.setup_theme(
            theme=settings.app_theme_to_str(self.settings.app_theme),
            additional_qss=self.editor_stylesheet,
        )

        # print(self.editor_stylesheet)

    def setup_font(self) -> None:
        self.editor_font = QFont("Noto Serif Bengali", self.settings.font_size)
        self.input_edit.setFont(self.editor_font)
        self.output_edit.setFont(self.editor_font)

    def setup_ui(self) -> None:
        self.autocomplete_words = ["dhori", "kaj", "nil"]

        self.resize(800, 600)
        self.root_widget = QtWidgets.QWidget()
        self.horizontal_layout = QtWidgets.QHBoxLayout(self.root_widget)
        self.main_box = QtWidgets.QHBoxLayout()
        self.editor_box = QtWidgets.QHBoxLayout()
        self.button_frame = QtWidgets.QFrame(self.root_widget)
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
        self.button_box = QtWidgets.QVBoxLayout()

        self.run_pm = QStyle.StandardPixmap.SP_MediaPlay

        self.run_icon = self.style().standardIcon(self.run_pm)

        self.run_button = QtWidgets.QPushButton(self.button_frame)
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
        self.editor_splitter.setOrientation(QtGui.Qt.Orientation.Vertical)
        self.input_edit = PanktiEditor(self.editor_splitter)
        # self.input_edit.comps.setStringList(["dhori", "kaj"])

        # QtWidgets.QPlainTextEdit(self.editor_splitter)

        self.highlighter = PanktiSyntaxHighlighter(self.input_edit.document())
        self.highlighter.set_theme(self.settings.editor_theme)

        self.editor_splitter.addWidget(self.input_edit)

        self.output_edit = QtWidgets.QPlainTextEdit(self.editor_splitter)
        self.editor_splitter.addWidget(self.output_edit)

        self.editor_box.addWidget(self.editor_splitter)

        self.main_box.addLayout(self.editor_box)

        self.horizontal_layout.addLayout(self.main_box)

        self.setCentralWidget(self.root_widget)
        self.menubar = QtWidgets.QMenuBar()
        self.statusbar = QtWidgets.QStatusBar()
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

        self.undo_menu_action = QAction(
            QIcon(":/icons/undo.svg"),
            "&Undo",
            self,
        )
        self.redo_menu_action = QAction(
            QIcon(":/icons/redo.svg"),
            "&Redo",
            self,
        )
        self.cut_menu_action = QAction(
            QIcon(":/icons/cut.svg"),
            "&Cut",
            self,
        )
        self.copy_menu_action = QAction(
            QIcon(":/icons/copy.svg"),
            "&Copy",
            self,
        )
        self.paste_menu_action = QAction(
            QIcon(":/icons/paste.svg"),
            "&Paste",
            self,
        )
        self.select_all_menu_action = QAction(
            QIcon(":/icons/select_all.svg"),
            "&Select All",
            self,
        )

        self.find_menu_action = QAction(
            QIcon(":/icons/search.svg"),
            "&Find",
            self,
        )
        self.find_and_replace_menu_ction = QAction(
            QIcon(":/icons/find_replace.svg"),
            "&Find & Replace",
            self,
        )

        self.edit_menu = self.menubar.addMenu("&Edit")
        self.edit_menu.addAction(self.undo_menu_action)
        self.edit_menu.addAction(self.redo_menu_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.cut_menu_action)
        self.edit_menu.addAction(self.copy_menu_action)
        self.edit_menu.addAction(self.paste_menu_action)
        self.edit_menu.addAction(self.select_all_menu_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.find_menu_action)
        self.edit_menu.addAction(self.find_and_replace_menu_ction)

        self.setMenuBar(self.menubar)

    def redraw_settings(self) -> None:
        self.highlighter.set_theme(self.settings.editor_theme)
        self.setup_theme()
        self.input_edit.update()
        self.output_edit.update()

        self.setup_font()

    def show_message_box(self, text: str) -> None:
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(text)
        msgbox.exec()

    def btn_click(self, _):
        dlg = PanktiSettingsDialog()
        dlg.setup(self.settings)
        dlg.exec()

        if dlg.save:
            self.settings = dlg.settings_value
            self.redraw_settings()
            # print(self.settings.to_pickle().decode())
            # self.settings.dump_settings("./panktikhata.pickle")
            config_path, ok = settings.config_save_path(True)
            if not ok:
                self.show_message_box("Failed to save config")
            else:
                self.settings.dump_settings(config_path)

        else:
            dlg.destroy()

    def retranslate_ui(self):
        self.setWindowTitle(
            QtCore.QCoreApplication.translate(
                "MainWindow", "Pankti Khata", None
            )
        )
