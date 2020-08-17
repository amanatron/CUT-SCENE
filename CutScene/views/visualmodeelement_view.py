from PySide2.QtWidgets import QWidget, QFrame
from PySide2.QtCore import QSize
from views.visualmodeelement_view_ui import Ui_visualModeElement
from views.subvisualmodeelement_view_ui import Ui_subVisualModeElement
from views.paramdialogue_view import ParamDialogue

class VisualModeElement(QFrame):
    def __init__(self, parent, scene_element=None, edit_callback=None, delete_callback=None, new_item_callbacks={}):
        super().__init__(parent)
        self._ui = Ui_visualModeElement()
        self._ui.setupUi(self)
        self.scene_element = scene_element
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback
        self.new_item_callbacks = new_item_callbacks
        self.parent=parent

        # connect buttons
        self._ui.editButton.clicked.connect(self.editElement)
        self._ui.deleteButton.clicked.connect(self.delete)

        # wrote a lot of this out manually, tbh dont see why not, its robust and works
        self._ui.transitionButton.clicked.connect(self.addTransition)
        self._ui.headingButton.clicked.connect(self.addHeading)
        self._ui.dialogueButton.clicked.connect(self.addDialogue)
        self._ui.actButton.clicked.connect(self.addAct)
        self._ui.controlButton.clicked.connect(self.addControl)
        self._ui.pseudocodeButton.clicked.connect(self.addPseudocode)
        self._ui.physicsButton.clicked.connect(self.addPhysics)
        self._ui.actionButton.clicked.connect(self.addAction)

        # update labels
        self.updateLabels()

        # set button visibility
        if self.scene_element.type == "OBJECTIVE":
            self._ui.transitionButton.setVisible(False)
            self._ui.headingButton.setVisible(False)
            self._ui.dialogueButton.setVisible(False)
            self._ui.actButton.setVisible(False)
        elif self.scene_element.type == "ANIMATION":
            self._ui.controlButton.setVisible(False)
            self._ui.pseudocodeButton.setVisible(False)
            self._ui.physicsButton.setVisible(False)
        else:
            self._ui.transitionButton.setVisible(False)
            self._ui.headingButton.setVisible(False)
            self._ui.dialogueButton.setVisible(False)
            self._ui.actButton.setVisible(False)
            self._ui.controlButton.setVisible(False)
            self._ui.pseudocodeButton.setVisible(False)
            self._ui.physicsButton.setVisible(False)
            self._ui.actionButton.setVisible(False)

        self.defaultSize = (self.geometry().size().width(), self.geometry().size().height())

    def sizeHint(self):
        width, height = self.defaultSize
        n = self._ui.subElementsLayout.count()
        height += 7
        height += 37*n
        return QSize(width, height)

    def addSubElement(self, element):
        widget = SubElement(element, 
                            delete_callback=self.delete_callback,
                            edit_callback=self.edit_callback)
        self._ui.subElementsLayout.addWidget(widget)

    def addTransition(self):
        self.new_item_callbacks["TRANSITION"](self.scene_element.itemID)

    def addHeading(self):
        self.new_item_callbacks["HEADING"](self.scene_element.itemID)

    def addDialogue(self):
        self.new_item_callbacks["DIALOGUE"](self.scene_element.itemID)

    def addAct(self):
        self.new_item_callbacks["ACT"](self.scene_element.itemID)
    
    def addControl(self):
        self.new_item_callbacks["CONTROL"](self.scene_element.itemID)

    def addPseudocode(self):
        self.new_item_callbacks["PSEUDOCODE"](self.scene_element.itemID)
    
    def addPhysics(self):
        self.new_item_callbacks["PHYSICS"](self.scene_element.itemID)

    def addAction(self):
        self.new_item_callbacks["ACTION"](self.scene_element.itemID)

    def updateLabels(self):
        if self.scene_element:
            self._ui.elementLabel.setText(self.scene_element.type)
            if self.scene_element.type in ["OBJECTIVE", "ANIMATION"]:
                self._ui.nameLabel.setText(self.scene_element.name)
            else:
                self._ui.nameLabel.setParent(None)

    def delete(self):
        if self.delete_callback:
            self.delete_callback(self.scene_element.itemID)

    def editElement(self):
        params = ParamDialogue.getParams(self, self.scene_element.type, edit=True, defaults=self.scene_element.dict())
        if not params:
            return
        self.scene_element.edit(params)
        self.updateLabels()

class SubElement(QWidget):
    def __init__(self, scene_element,
                 edit_callback = None,
                 delete_callback = None):
        super().__init__()
        self._ui = Ui_subVisualModeElement()
        self._ui.setupUi(self)
        self.scene_element = scene_element
        self.edit_callback = edit_callback
        self.delete_callback = delete_callback
        self._ui.editButton.clicked.connect(self.editElement)
        self._ui.deleteButton.clicked.connect(self.delete)
        self.updateLabel()
        self.show()

    def delete(self):
        if self.delete_callback:
            self.delete_callback(self.scene_element.itemID)

    def updateLabel(self):
        if self.scene_element:
            self._ui.elementLabel.setText(self.scene_element.type)

    def editElement(self):
        params = ParamDialogue.getParams(self, self.scene_element.type, edit=True, defaults=self.scene_element.dict())
        if not params:
            return
        self.scene_element.edit(params)
        self.updateLabel()