# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtGui, QtWidgets  # type: ignore


class PanktiSettingsDialog(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()

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

        self.font_size_hl.addWidget(self.font_size_label)
        self.font_size_hl.addWidget(self.font_size_spin_box)

        self.vertical_layout.addLayout(self.font_size_hl)

        # End First Row -> Font Size

        # Second Row -> App Theme

        self.app_theme_hl = QtWidgets.QHBoxLayout()
        self.app_theme_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )
        self.app_theme_label.setText("App Theme")

        self.app_theme_hl.addWidget(self.app_theme_label)

        self.app_theme_combox_box = QtWidgets.QComboBox(
            self.scroll_area_widget_contents
        )

        self.app_theme_hl.addWidget(self.app_theme_combox_box)

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

        self.editor_theme_hl.addWidget(self.editor_theme_label)
        self.editor_theme_hl.addWidget(self.editor_theme_combo_box)

        self.vertical_layout.addLayout(self.editor_theme_hl)

        # End Third Row -> Editor Theme

        # Fourth Row -> Pankti Interpreter Path

        self.pankti_path_hl = QtWidgets.QHBoxLayout()
        self.pankti_path_label = QtWidgets.QLabel(
            self.scroll_area_widget_contents
        )
        self.pankti_path_label.setText("Path to Pankti")

        self.pankti_path_hl.addWidget(self.pankti_path_label)

        self.pankti_path_line_edit = QtWidgets.QLineEdit(
            self.scroll_area_widget_contents
        )

        self.pankti_path_hl.addWidget(
            self.pankti_path_line_edit, 0, QtGui.Qt.AlignmentFlag.AlignHCenter
        )

        self.pankti_path_tool_button = QtWidgets.QToolButton(
            self.scroll_area_widget_contents
        )
        self.pankti_path_tool_button.setText("Browse")

        self.pankti_path_hl.addWidget(self.pankti_path_tool_button)

        self.vertical_layout.addLayout(self.pankti_path_hl)

        # End Fourth Row -> Pankti Interpreter Path

        # Fifth Row -> Autosave

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

        self.autosave_hl.addWidget(self.autosave_check_box)

        self.vertical_layout.addLayout(self.autosave_hl)

        # End Fifth Row -> Autosave

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

        self.horizontal_layout_5.addWidget(self.save_button)

        self.cancel_button = QtWidgets.QPushButton(self.vertical_widget_2)
        size_policy.setHeightForWidth(
            self.cancel_button.sizePolicy().hasHeightForWidth()
        )
        self.cancel_button.setSizePolicy(size_policy)
        self.cancel_button.setText("Cancel")

        self.horizontal_layout_5.addWidget(self.cancel_button)
        self.main_layout.addWidget(
            self.vertical_widget_2,
            0,
            QtGui.Qt.AlignmentFlag.AlignRight
            | QtGui.Qt.AlignmentFlag.AlignBottom,
        )

        self.grid_layout.addLayout(self.main_layout, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(self)

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
