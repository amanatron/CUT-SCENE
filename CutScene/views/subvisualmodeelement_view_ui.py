# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\subvisualmodeelement_view.ui',
# licensing of '.\resources\subvisualmodeelement_view.ui' applies.
#
# Created: Mon Aug 17 10:24:46 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_subVisualModeElement(object):
    def setupUi(self, subVisualModeElement):
        subVisualModeElement.setObjectName("subVisualModeElement")
        subVisualModeElement.resize(178, 30)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(subVisualModeElement.sizePolicy().hasHeightForWidth())
        subVisualModeElement.setSizePolicy(sizePolicy)
        subVisualModeElement.setMinimumSize(QtCore.QSize(0, 30))
        subVisualModeElement.setStyleSheet("QLabel {\n"
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(subVisualModeElement)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.elementLabel = QtWidgets.QLabel(subVisualModeElement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elementLabel.sizePolicy().hasHeightForWidth())
        self.elementLabel.setSizePolicy(sizePolicy)
        self.elementLabel.setStyleSheet("font: 63 italic 8pt \"Segoe UI Semibold\";")
        self.elementLabel.setText("")
        self.elementLabel.setWordWrap(False)
        self.elementLabel.setMargin(0)
        self.elementLabel.setIndent(25)
        self.elementLabel.setObjectName("elementLabel")
        self.horizontalLayout.addWidget(self.elementLabel)
        self.editButton = QtWidgets.QPushButton(subVisualModeElement)
        self.editButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/elementIcons/edit_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(subVisualModeElement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteButton.sizePolicy().hasHeightForWidth())
        self.deleteButton.setSizePolicy(sizePolicy)
        self.deleteButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/elementIcons/delete_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)

        self.retranslateUi(subVisualModeElement)
        QtCore.QMetaObject.connectSlotsByName(subVisualModeElement)

    def retranslateUi(self, subVisualModeElement):
        subVisualModeElement.setWindowTitle(QtWidgets.QApplication.translate("subVisualModeElement", "Form", None, -1))
        self.editButton.setToolTip(QtWidgets.QApplication.translate("subVisualModeElement", "Edit", None, -1))
        self.deleteButton.setToolTip(QtWidgets.QApplication.translate("subVisualModeElement", "Delete", None, -1))

import resources_rc
