# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\visualmodeelement_view.ui',
# licensing of '.\resources\visualmodeelement_view.ui' applies.
#
# Created: Wed Aug 12 18:59:48 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_visualModeElement(object):
    def setupUi(self, visualModeElement):
        visualModeElement.setObjectName("visualModeElement")
        visualModeElement.resize(325, 176)
        visualModeElement.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(visualModeElement)
        self.verticalLayout.setObjectName("verticalLayout")
        self.elementLabel = QtWidgets.QLabel(visualModeElement)
        self.elementLabel.setStyleSheet("font: 63 italic 8pt \"Segoe UI Semibold\";")
        self.elementLabel.setText("")
        self.elementLabel.setWordWrap(False)
        self.elementLabel.setMargin(0)
        self.elementLabel.setIndent(25)
        self.elementLabel.setObjectName("elementLabel")
        self.verticalLayout.addWidget(self.elementLabel)
        self.nameLabel = QtWidgets.QLabel(visualModeElement)
        self.nameLabel.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.nameLabel.setText("")
        self.nameLabel.setWordWrap(True)
        self.nameLabel.setObjectName("nameLabel")
        self.verticalLayout.addWidget(self.nameLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.editButton = QtWidgets.QPushButton(visualModeElement)
        self.editButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/elementIcons/edit_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.editButton.setIcon(icon)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(visualModeElement)
        self.deleteButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/elementIcons/delete_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon1)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(visualModeElement)
        QtCore.QMetaObject.connectSlotsByName(visualModeElement)

    def retranslateUi(self, visualModeElement):
        visualModeElement.setWindowTitle(QtWidgets.QApplication.translate("visualModeElement", "Form", None, -1))
        self.editButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Edit", None, -1))
        self.deleteButton.setToolTip(QtWidgets.QApplication.translate("visualModeElement", "Delete", None, -1))

import resources_rc
