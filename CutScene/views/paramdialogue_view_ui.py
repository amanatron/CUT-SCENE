# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\resources\paramdialogue_view.ui',
# licensing of '.\resources\paramdialogue_view.ui' applies.
#
# Created: Tue Jul 28 11:50:27 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_paramdialogue(object):
    def setupUi(self, paramdialogue):
        paramdialogue.setObjectName("paramdialogue")
        paramdialogue.setWindowModality(QtCore.Qt.ApplicationModal)
        paramdialogue.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(paramdialogue)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(paramdialogue)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(paramdialogue)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(paramdialogue)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), paramdialogue.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), paramdialogue.reject)
        QtCore.QMetaObject.connectSlotsByName(paramdialogue)

    def retranslateUi(self, paramdialogue):
        paramdialogue.setWindowTitle(QtWidgets.QApplication.translate("paramdialogue", "Dialog", None, -1))

