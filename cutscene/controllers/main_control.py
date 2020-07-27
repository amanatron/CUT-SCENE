from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtWidgets import QFileDialog
from PySide2.QtGui import QStandardItemModel, QStandardItem

from views.paramdialogue_view import ParamDialogue

# The controller class(es) perform any logic and then sets data in the model.
# An example:The change_amount function takes the new value from the widget, performs logic, and sets attributes on the model.


class MainController(QObject):
    activeLevelItemChanged = Signal(str)
    projectLoaded = Signal()

    def __init__(self, model):
        super().__init__()
        self._model = model
        self.activeLevelItem = None
        self.projectLoaded.connect(self.initLevelModel)

    def openProject(self):
        # toProceed = self.handleUnsavedChanges()
        toProceed = True
        if not toProceed:
            return
        projectPath = QFileDialog.getOpenFileName(self, 'Open Project', 
                os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            self.loadProject(projectPath)

    def newItem(self, item_type, item_parent):
        pass

    def newProject(self):
        # toProceed = self.handleUnsavedChanges()
        toProceed = True
        if not toProceed:
            return
        params = ParamDialogue.getParams(self, "PROJECT")
        if params:
            print(params)
            self._model.newProject(**params)
        else:
            pass
        # self._model.newProject(**params)

    def newLevel(self):
        # toProceed = self.handleUnsavedChanges()
        toProceed = True
        if not toProceed:
            return
        params = ParamDialogue.getParams(self, "PROJECT")
        if params:
            print(params)
            self._model.newProject(**params)
        else:
            pass

    def saveProject(self):
        pass

    def saveAsProject(self):
        pass

    @Slot(str)
    def loadProject(self, projectPath):
        self._model.loadProject(projectPath)
        self.projectLoaded.emit()

    def initLevelModel(self):
        # item here refers to level or sublevel
        def newItemEntry(level, parent_item):
            new_item = StandardItem(level, level.name)
            parent_item.appendRow(new_item)
            item_dict = level.dict()
            if item_dict["__type__"] in ["LEVEL", "SUBLEVEL", "CUTSCENEPROJECT"]:
                for item in level.get():
                    newItemEntry(item, new_item)

        self.levels_model = QStandardItemModel()
        parent_item = self.levels_model.invisibleRootItem()
        newItemEntry(self._model.project, parent_item)

    @Slot(int)
    def levelItemSelected(self, item):
        """ function called when an item is selected from the levelsView """
        level_item = self.levels_model.itemFromIndex(item).obj
        item_dict = level_item.dict()
        print(item_dict["__type__"])
        self.activeLevelItem = level_item
        self.activeLevelItemChanged.emit(item_dict["__type__"])

class StandardItem(QStandardItem):
    def __init__(self, obj, name):
        super().__init__(name)
        self.obj = obj
