# -*- coding: utf-8 -*-

from PySide6 import QtCore, QtGui, QtWidgets # type: ignore


class PanktiSettingsDialog(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()

        self.setupUi()

    def setupUi(self) -> None:

        if not self.objectName():
            self.setObjectName(u"Dialog")

        self.resize(539, 447)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.settingsHeaderLabel = QtWidgets.QLabel(self)
        self.settingsHeaderLabel.setObjectName(u"settingsHeaderLabel")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsHeaderLabel.sizePolicy().hasHeightForWidth())
        self.settingsHeaderLabel.setSizePolicy(sizePolicy)
        self.settingsHeaderLabel.setAlignment(QtGui.Qt.AlignmentFlag.AlignHCenter)

        self.mainLayout.addWidget(self.settingsHeaderLabel, 0, QtGui.Qt.AlignmentFlag.AlignHCenter)

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 521, 347))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.spinBox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout_4.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.horizontalLayout_9.addWidget(self.comboBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_7.addWidget(self.comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_10.addWidget(self.lineEdit, 0, QtGui.Qt.AlignmentFlag.AlignHCenter)

        self.toolButton = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_10.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setTristate(False)

        self.horizontalLayout_11.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.mainLayout.addWidget(self.scrollArea)

        self.verticalWidget_2 = QtWidgets.QWidget(self)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setMinimumSize(QtCore.QSize(525, 0))
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.verticalWidget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.saveButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.saveButton)

        self.cancelButton = QtWidgets.QPushButton(self.verticalWidget_2)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.cancelButton)


        self.mainLayout.addWidget(self.verticalWidget_2, 0, QtGui.Qt.AlignmentFlag.AlignRight|QtGui.Qt.AlignmentFlag.AlignBottom)


        self.gridLayout.addLayout(self.mainLayout, 0, 0, 1, 1)

        QtWidgets.QWidget.setTabOrder(self.scrollArea, self.spinBox)
        QtWidgets.QWidget.setTabOrder(self.spinBox, self.comboBox_2)
        QtWidgets.QWidget.setTabOrder(self.comboBox_2, self.comboBox)
        QtWidgets.QWidget.setTabOrder(self.comboBox, self.lineEdit)
        QtWidgets.QWidget.setTabOrder(self.lineEdit, self.toolButton)
        QtWidgets.QWidget.setTabOrder(self.toolButton, self.checkBox)
        QtWidgets.QWidget.setTabOrder(self.checkBox, self.saveButton)
        QtWidgets.QWidget.setTabOrder(self.saveButton, self.cancelButton)

        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate("Settings", u"Settings", None))
        self.settingsHeaderLabel.setText(QtCore.QCoreApplication.translate("Dialog", u"Settings", None))
        self.label.setText(QtCore.QCoreApplication.translate("Dialog", u"Font Size", None))
        self.label_3.setText(QtCore.QCoreApplication.translate("Dialog", u"App Theme", None))
        self.label_2.setText(QtCore.QCoreApplication.translate("Dialog", u"Editor Theme", None))
        self.label_4.setText(QtCore.QCoreApplication.translate("Dialog", u"Pankti Path", None))
        self.toolButton.setText(QtCore.QCoreApplication.translate("Dialog", u"...", None))
        self.label_5.setText(QtCore.QCoreApplication.translate("Dialog", u"Autsave", None))
        self.checkBox.setText("")
        self.saveButton.setText(QtCore.QCoreApplication.translate("Dialog", u"Save", None))
        self.cancelButton.setText(QtCore.QCoreApplication.translate("Dialog", u"Cancel", None))
    # retranslateUi

