from PySide2.QtCore import QObject, Signal
from PySide2.QtGui import QStandardItemModel, QStandardItem, QIcon, QPixmap
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
    projectLoaded = Signal()
    projectSaved = Signal()
    levelsChanged = Signal()

    def __init__(self):
        super().__init__()
        self.project = None
        self.projectPath = None

    def newProject(self, params):
        self.project = cutscene.CutSceneProject(**params)
        self.projectPath = None
        self.initLevelModel()
        self.projectLoaded.emit()

    def loadProject(self, projectPath):
        self.project = cutscene.loadProject(projectPath)
        self.projectPath = projectPath
        self.initLevelModel()
        self.projectLoaded.emit()

    def saveProject(self, projectPath):
        cutscene.saveProject(self.project, projectPath)
        self.projectPath = projectPath
        self.projectSaved.emit()

    def addLevelItem(self, parent, item_type, params):
        level_inst = parent.obj.new(item_type, **params)
        new_item = StandardItem(level_inst, level_inst.name)
        parent.appendRow(new_item)
        self.levelsChanged.emit()

    def getProject(self):
        return self.project

    def getLevels(self):
        return self.project.get()

    def initLevelModel(self):
        # item here refers to level or sublevel
        def newItemEntry(level, parent_item):
            new_item = StandardItem(level, level.name)
            parent_item.appendRow(new_item)
            if new_item.type in ["LEVEL", "SUBLEVEL", "CUTSCENEPROJECT"]:
                for level_inst in level.get():
                    newItemEntry(level_inst, new_item)

        self.levels_model = QStandardItemModel()
        parent_item = self.levels_model.invisibleRootItem()
        newItemEntry(self.project, parent_item)
        self.levelsChanged.emit()


class StandardItem(QStandardItem):
    def __init__(self, obj, name):
        super().__init__(name)
        self.obj = obj
        self.type = obj.dict()["__type__"]
        if self.type == "SCENE":
            icon = QIcon()
            icon.addPixmap(QPixmap(":/levelViewIcons/img/icons/levelViewIcons/videogame_white_96x96.png"), QIcon.Normal, QIcon.Off)
            self.setIcon(icon)



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



        # self._even_odd = ''
        # self._enable_reset = False
