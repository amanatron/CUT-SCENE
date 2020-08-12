# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\addimage_view.ui',
# licensing of '.\resources\addimage_view.ui' applies.
#
# Created: Wed Aug 12 16:46:23 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_addimage(object):
    def setupUi(self, addimage):
        addimage.setObjectName("addimage")
        addimage.resize(635, 171)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(addimage.sizePolicy().hasHeightForWidth())
        addimage.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(addimage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.importButton = QtWidgets.QPushButton(addimage)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/visualModeIcons/vertical_align_bottom_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importButton.setIcon(icon)
        self.importButton.setObjectName("importButton")
        self.horizontalLayout.addWidget(self.importButton)
        self.drawButton = QtWidgets.QPushButton(addimage)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/visualModeIcons/img/icons/elementIcons/edit_black_96x96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.drawButton.setIcon(icon1)
        self.drawButton.setObjectName("drawButton")
        self.horizontalLayout.addWidget(self.drawButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(addimage)
        QtCore.QMetaObject.connectSlotsByName(addimage)

    def retranslateUi(self, addimage):
        addimage.setWindowTitle(QtWidgets.QApplication.translate("addimage", "Form", None, -1))
        self.importButton.setText(QtWidgets.QApplication.translate("addimage", "Import Image", None, -1))
        self.drawButton.setText(QtWidgets.QApplication.translate("addimage", "Draw Image", None, -1))

import resources_rc
