# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtGui, QtWidgets

from pankti.settings import (
    AppLanguage,
    AppTheme,
    PanktiSettings,
    app_theme_to_str,
)
from themes.syntaxstyle import THEMES  # type: ignore

APP_THEMES = {
    "auto": ("Auto", AppTheme.AUTO),
    "dark": ("Dark", AppTheme.DARK),
    "light": ("Light", AppTheme.LIGHT),
}
LANGUAGE_ITEMS = {
    "en": ("English", AppLanguage.ENGLISH),
    "bn": ("Bengali", AppLanguage.BENGALI),
}  # type : Dict[str, str]

EDITOR_THEMES = [(key, value.tname) for key, value in THEMES.items()]


class PanktiSettingsDialog(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.settings_value = PanktiSettings()
        self.save = False

    def setup(self, s: PanktiSettings):
        self.settings_value = s
        self.setup_ui()

    def setup_ui(self) -> None:
        self.resize(539, 447)
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.settings_header_label = QtWidgets.QLabel(self)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.settings_header_label.sizePolicy().hasHeightForWidth()
        )
        self.settings_header_label.setSizePolicy(size_policy)
        self.settings_header_label.setAlignment(
            QtGui.Qt.AlignmentFlag.AlignHCenter
        )

        self.main_layout.addWidget(
            self.settings_header_label, 0, QtGui.Qt.AlignmentFlag.AlignHCenter
        )

        self.scroll_area = QtWidgets.QScrollArea(self)
        size_policy1 = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        size_policy1.setHorizontalStretch(0)
        size_policy1.setVerticalStretch(0)
        size_policy1.setHeightForWidth(
            self.scroll_area.sizePolicy().hasHeightForWidth()
        )
        self.scroll_area.setSizePolicy(size_policy1)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget_contents = QtWidgets.QWidget()
        self.scroll_area_widget_contents.setGeometry(
            QtCore.QRect(0, 0, 521, 347)
        )
        self.vertical_layout = QtWidgets.QVBoxLayout(
            self.scroll_area_widget_contents
        )

        # First Row -> Font Size
        self.font_size_hl = QtWidgets.QHBoxLayout()
        self.font_size_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )
        self.font_size_label.setText("Font Size")

        self.font_size_spin_box = QtWidgets.QSpinBox(
            self.scroll_area_widget_contents
        )

        self.font_size_spin_box.setValue(self.settings_value.font_size)

        self.font_size_hl.addWidget(self.font_size_label)
        self.font_size_hl.addWidget(self.font_size_spin_box)

        self.vertical_layout.addLayout(self.font_size_hl)

        self.output_font_size_hl = QtWidgets.QHBoxLayout()
        self.output_font_size_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )
        self.output_font_size_label.setText("Output Font Size")

        self.output_font_size_spin_box = QtWidgets.QSpinBox(
            self.scroll_area_widget_contents
        )

        self.output_font_size_spin_box.setValue(
            self.settings_value.output_font_size
        )

        self.output_font_size_hl.addWidget(self.output_font_size_label)
        self.output_font_size_hl.addWidget(self.output_font_size_spin_box)

        self.vertical_layout.addLayout(self.output_font_size_hl)

        # End First Row -> Font Size

        # Second Row -> App Theme

        self.app_theme_hl = QtWidgets.QHBoxLayout()
        self.app_theme_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )
        self.app_theme_label.setText("App Theme")

        self.app_theme_hl.addWidget(self.app_theme_label)

        self.app_theme_combo_box = QtWidgets.QComboBox(
            self.scroll_area_widget_contents
        )

        for k, v in APP_THEMES.items():
            self.app_theme_combo_box.addItem(v[0], k)

        self.app_theme_combo_box.setCurrentText(
            app_theme_to_str(self.settings_value.app_theme).capitalize()
        )

        self.app_theme_hl.addWidget(self.app_theme_combo_box)

        self.vertical_layout.addLayout(self.app_theme_hl)

        # End Second Row -> App Theme

        # Third Row -> Editor Theme

        self.editor_theme_hl = QtWidgets.QHBoxLayout()
        self.editor_theme_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )
        self.editor_theme_label.setText("Editor Theme")

        self.editor_theme_combo_box = QtWidgets.QComboBox(
            self.scroll_area_widget_contents
        )

        for item in EDITOR_THEMES:
            self.editor_theme_combo_box.addItem(item[1], item[0])

        self.editor_theme_combo_box.setCurrentText(
            self.settings_value.editor_theme.tname
        )

        self.editor_theme_hl.addWidget(self.editor_theme_label)
        self.editor_theme_hl.addWidget(self.editor_theme_combo_box)

        self.vertical_layout.addLayout(self.editor_theme_hl)

        # End Third Row -> Editor Theme

        # Fourth Row -> Language

        self.language_hl = QtWidgets.QHBoxLayout()
        self.language_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )

        self.language_label.setText("Language")
        self.language_hl.addWidget(self.language_label)
        self.language_combo_box = QtWidgets.QComboBox(
            self.scroll_area_widget_contents
        )

        for k, v in LANGUAGE_ITEMS.items():
            self.language_combo_box.addItem(v[0], k)

        self.language_hl.addWidget(self.language_combo_box)

        self.vertical_layout.addLayout(self.language_hl)

        # End Fourth Row -> Language

        # Fifth Row -> Pankti Interpreter Path

        self.pankti_path_hl = QtWidgets.QHBoxLayout()
        self.pankti_path_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )
        self.pankti_path_label.setText("Path to Pankti")

        self.pankti_path_hl.addWidget(self.pankti_path_label)

        self.pankti_path_line_edit = QtWidgets.QLineEdit(
            self.scroll_area_widget_contents
        )

        self.pankti_path_line_edit.setText(self.settings_value.pankti_path)

        self.pankti_path_hl.addWidget(
            self.pankti_path_line_edit, 0, QtGui.Qt.AlignmentFlag.AlignHCenter
        )

        self.pankti_path_tool_button = QtWidgets.QToolButton(
            self.scroll_area_widget_contents
        )
        self.pankti_path_tool_button.setText("Browse")

        self.pankti_path_hl.addWidget(self.pankti_path_tool_button)

        self.vertical_layout.addLayout(self.pankti_path_hl)
        self.pankti_path_tool_button.clicked.connect(
            self.open_select_pankti_exe
        )

        # End Fifth Row -> Pankti Interpreter Path

        # Sixth Row -> Autosave

        self.autosave_hl = QtWidgets.QHBoxLayout()
        self.autosave_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )
        self.autosave_label.setText("Autosave")

        self.autosave_hl.addWidget(self.autosave_label)

        self.autosave_check_box = QtWidgets.QCheckBox(
            self.scroll_area_widget_contents
        )
        self.autosave_check_box.setTristate(False)

        self.autosave_check_box.setChecked(self.settings_value.autosave)

        self.autosave_hl.addWidget(self.autosave_check_box)

        self.vertical_layout.addLayout(self.autosave_hl)

        # End Sixth Row -> Autosave

        self.scroll_area.setWidget(self.scroll_area_widget_contents)

        self.main_layout.addWidget(self.scroll_area)

        self.vertical_widget_2 = QtWidgets.QWidget(self)
        size_policy.setHeightForWidth(
            self.vertical_widget_2.sizePolicy().hasHeightForWidth()
        )
        self.vertical_widget_2.setSizePolicy(size_policy)
        self.vertical_widget_2.setMinimumSize(QtCore.QSize(525, 0))
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout(
            self.vertical_widget_2
        )
        self.save_button = QtWidgets.QPushButton(self.vertical_widget_2)
        size_policy.setHeightForWidth(
            self.save_button.sizePolicy().hasHeightForWidth()
        )
        self.save_button.setSizePolicy(size_policy)
        self.save_button.setText("Save")

        self.save_button.clicked.connect(self.clicked_save)

        self.horizontal_layout_5.addWidget(self.save_button)

        self.cancel_button = QtWidgets.QPushButton(self.vertical_widget_2)
        size_policy.setHeightForWidth(
            self.cancel_button.sizePolicy().hasHeightForWidth()
        )
        self.cancel_button.setSizePolicy(size_policy)
        self.cancel_button.setText("Cancel")

        self.cancel_button.clicked.connect(self.clicked_cancel)

        self.horizontal_layout_5.addWidget(self.cancel_button)
        self.main_layout.addWidget(
            self.vertical_widget_2,
            0,
            QtGui.Qt.AlignmentFlag.AlignRight
            | QtGui.Qt.AlignmentFlag.AlignBottom,
        )

        self.grid_layout.addLayout(self.main_layout, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(self)

    def open_select_pankti_exe(self, _) -> None:
        fname = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select Pankti Executable",
            "",
            filter="Any File (*.*);;Executable (*.exe)",
        )

        self.pankti_path_line_edit.setText(fname[0])

    def clicked_cancel(self, _) -> None:
        self.save = False
        self.done(0)

    def clicked_save(self, _) -> None:
        d = self.app_theme_combo_box.currentData()
        self.settings_value.app_theme = APP_THEMES[d][1]

        d = self.language_combo_box.currentData()
        self.settings_value.language = LANGUAGE_ITEMS[d][1]

        d = self.editor_theme_combo_box.currentData()
        self.settings_value.editor_theme = THEMES[d]

        self.settings_value.font_size = self.font_size_spin_box.value()
        self.settings_value.output_font_size = (
            self.output_font_size_spin_box.value()
        )

        self.settings_value.pankti_path = self.pankti_path_line_edit.text()

        self.settings_value.autosave = self.autosave_check_box.isChecked()
        self.save = True
        self.done(0)

    # setupUi

    # def retranslate_ui(self):
    #    self.setWindowTitle(
    #        QtCore.QCoreApplication.translate("Settings", "Settings", None)
    #    )
    #    self.settings_header_label.setText(
    #        QtCore.QCoreApplication.translate("Dialog", "Settings", None)
    #    )
    #    #self.label.setText(
    #    #    QtCore.QCoreApplication.translate("Dialog", "Font Size", None)
    #    #)
    #    self.label_3.setText(
    #        QtCore.QCoreApplication.translate("Dialog", "App Theme", None)
    #    )
    #    self.label_2.setText(
    #        QtCore.QCoreApplication.translate("Dialog", "Editor Theme", None)
    #    )
    #    self.label_4.setText(
    #        QtCore.QCoreApplication.translate("Dialog", "Pankti Path", None)
    #    )
    #    self.tool_button.setText(
    #        QtCore.QCoreApplication.translate("Dialog", "...", None)
    #    )
    #    self.label_5.setText(
    #        QtCore.QCoreApplication.translate("Dialog", "Autsave", None)
    #    )
    #    self.check_box.setText("")
    #    self.save_button.setText(
    #        QtCore.QCoreApplication.translate("Dialog", "Save", None)
    #    )
    #    self.cancel_button.setText(
    #        QtCore.QCoreApplication.translate("Dialog", "Cancel", None)
    #    )

    # retranslateUi
