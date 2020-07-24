from PySide2.QtCore import QObject, Signal, Slot 
from PySide2.QtGui import QStandardItemModel, QStandardItem
import cutscene


# The model class stores program data and state and some minimal logic for announcing changes to this data. 
# This model shouldn't be confused with the Qt model (see http://qt-project.org/doc/qt-4.8/model-view-programming.html) as it's not really the same thing.
# 
# The model might look like:
# 
# Writes to the model automatically emit signals to any listening views via code in the setter decorated functions. 
# Alternatively the controller could manually trigger the signal whenever it decides.
# 
# In the case where Qt model types (e.g. QStringListModel) have been connected with a widget then the view containing 
# that widget does not need to be updated at all; this happens automatically via the Qt framework.


class Model(QObject):
    activeSceneChanged = Signal()
    projectLoaded = Signal()
    #even_odd_changed = Signal(str)
    #enable_reset_changed = Signal(bool)


    # @property
    # def active_level(self):
    #     return self._active_level

    # @active_level.setter
    # def active_level(self, value):
    #     self._active_level = value
    #     self.activeLevelChanged.emit(value)

    def get_project(self):
        return self.project

    def get_levels(self):
        return self.project.get()

    def loadProject(self, projectPath):
        self.project = cutscene.loadProject(projectPath)
        self.projectPath = projectPath
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
        newItemEntry(self.project, parent_item)

    # def initSceneModel(self, scene):

    #     # item here refers to sceneElement
    #     def newItemEntry(element, parent_item):
    #         item_dict = element.dict()
    #         new_item = StandardItem(element, item_dict["__type__"])
    #         parent_item.appendRow(new_item)
    #         if item_dict["__type__"] in ["ANIMATION", "SCENE"]:
    #             for item in element.get():
    #                 newItemEntry(item, new_item)

    #     self.scene_model = QStandardItemModel()
    #     parent_item = self.scene_model.invisibleRootItem()
    #     newItemEntry(scene, parent_item)

    def levelItemSelected(self, item):
        """ function called when an item is selected from the levelsView """
        level_item = self.levels_model.itemFromIndex(item).obj
        item_dict = level_item.dict()
        if item_dict["__type__"] == "SCENE":
            #self.initSceneModel(level_item)
            self.activeSceneChanged.emit()


    # @property
    # def even_odd(self):
    #     return self._even_odd

    # @even_odd.setter
    # def even_odd(self, value):
    #     self._even_odd = value
    #     self.even_odd_changed.emit(value)

    # @property
    # def enable_reset(self):
    #     return self._enable_reset

    # @enable_reset.setter
    # def enable_reset(self, value):
    #     self._enable_reset = value
    #     self.enable_reset_changed.emit(value)

    def __init__(self):
        super().__init__()
        self._active_level = None
        self.project = None
        self.projectPath = None
        self.projectLoaded.connect(self.initLevelModel)


        # self._even_odd = ''
        # self._enable_reset = False

class StandardItem(QStandardItem):
    def __init__(self, obj, name):
        super().__init__(name)
        self.obj = obj
