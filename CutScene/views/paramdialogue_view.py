from PySide2.QtWidgets import QDialog, QLineEdit, QPlainTextEdit, QComboBox
from views.paramdialogue_view_ui import Ui_paramdialogue
from cutscene.utils import paramHelp

class ParamDialogue(QDialog):
    def __init__(self, parent, paramType):
        super().__init__()
        self._dialogue = Ui_paramdialogue()
        self._dialogue.setupUi(self)
        self._rows = []
        title, params = paramHelp[paramType]
        self._dialogue.label.setText(title)
        for param in params:
            row = DialogueRow(*param)
            self._rows.append(row)
            self._dialogue.formLayout.addRow(row.label, row.widget)

    @classmethod
    def getParams(self, parent, paramType):
        dialog = self(parent, paramType)
        result = dialog.exec_()
        if result:
            params = {}
            for row in dialog._rows:
                params[row.param_str] = row.get()
            return params
        else:
            return None

class DialogueRow(object):
    def __init__(self, param_str, label, input_type):
        self.param_str = param_str
        self.input_type = input_type
        self.label = label
        if input_type == "shortStr":
            self.widget = QLineEdit()
        elif input_type == "Str":
            self.widget = QPlainTextEdit()
        elif type(input_type) is list:
            self.widget = QComboBox(input_type)
        else:
            raise ValueError("Unsupported input type: {}".format(input_type))

    def get(self):
        if self.input_type == "Str":
            return self.widget.toPlainText()
        elif self.input_type == "shortStr":
            return self.widget.text()
        elif type(self.input_type) is list:
            return self.widget.currentText()

