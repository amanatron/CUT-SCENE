from PySide2.QtWidgets import QWidget, QFrame
from views.visualmodeelement_view_ui import Ui_visualModeElement
from views.paramdialogue_view import ParamDialogue

class VisualModeElement(QFrame):
    def __init__(self, parent, scene_element=None, edit_callback=None, delete_callback=None):
        super().__init__(parent)
        self._ui = Ui_visualModeElement()
        self._ui.setupUi(self)
        self.scene_element = scene_element
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback

        # connect buttons
        self._ui.editButton.clicked.connect(self.editElement)
        self._ui.deleteButton.clicked.connect(self.delete)

        # update labels
        self.updateLabels()


    def updateLabels(self):
        if self.scene_element:
            self._ui.elementLabel.setText(self.scene_element.type)
            self._ui.nameLabel.setText(self.scene_element.name)

    def delete(self):
        if self.delete_callback:
            self.delete_callback(self.scene_element.itemID)

    def editElement(self):
        params = ParamDialogue.getParams(self, self.scene_element.type, edit=True, defaults=self.scene_element.dict())
        if not params:
            return
        self.scene_element.edit(params)
        self.updateLabels()
    # def enterEvent(self, e):
    #     print(f"mouse over {self}")
    #     style = self.styleSheet()
    #     print(style)
    #     self.setStyleSheet("QFrame {border-width 3px}")

    # def leaveEvent(self, e):
    #     print(f"mouse left {self}")
    #     self.setStyleSheet("QFrame {border-width 1px}")