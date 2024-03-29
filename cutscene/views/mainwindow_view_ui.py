# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\mainwindow_view.ui',
# licensing of '.\resources\mainwindow_view.ui' applies.
#
# Created: Mon Aug 17 10:54:37 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1432, 934)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(300, 0))
        self.widget.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget.setStyleSheet("background-color: rgb(35, 47, 52);\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Segoe UI\";\n"
"margin-left: 5px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.levelsView = QtWidgets.QTreeView(self.widget)
        self.levelsView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.levelsView.setStyleSheet("QTreeView {\n"
"    show-decoration-selected: 1;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 25 12pt \"Segoe UI Light\";\n"
"    outline: none;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    border-radius: 2px;\n"
"    border: 0px;\n"
"    margin-top: 3px;\n"
"    margin-bottom: 3px;\n"
"    padding: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTreeView::item:hover {\n"
"    background: rgb(40, 57, 66)\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    background: rgb(52, 73, 85);\n"
"}")
        self.levelsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.levelsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.levelsView.setLineWidth(1)
        self.levelsView.setAutoScrollMargin(16)
        self.levelsView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.levelsView.setProperty("showDropIndicator", False)
        self.levelsView.setDragEnabled(True)
        self.levelsView.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.levelsView.setIndentation(25)
        self.levelsView.setAnimated(True)
        self.levelsView.setExpandsOnDoubleClick(False)
        self.levelsView.setObjectName("levelsView")
        self.levelsView.header().setVisible(False)
        self.verticalLayout.addWidget(self.levelsView)
        self.buttonCreateProject = QtWidgets.QPushButton(self.widget)
        self.buttonCreateProject.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 9pt \"Segoe UI\";\n"
"background-color: rgb(40, 57, 66);\n"
"padding: 5px;\n"
"border-radius: 3px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(52, 73, 85);\n"
"padding: 5px;\n"
"border-radius: 3px\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/levelIcons/img/icons/levelIcons/create_white_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCreateProject.setIcon(icon)
        self.buttonCreateProject.setIconSize(QtCore.QSize(30, 30))
        self.buttonCreateProject.setAutoDefault(False)
        self.buttonCreateProject.setFlat(False)
        self.buttonCreateProject.setObjectName("buttonCreateProject")
        self.verticalLayout.addWidget(self.buttonCreateProject)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(40, 57, 66);\n"
"padding: 5px;\n"
"border-radius: 3px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(52, 73, 85);\n"
"padding: 5px;\n"
"border-radius: 3px\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonAddLevel = QtWidgets.QPushButton(self.widget_2)
        self.buttonAddLevel.setStyleSheet("")
        self.buttonAddLevel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/levelIcons/img/icons/levelIcons/add_box_white_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/levelIcons/img/icons/levelIcons/add_box_grey_96x96.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.buttonAddLevel.setIcon(icon1)
        self.buttonAddLevel.setIconSize(QtCore.QSize(30, 30))
        self.buttonAddLevel.setObjectName("buttonAddLevel")
        self.horizontalLayout.addWidget(self.buttonAddLevel)
        self.buttonAddSubLevel = QtWidgets.QPushButton(self.widget_2)
        self.buttonAddSubLevel.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/levelIcons/img/icons/levelIcons/library_add_white_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/levelIcons/img/icons/levelIcons/library_add_grey_96x96.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.buttonAddSubLevel.setIcon(icon2)
        self.buttonAddSubLevel.setIconSize(QtCore.QSize(30, 30))
        self.buttonAddSubLevel.setObjectName("buttonAddSubLevel")
        self.horizontalLayout.addWidget(self.buttonAddSubLevel)
        self.buttonAddScene = QtWidgets.QPushButton(self.widget_2)
        self.buttonAddScene.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/levelIcons/img/icons/levelIcons/videogame_asset_white_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/levelIcons/img/icons/levelIcons/videogame_asset_grey_96x96.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        self.buttonAddScene.setIcon(icon3)
        self.buttonAddScene.setIconSize(QtCore.QSize(30, 30))
        self.buttonAddScene.setObjectName("buttonAddScene")
        self.horizontalLayout.addWidget(self.buttonAddScene)
        self.verticalLayout.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.widget, 3, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(0, 0, 801, 40))
        self.widget_4.setStyleSheet("QPushButton {\n"
"background-color: rgb(238, 238, 238);\n"
"padding: 5px;\n"
"border-radius: 3px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 200, 200);\n"
"padding: 5px;\n"
"border-radius: 3px\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"background-color: rgb(200, 200, 200);\n"
"padding: 5px;\n"
"border-radius: 3px\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sceneToolsLabel = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sceneToolsLabel.sizePolicy().hasHeightForWidth())
        self.sceneToolsLabel.setSizePolicy(sizePolicy)
        self.sceneToolsLabel.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.sceneToolsLabel.setMargin(1)
        self.sceneToolsLabel.setIndent(10)
        self.sceneToolsLabel.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.sceneToolsLabel.setObjectName("sceneToolsLabel")
        self.horizontalLayout_2.addWidget(self.sceneToolsLabel)
        self.buttonAddObjective = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddObjective.sizePolicy().hasHeightForWidth())
        self.buttonAddObjective.setSizePolicy(sizePolicy)
        self.buttonAddObjective.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/explore_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAddObjective.setIcon(icon4)
        self.buttonAddObjective.setIconSize(QtCore.QSize(30, 30))
        self.buttonAddObjective.setObjectName("buttonAddObjective")
        self.horizontalLayout_2.addWidget(self.buttonAddObjective)
        self.buttonAddAnimation = QtWidgets.QPushButton(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddAnimation.sizePolicy().hasHeightForWidth())
        self.buttonAddAnimation.setSizePolicy(sizePolicy)
        self.buttonAddAnimation.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/forum_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAddAnimation.setIcon(icon5)
        self.buttonAddAnimation.setIconSize(QtCore.QSize(30, 30))
        self.buttonAddAnimation.setCheckable(False)
        self.buttonAddAnimation.setObjectName("buttonAddAnimation")
        self.horizontalLayout_2.addWidget(self.buttonAddAnimation)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonManipulate = QtWidgets.QPushButton(self.widget_4)
        self.buttonManipulate.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/pan_tool_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonManipulate.setIcon(icon6)
        self.buttonManipulate.setIconSize(QtCore.QSize(30, 30))
        self.buttonManipulate.setCheckable(True)
        self.buttonManipulate.setObjectName("buttonManipulate")
        self.horizontalLayout_2.addWidget(self.buttonManipulate)
        self.buttonConnect = QtWidgets.QPushButton(self.widget_4)
        self.buttonConnect.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/timeline_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonConnect.setIcon(icon7)
        self.buttonConnect.setIconSize(QtCore.QSize(30, 30))
        self.buttonConnect.setCheckable(True)
        self.buttonConnect.setChecked(False)
        self.buttonConnect.setObjectName("buttonConnect")
        self.horizontalLayout_2.addWidget(self.buttonConnect)
        self.buttonDelete = QtWidgets.QPushButton(self.widget_4)
        self.buttonDelete.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/remove_circle_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonDelete.setIcon(icon8)
        self.buttonDelete.setIconSize(QtCore.QSize(30, 30))
        self.buttonDelete.setCheckable(True)
        self.buttonDelete.setObjectName("buttonDelete")
        self.horizontalLayout_2.addWidget(self.buttonDelete)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.widget_3, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1432, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
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
        self.menuFile.addAction(self.actionSaveAs)
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
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Project Explorer", None, -1))
        self.buttonCreateProject.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Create Project", None, -1))
        self.buttonCreateProject.setText(QtWidgets.QApplication.translate("MainWindow", "Create Project", None, -1))
        self.buttonAddLevel.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add Level", None, -1))
        self.buttonAddSubLevel.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add SubLevel", None, -1))
        self.buttonAddScene.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add Scene", None, -1))
        self.sceneToolsLabel.setText(QtWidgets.QApplication.translate("MainWindow", "Scene Tools", None, -1))
        self.buttonAddObjective.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add Objective", None, -1))
        self.buttonAddAnimation.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Add Animation", None, -1))
        self.buttonManipulate.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Move Item", None, -1))
        self.buttonConnect.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Connect Items", None, -1))
        self.buttonDelete.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Remove Connection", None, -1))
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
        self.actionSaveAs.setText(QtWidgets.QApplication.translate("MainWindow", "Save As", None, -1))
        self.actionSaveAs.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Save a copy of this project", None, -1))
        self.actionSaveAs.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, -1))
        self.actionExit.setText(QtWidgets.QApplication.translate("MainWindow", "Exit", None, -1))
        self.actionExit.setToolTip(QtWidgets.QApplication.translate("MainWindow", "Exit CutScene", None, -1))
        self.actionExit.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Q", None, -1))
        self.actionUndo.setText(QtWidgets.QApplication.translate("MainWindow", "Undo", None, -1))
        self.actionUndo.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Z", None, -1))
        self.actionRedo.setText(QtWidgets.QApplication.translate("MainWindow", "Redo", None, -1))
        self.actionRedo.setShortcut(QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+Z", None, -1))

import resources_rc
