# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\visualmodeelement_view.ui',
# licensing of '.\resources\visualmodeelement_view.ui' applies.
#
# Created: Mon Aug 17 10:54:37 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_visualModeElement(object):
    def setupUi(self, visualModeElement):
        visualModeElement.setObjectName("visualModeElement")
        visualModeElement.resize(474, 133)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(visualModeElement.sizePolicy().hasHeightForWidth())
        visualModeElement.setSizePolicy(sizePolicy)
        visualModeElement.setMinimumSize(QtCore.QSize(0, 0))
        visualModeElement.setStyleSheet("QWidget#visualModeElement {\n"
"border: 1px solid rgb(213, 213, 213);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255) }\n"
"\n"
"QWidget#visualModeElement:hover {\n"
"border: 2px solid rgb(213, 213, 213);\n"
"}\n"
"\n"
"QLabel {\n"
"background-color: rgb(255, 255, 255)}\n"
"\n"
"QPushButton {\n"
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
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(visualModeElement)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.elementLabel = QtWidgets.QLabel(visualModeElement)
        self.elementLabel.setMinimumSize(QtCore.QSize(0, 17))
        self.elementLabel.setStyleSheet("font: 63 italic 8pt \"Segoe UI Semibold\";")
        self.elementLabel.setText("")
        self.elementLabel.setWordWrap(False)
        self.elementLabel.setMargin(0)
        self.elementLabel.setIndent(25)
        self.elementLabel.setObjectName("elementLabel")
        self.verticalLayout.addWidget(self.elementLabel)
        self.nameLabel = QtWidgets.QLabel(visualModeElement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setMinimumSize(QtCore.QSize(0, 31))
        self.nameLabel.setSizeIncrement(QtCore.QSize(0, 0))
        self.nameLabel.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.nameLabel.setText("")
        self.nameLabel.setWordWrap(True)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        self.subElementsWidget = QtWidgets.QWidget(visualModeElement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.subElementsWidget.sizePolicy().hasHeightForWidth())
        self.subElementsWidget.setSizePolicy(sizePolicy)
        self.subElementsWidget.setObjectName("subElementsWidget")
        self.subElementsLayout = QtWidgets.QVBoxLayout(self.subElementsWidget)
        self.subElementsLayout.setContentsMargins(0, 0, 0, 0)
        self.subElementsLayout.setObjectName("subElementsLayout")
        self.verticalLayout.addWidget(self.subElementsWidget)
        self.line = QtWidgets.QFrame(visualModeElement)
        self.line.setMinimumSize(QtCore.QSize(0, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.controlButton = QtWidgets.QPushButton(visualModeElement)
        self.controlButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/keyboard_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.controlButton.setIcon(icon)
        self.controlButton.setObjectName("controlButton")
        self.horizontalLayout.addWidget(self.controlButton)
        self.actionButton = QtWidgets.QPushButton(visualModeElement)
        self.actionButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/comment_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionButton.setIcon(icon1)
        self.actionButton.setObjectName("actionButton")
        self.horizontalLayout.addWidget(self.actionButton)
        self.pseudocodeButton = QtWidgets.QPushButton(visualModeElement)
        self.pseudocodeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/code_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pseudocodeButton.setIcon(icon2)
        self.pseudocodeButton.setObjectName("pseudocodeButton")
        self.horizontalLayout.addWidget(self.pseudocodeButton)
        self.physicsButton = QtWidgets.QPushButton(visualModeElement)
        self.physicsButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/vertical_align_bottom_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.physicsButton.setIcon(icon3)
        self.physicsButton.setObjectName("physicsButton")
        self.horizontalLayout.addWidget(self.physicsButton)
        self.headingButton = QtWidgets.QPushButton(visualModeElement)
        self.headingButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/title_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.headingButton.setIcon(icon4)
        self.headingButton.setObjectName("headingButton")
        self.horizontalLayout.addWidget(self.headingButton)
        self.dialogueButton = QtWidgets.QPushButton(visualModeElement)
        self.dialogueButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/record_voice_over_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dialogueButton.setIcon(icon5)
        self.dialogueButton.setObjectName("dialogueButton")
        self.horizontalLayout.addWidget(self.dialogueButton)
        self.actButton = QtWidgets.QPushButton(visualModeElement)
        self.actButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/movie_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actButton.setIcon(icon6)
        self.actButton.setObjectName("actButton")
        self.horizontalLayout.addWidget(self.actButton)
        self.transitionButton = QtWidgets.QPushButton(visualModeElement)
        self.transitionButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/swap_horiz_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.transitionButton.setIcon(icon7)
        self.transitionButton.setObjectName("transitionButton")
        self.horizontalLayout.addWidget(self.transitionButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.editButton = QtWidgets.QPushButton(visualModeElement)
        self.editButton.setMinimumSize(QtCore.QSize(0, 0))
        self.editButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/elementIcons/edit_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon8)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(visualModeElement)
        self.deleteButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/elementIcons/delete_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon9)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(visualModeElement)
        QtCore.QMetaObject.connectSlotsByName(visualModeElement)

    def retranslateUi(self, visualModeElement):
        visualModeElement.setWindowTitle(QtWidgets.QApplication.translate("visualModeElement", "Form", None, -1))
        self.controlButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Add Controls", None, -1))
        self.actionButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Add Action/Description", None, -1))
        self.pseudocodeButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Add Pseudocode", None, -1))
        self.physicsButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Add Physics", None, -1))
        self.headingButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Add Heading", None, -1))
        self.dialogueButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Add Dialog", None, -1))
        self.actButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Add Act", None, -1))
        self.transitionButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Add Transition", None, -1))
        self.editButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Edit", None, -1))
        self.deleteButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Delete", None, -1))

import resources_rc
