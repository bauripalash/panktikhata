# -*- coding: utf-8 -*-
from PySide6 import QtCore, QtGui, QtWidgets # type: ignore
from PySide6.QtGui import QAction, QIcon # type: ignore
from PySide6.QtWidgets import QStyle, QStyleOption # type: ignore

from ui.highlighter import PanktiSyntaxHighlighter
from themes import defaultLight
from ui.settingsdlg import PanktiSettingsDialog
from assets import resources


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self) -> None:
        if not self.objectName():
            self.setObjectName(u"MainWindow")

        self.setStyleSheet(defaultLight.themeDefaultLight)

        self.resize(800, 600)
        self.rootWidget = QtWidgets.QWidget()
        self.rootWidget.setObjectName(u"rootWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.rootWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.mainBox = QtWidgets.QHBoxLayout()
        self.mainBox.setObjectName(u"mainBox")
        self.EditorBox = QtWidgets.QHBoxLayout()
        self.EditorBox.setObjectName(u"EditorBox")
        self.ButtonFrame = QtWidgets.QFrame(self.rootWidget)
        self.ButtonFrame.setObjectName(u"ButtonFrame")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonFrame.sizePolicy().hasHeightForWidth())
        self.ButtonFrame.setSizePolicy(sizePolicy)
        
        
        self.ButtonFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ButtonFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)#QFrame.Raised)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ButtonFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ButtonBox = QtWidgets.QVBoxLayout()
        self.ButtonBox.setObjectName(u"ButtonBox")
        

        self.runPm = QStyle.StandardPixmap.SP_MediaPlay
        self.runIcon = self.style().standardIcon(self.runPm)
        self.RunButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.RunButton.setObjectName(u"RunButton")

        self.RunButton.setIcon(self.runIcon)

        self.RunButton.clicked.connect(self.btnClick)


        self.ButtonBox.addWidget(self.RunButton, 0, QtGui.Qt.AlignmentFlag.AlignTop)
        

        self.verticalLayout_2.addLayout(self.ButtonBox)


        self.EditorBox.addWidget(self.ButtonFrame, 0, QtGui.Qt.AlignmentFlag.AlignTop)

        self.EditorSplitter = QtWidgets.QSplitter(self.rootWidget)
        self.EditorSplitter.setObjectName(u"EditorSplitter")
        self.EditorSplitter.setOrientation(QtGui.Qt.Orientation.Vertical)
        self.InputEdit = QtWidgets.QPlainTextEdit(self.EditorSplitter)
        
        self.highligher = PanktiSyntaxHighlighter(self.InputEdit.document())

        self.InputEdit.setObjectName(u"InputEdit")
        self.EditorSplitter.addWidget(self.InputEdit)

        self.OutputEdit = QtWidgets.QPlainTextEdit(self.EditorSplitter)
        self.OutputEdit.setObjectName(u"OutputEdit")
        self.EditorSplitter.addWidget(self.OutputEdit)

        self.EditorBox.addWidget(self.EditorSplitter)


        self.mainBox.addLayout(self.EditorBox)


        self.horizontalLayout_3.addLayout(self.mainBox)

        self.setCentralWidget(self.rootWidget)
        self.menubar = QtWidgets.QMenuBar()
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        self.setupMenu()

        

        QtCore.QMetaObject.connectSlotsByName(self)

    def setupMenu(self):
        self.newMenuAction = QAction(QIcon(":/icons/description.svg"), "&New", self)
        self.openMenuAction = QAction(QIcon(":/icons/folder_open.svg"), "&Open", self)
        self.saveMenuAction = QAction(QIcon(":/icons/save.svg"), "&Save", self)
        self.quitMenuAction = QAction(QIcon(":/icons/power_settings_new.svg"), "&Quit", self)


        self.fileMenu = self.menubar.addMenu("&File")
        self.fileMenu.addAction(self.newMenuAction)
        self.fileMenu.addAction(self.openMenuAction)
        self.fileMenu.addAction(self.saveMenuAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitMenuAction)


        self.undoMenuAction = QAction()
        self.redoMenuAction = QAction()
        self.cutMenuAction  = QAction()
        self.copyMenuAction = QAction()
        self.pasteMenuAction = QAction()
        self.selectAllMenuAction = QAction()

        self.findMenuAction = QAction()
        self.findAndReplaceMenuAction = QAction()




        self.setMenuBar(self.menubar)
        

    def btnClick(self, s):
        dlg = PanktiSettingsDialog()
        dlg.exec()

    def retranslateUi(self):
        self.setWindowTitle(QtCore.QCoreApplication.translate("MainWindow", u"Pankti Khata", None))
        #self.RunButton.setText(QtCore.QCoreApplication.translate("MainWindow", u"Run", None))



