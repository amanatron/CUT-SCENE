# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\mainwindow_view.ui',
# licensing of '.\resources\mainwindow_view.ui' applies.
#
# Created: Tue Jul 21 13:43:35 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 564)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout.addWidget(self.listView)
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout.addWidget(self.listView_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 786, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "CutScene", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("MainWindow", "File", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("MainWindow", "Edit", None, -1))
        self.actionNew.setText(QtWidgets.QApplication.translate("MainWindow", "New", None, -1))
        self.actionNew.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Create a new project", None, -1))
        self.actionNew.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+N", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "Open", None, -1))
        self.actionOpen.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Open an existing project", None, -1))
        self.actionOpen.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionSave.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionSave.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Save this project", None, -1))
        self.actionSave.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionSave_As.setText(QtWidgets.QApplication.translate("MainWindow", "Save As", None, -1))
        self.actionSave_As.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Save a copy of this project", None, -1))
        self.actionSave_As.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionExit.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Exit CutScene", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionUndo.setText(QtWidgets.QApplication.translate("MainWindow", "Undo", None, -1))
        self.actionUndo.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Z", None, -1))
        self.actionRedo.setText(QtWidgets.QApplication.translate("MainWindow", "Redo", None, -1))
        self.actionRedo.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, -1))

