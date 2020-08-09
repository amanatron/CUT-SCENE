from PySide2.QtWidgets import QWidget
from views.visualmodeelement_view_ui import Ui_visualModeElement

class VisualModeElement(QWidget):
    def __init__(self, sceneElement):
        super().__init__()
        self._ui = Ui_visualModeElement()
        self._ui.setupUi(self)
        self.sceneElement = sceneElement
        self._ui.elementLabel.setText(self.sceneElement.type)
        self._ui.nameLabel.setText(self.sceneElement.name)


