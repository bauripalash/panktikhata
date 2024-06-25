# -*- coding: utf-8 -*-
from pathlib import Path
import tempfile
import typing
from PySide6 import QtCore, QtGui, QtWidgets  # type: ignore
from PySide6.QtGui import QAction, QFont, QFontDatabase, QIcon  # type: ignore
from PySide6.QtCore import QProcess, QStringListModel, QThreadPool
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
    def close(self) -> bool:
        if self.pankti_process is not None:
            self.pankti_process.close()

        return super().close()

    def __init__(self):
        super().__init__()

        self.settings = self.load_settings()
        self.enable_themes: bool = True
        self.thread_mgr = QThreadPool()
        self.pankti_process = None
        self.temp_file = None
        self.filename: str | None = None
        self.is_file_unsaved = False
        self.title_unsave_marked = False

        if self.enable_themes:
            self.setup_theme()
        self.setup_ui()
        self.setup_font()

    def load_settings(self) -> settings.PanktiSettings:
        configpath, _ = settings.config_save_path(False)
        # print(ok)
        s, _ = settings.get_settings_from_conf(configpath)
        return s

    def setup_theme(self) -> None:
        self.fontdb = QFontDatabase()

        self.fontdb.addApplicationFont(":/fonts/noto_regular.ttf")
        self.fontdb.addApplicationFont(":/fonts/noto_bold.ttf")
        self.editor_stylesheet = syntaxclass.get_stylesheet(
            self.settings.editor_theme,
        )

        qdarktheme.setup_theme(
            theme=settings.app_theme_to_str(self.settings.app_theme),
            additional_qss=self.editor_stylesheet,
        )

        # print(self.editor_stylesheet)

    def setup_font(self) -> None:
        self.editor_font = QFont("Noto Serif Bengali", self.settings.font_size)
        self.input_edit.setFont(self.editor_font)
        self.input_edit.syntaxstyle = self.settings.editor_theme
        # self.input_edit.linepainter.setFont(self.editor_font)
        self.output_font = QFont(
            "Noto Serif Bengali",
            self.settings.output_font_size,
        )
        self.output_edit.setFont(self.output_font)

    def setup_ui(self) -> None:
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

        self.run_icon = QIcon(":/icons/play_arrow.svg")
        self.stop_icon = QIcon(":/icons/stop.svg")

        self.run_button = QtWidgets.QPushButton(self.button_frame)
        self.run_button.setIcon(self.run_icon)
        self.run_button.clicked.connect(self.run_btn_click)
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
        self.input_edit.setObjectName("input_edit")
        fontwidth = QtGui.QFontMetrics(
            self.input_edit.font()
        ).averageCharWidth()
        self.input_edit.setTabStopDistance(4 * fontwidth)
        self.input_edit.modificationChanged.connect(self.input_modified_update)

        self.input_edit.undoAvailable.connect(self.undo_enable)
        self.input_edit.redoAvailable.connect(self.redo_enable)

        self.highlighter = PanktiSyntaxHighlighter(self.input_edit.document())
        self.highlighter.set_theme(self.settings.editor_theme)

        self.editor_splitter.addWidget(self.input_edit)

        self.output_edit = QtWidgets.QPlainTextEdit(self.editor_splitter)
        self.output_edit.setObjectName("output_edit")
        self.editor_splitter.addWidget(self.output_edit)

        self.editor_box.addWidget(self.editor_splitter)

        self.main_box.addLayout(self.editor_box)

        self.horizontal_layout.addLayout(self.main_box)

        self.setCentralWidget(self.root_widget)
        self.menubar = QtWidgets.QMenuBar()
        self.statusbar = QtWidgets.QStatusBar()
        self.setStatusBar(self.statusbar)

        self.update_title_with_filename()
        self.setup_menu()

        QtCore.QMetaObject.connectSlotsByName(self)

    def setup_menu(self):
        self.new_menu_action = QAction(
            QIcon(":/icons/description.svg"), "&New", self
        )
        self.open_menu_action = QAction(
            QIcon(":/icons/folder_open.svg"), "&Open", self
        )
        self.open_menu_action.setShortcut("Ctrl+O")

        self.open_menu_action.triggered.connect(self.open_file)

        self.save_menu_action = QAction(
            QIcon(":/icons/save.svg"), "&Save", self
        )

        self.save_menu_action.setShortcut("Ctrl+S")

        self.save_menu_action.triggered.connect(self.save_file)

        self.save_as_menu_action = QAction(
            QIcon(":/icons/save_as.svg"), "&Save as", self
        )

        self.save_as_menu_action.setShortcut("Ctrl+Shift+S")

        self.save_as_menu_action.triggered.connect(self.save_as_file)

        self.quit_menu_action = QAction(
            QIcon(":/icons/power_settings_new.svg"), "&Quit", self
        )

        self.file_menu = self.menubar.addMenu("&File")
        self.file_menu.addAction(self.new_menu_action)
        self.file_menu.addAction(self.open_menu_action)
        self.file_menu.addAction(self.save_menu_action)
        self.file_menu.addAction(self.save_as_menu_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.quit_menu_action)

        self.undo_menu_action = QAction(
            QIcon(":/icons/undo.svg"),
            "&Undo",
            self,
        )

        self.undo_menu_action.setShortcut("Ctrl+Z")
        self.undo_menu_action.triggered.connect(self.undo_clicked)
        self.undo_menu_action.setEnabled(False)

        self.redo_menu_action = QAction(
            QIcon(":/icons/redo.svg"),
            "&Redo",
            self,
        )
        self.redo_menu_action.setShortcut("Ctrl+Shift+Z")
        self.redo_menu_action.triggered.connect(self.redo_clicked)
        self.redo_menu_action.setEnabled(False)

        self.cut_menu_action = QAction(
            QIcon(":/icons/cut.svg"),
            "&Cut",
            self,
        )

        self.cut_menu_action.setShortcut("Ctrl+X")
        self.cut_menu_action.triggered.connect(self.cut_clicked)

        self.copy_menu_action = QAction(
            QIcon(":/icons/copy.svg"),
            "&Copy",
            self,
        )

        self.copy_menu_action.setShortcut("Ctrl+C")
        self.copy_menu_action.triggered.connect(self.copy_clicked)

        self.paste_menu_action = QAction(
            QIcon(":/icons/paste.svg"),
            "&Paste",
            self,
        )

        self.paste_menu_action.setShortcut("Ctrl+V")
        self.paste_menu_action.triggered.connect(self.paste_clicked)

        self.select_all_menu_action = QAction(
            QIcon(":/icons/select_all.svg"),
            "&Select All",
            self,
        )

        self.select_all_menu_action.setShortcut("Ctrl+A")
        self.select_all_menu_action.triggered.connect(
            self.select_all_clicked,
        )

        self.find_menu_action = QAction(
            QIcon(":/icons/search.svg"),
            "&Find",
            self,
        )
        self.find_and_replace_menu_action = QAction(
            QIcon(":/icons/find_replace.svg"),
            "&Find & Replace",
            self,
        )

        self.settings_menu_action = QAction(
            QIcon(":/icons/settings.svg"),
            "&Settings",
            self,
        )

        self.settings_menu_action.triggered.connect(
            self.settings_btn_click,
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
        self.edit_menu.addAction(self.find_and_replace_menu_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.settings_menu_action)

        self.run_menu_action = QAction(
            QIcon(":/icons/play_arrow.svg"),
            "&Run",
            self,
        )

        self.clear_output_menu_action = QAction(
            QIcon(":/icons/mop.svg"),
            "&Clear Output",
            self,
        )

        self.examples_menu_action = QAction(
            QIcon(":/icons/shopping_bag.svg"),
            "&Examples",
            self,
        )

        self.clear_output_menu_action.triggered.connect(
            self.clear_output_clicked,
        )

        self.run_menu = self.menubar.addMenu("&Run")
        self.run_menu.addAction(self.run_menu_action)
        self.run_menu.addAction(self.examples_menu_action)
        self.run_menu.addAction(self.clear_output_menu_action)

        self.help_menu_action = QAction(
            QIcon(":/icons/support.svg"),
            "&Help",
            self,
        )
        self.about_menu_action = QAction(
            QIcon(":/icons/about.svg"),
            "&About",
            self,
        )
        self.learn_menu_action = QAction(
            QIcon(":/icons/book.svg"),
            "&Learn Pankti",
            self,
        )
        self.help_menu = self.menubar.addMenu("&Help")
        self.help_menu.addAction(self.help_menu_action)
        self.help_menu.addAction(self.about_menu_action)
        self.help_menu.addAction(self.learn_menu_action)

        self.setMenuBar(self.menubar)

    def clear_output_clicked(self, _) -> None:
        self.output_edit.clear()

    def select_all_clicked(self, _) -> None:
        self.input_edit.selectAll()

    def cut_clicked(self, _) -> None:
        self.input_edit.cut()

    def copy_clicked(self, _) -> None:
        self.input_edit.copy()

    def paste_clicked(self, _) -> None:
        self.input_edit.paste()

    def undo_enable(self, flag: bool) -> None:
        self.undo_menu_action.setEnabled(flag)

    def undo_clicked(self, _) -> None:
        self.input_edit.undo()

    def redo_enable(self, flag: bool) -> None:
        self.redo_menu_action.setEnabled(flag)

    def redo_clicked(self, _) -> None:
        self.input_edit.redo()

    def input_modified_update(self, _) -> None:
        self.update_title_with_filename()

    def update_title_with_filename(self) -> None:
        f = "untitled"
        unsaved_marker = ""
        if self.input_edit.document().isModified():
            unsaved_marker = "*"
        if self.filename is not None:
            f = Path(self.filename).name

        self.setWindowTitle(f"Pankti Khata ({unsaved_marker}{f})")

    def _save_file(self, ignore_filename: bool = False) -> None:
        if self.filename is None or ignore_filename:
            dlg = QtWidgets.QFileDialog()
            dlg.setNameFilters(["Pankti Source Code (*.pank)", "Any File (*)"])
            dlg.setViewMode(QtWidgets.QFileDialog.ViewMode.Detail)
            dlg.setDefaultSuffix("pank")
            dlg.setOptions(QtWidgets.QFileDialog.Option.DontUseNativeDialog)
            dlg.setAcceptMode(QtWidgets.QFileDialog.AcceptMode.AcceptSave)
            flist: QStringListModel = QStringListModel()
            if dlg.exec_():
                f = dlg.selectedFiles()

            if len(flist.stringList()) < 1:
                return

            fname = flist.stringList()[0]

            with open(fname, "w") as f:
                f.write(self.input_edit.toPlainText())
                self.filename = fname

                self.input_edit.document().setModified(False)
                self.update_title_with_filename()
        else:
            # Todo : show msg about file not being on storage and
            # give options to save if file doesn't exist

            with open(self.filename, "w") as f:
                f.write(self.input_edit.toPlainText())

                self.input_edit.document().setModified(False)

    def save_file(self, _) -> None:
        self._save_file()

    def save_as_file(self, _) -> None:
        self._save_file(True)

    def open_file(self, _) -> None:
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open Pankti Source File",
            "",
            "Pankti Source File (*.pank);;Any File (*)",
            options=QtWidgets.QFileDialog.Option.DontUseNativeDialog,
        )

        if len(fname) < 1:
            return

        f = Path(fname)

        if not f.exists() or not f.is_file():
            self.show_message_box(f"Failed to {fname}. No Such file exists!")
            return

        with open(fname, "r") as f:
            self.input_edit.setPlainText(f.read())
            self.filename = fname

            self.input_edit.document().setModified(False)
            self.update_title_with_filename()

    def redraw_settings(self) -> None:
        self.highlighter.set_theme(
            self.settings.editor_theme,
        )
        self.setup_theme()
        self.input_edit.update()
        self.output_edit.update()

        self.setup_font()

    def show_message_box(self, text: str) -> None:
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(text)
        msgbox.exec()

    def handle_pankti_stdout(self) -> None:
        if self.pankti_process is not None:
            d = self.pankti_process.readAllStandardOutput()
            self.output_edit.appendPlainText(d.toStdString())
            self.output_edit.ensureCursorVisible()

    def handle_pankti_stderr(self) -> None:
        if self.pankti_process is not None:
            d = self.pankti_process.readAllStandardError()
            self.output_edit.appendPlainText(d.toStdString())
            self.output_edit.ensureCursorVisible()

    def run_code_finished(self) -> None:
        if self.temp_file is not None:
            self.temp_file.close()
            self.temp_file = None

        self.pankti_process = None

        # self.output_edit.appendPlainText("\n-- process finished --")
        self.run_button.setIcon(self.run_icon)
        self.run_button.clicked.disconnect()
        self.run_button.clicked.connect(self.run_btn_click)

    def handle_pankti_process_state(
        self, state: QProcess.ProcessState
    ) -> None:
        if state == QProcess.ProcessState.Running:
            self.run_button.setIcon(self.stop_icon)
            self.run_button.clicked.disconnect()
            self.run_button.clicked.connect(self.stop_btn_click)

    def run_src_code(self) -> None:
        if self.pankti_process is not None:
            return

        if self.temp_file is not None:
            self.temp_file.close()

        src = self.input_edit.toPlainText()

        pankti_path = Path(self.settings.pankti_path)

        self.temp_file = tempfile.NamedTemporaryFile()
        self.temp_file.write(src.encode())
        self.temp_file.flush()

        self.pankti_process = QProcess()
        self.pankti_process.finished.connect(self.run_code_finished)
        self.pankti_process.readyReadStandardError.connect(
            self.handle_pankti_stderr
        )
        self.pankti_process.readyReadStandardOutput.connect(
            self.handle_pankti_stdout
        )
        self.pankti_process.stateChanged.connect(
            self.handle_pankti_process_state
        )

        self.pankti_process.start(str(pankti_path), [self.temp_file.name])

        # print(self.pankti_process.program() , self.pankti_process.arguments())

    def run_btn_click(self, _) -> None:
        self.run_src_code()

    def stop_btn_click(self, _) -> None:
        if self.pankti_process is not None:
            self.pankti_process.close()

    def settings_btn_click(self, _):
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
