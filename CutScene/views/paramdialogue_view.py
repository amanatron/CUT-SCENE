from PySide2.QtWidgets import QDialog, QLineEdit, QPlainTextEdit, QComboBox, QWidget, QLabel, QFileDialog, QVBoxLayout, QDialogButtonBox
from PySide2.QtGui import QPixmap, QResizeEvent
from PySide2.QtCore import Qt, QBuffer, QIODevice
from views.paramdialogue_view_ui import Ui_paramdialogue
from views.paintdialogue_view_ui import Ui_PaintDialog
from views.addimage_view_ui import Ui_addimage
from views.paintwindow_view import PaintWindow
from cutscene.utils import paramHelp
import base64

class ParamDialogue(QDialog):
    def __init__(self, parent, paramType, edit=False, defaults={}):
        super().__init__()
        self._dialogue = Ui_paramdialogue()
        self._dialogue.setupUi(self)
        self._rows = []
        title, editTitle, params = paramHelp[paramType]
        if edit:
            self._dialogue.label.setText(editTitle)
        else:
            self._dialogue.label.setText(title)
        for param in params:
            if param[0] in defaults.keys():
                default = defaults[param[0]]
            else:
                default = None
            row = DialogueRow(*param, default)
            self._rows.append(row)
            self._dialogue.formLayout.addRow(row.label, row.widget)

    @classmethod
    def getParams(self, parent, paramType, edit=False, defaults={}):
        dialog = self(parent, paramType, edit=edit, defaults=defaults)
        if dialog.exec_():
            params = {}
            for row in dialog._rows:
                params[row.param_str] = row.get()
            return params
        else:
            return None

class DialogueRow(QWidget):
    def __init__(self, param_str, label, input_type, default):
        super().__init__()
        self.param_str = param_str
        self.input_type = input_type
        self.label = label
        self.default = default
        if input_type == "shortStr":
            self.widget = QLineEdit()
        elif input_type == "Str":
            self.widget = QPlainTextEdit()
        elif type(input_type) is list:
            self.widget = QComboBox(input_type)
        elif "Img" in input_type:
            self.widget = AddImageWidget()
        else:
            raise ValueError("Unsupported input type: {}".format(input_type))
        if default:
            self.setDefault()

    def setDefault(self):
        if self.input_type == "Str":
            self.widget.setPlainText(self.default)
        elif self.input_type == "shortStr":
            self.widget.setText(self.default)
        elif type(self.input_type) is list:
            index = self.widget.findData(self.default)
            self.widget.setCurrentIndex(index)
        elif "Img" in self.input_type:
            decoded = base64.b64decode(self.default)
            self.widget.loadData(decoded)

    def get(self):
        if self.input_type == "Str":
            return self.widget.toPlainText()
        elif self.input_type == "shortStr":
            return self.widget.text()
        elif type(self.input_type) is list:
            return self.widget.currentText()
        elif "Img" in self.input_type:
            if not self.widget.pixmap: return None
            buff = QBuffer()
            buff.open(QIODevice.ReadWrite)
            self.widget.pixmap.save(buff, "PNG")
            data = buff.data().data()
            return base64.b64encode(data)

class AddImageWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._ui = Ui_addimage()
        self._ui.setupUi(self)
        self._ui.importButton.clicked.connect(self.openImage)
        self._ui.drawButton.clicked.connect(self.drawImage)

        self.pixmap = None
        self.imagePreview = ImageLabel()
        self._ui.verticalLayout.addWidget(self.imagePreview)

    def loadData(self, data):
        self.pixmap = QPixmap()
        self.pixmap.loadFromData(data)
        self.imagePreview.setPixmap(self.pixmap)

    def openImage(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "PNG image files (*.png); JPEG image files (*jpg); All files (*.*)")
        if path:
            self.pixmap = QPixmap()
            self.pixmap.load(path)
            self.imagePreview.setPixmap(self.pixmap)

    def drawImage(self):
        dialogue = PaintDialog()
        if dialogue.exec_():
            self.pixmap = QPixmap(dialogue.paint.canvas.pixmap())
            self.imagePreview.setPixmap(self.pixmap)

class PaintDialog(QDialog):
    def __init__(self):
        super().__init__()
        self._ui = Ui_PaintDialog()
        self._ui.setupUi(self)
        
        self.paint = PaintWindow()

        self._ui.paintLayout.addWidget(self.paint)

        # QBtn = QDialogButtonBox.Reset | QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        # self.buttonBox = QDialogButtonBox(QBtn)
        # self.buttonBox.accepted.connect(self.accept)
        # self.buttonBox.rejected.connect(self.reject)

        # self.resetButton.clicked.connect(self.canvas.reset)
        # self.okayButton.clicked.connect(self.okayButtonPressed)
        # self.cancelButton.clicked.connect(self.cancelButtonPressed)

class ImageLabel(QLabel):
    def __init__(self):
        super(ImageLabel, self).__init__()
        self.pixmap_width: int = 1
        self.pixmapHeight: int = 1
        self._pixmap = None

    def setPixmap(self, pixmap: QPixmap) -> None:
        self._pixmap = pixmap
        self.pixmap_width = self._pixmap.width()
        self.pixmapHeight = self._pixmap.height()

        self.updateMargins()
        super(ImageLabel, self).setPixmap(self._pixmap)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        self.updateMargins()
        super(ImageLabel, self).resizeEvent(a0)

    def updateMargins(self):
        if self._pixmap is None:
            return
        pixmap_scaled = self._pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        super(ImageLabel, self).setPixmap(pixmap_scaled)
        pixmapWidth = pixmap_scaled.width()
        pixmapHeight = pixmap_scaled.height()
        if pixmapWidth <= 0 or pixmapHeight <= 0:
            return
        w, h = self.width(), self.height()
        if w <= 0 or h <= 0:
            return

        if w * pixmapHeight > h * pixmapWidth:
            m = int((w - (pixmapWidth * h / pixmapHeight)) / 2)
            self.setContentsMargins(m, 0, m, 0)
        else:
            m = int((h - (pixmapHeight * w / pixmapWidth)) / 2)
            self.setContentsMargins(0, m, 0, m)