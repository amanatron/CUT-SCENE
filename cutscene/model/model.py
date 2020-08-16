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
    sceneModified = Signal()


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

    def addLevelItem(self, parent_item, item_type, params):
        parent_inst = cutscene.utils.getByID(parent_item.id)
        level_inst = parent_inst.new(item_type, **params)
        level_item = StandardItem(level_inst, level_inst.name)
        parent_item.appendRow(level_item)
        self.levelsChanged.emit()
        return level_inst.id

    def addSceneItem(self, parent_id, item_type, params):
        parent = self.getInstByID(parent_id)
        scene_item = parent.new(item_type, **params)
        print(f"model added {item_type} to parent {parent_id} with params: {params}")
        self.sceneModified.emit()
        return scene_item.id

    def addSceneEvent(self, scene_id, fr, to, params):
        scene = self.getInstByID(scene_id)
        event = scene.addEvent(fr, to, **params)
        print(f"model added Event to scene {scene_id}, linking {fr} to {to} with params: {params}")
        self.sceneModified.emit()
        return event.id

    def getInstByID(self, item_id):
        return cutscene.utils.getByID(item_id)

    def getLevelItemById(self, item_id):
        def searchById(parent_index, item_id):
            parent_item = self.levels_model.itemFromIndex(parent_index)
            if parent_item.id == item_id:
                return parent_item
            elif parent_item.type in ["LEVEL", "SUBLEVEL", "CUTSCENEPROJECT"]:
                for row in range(parent_item.rowCount()):
                    index = self.levels_model.index(row, 0, parent_index)
                    item = searchById(index, item_id)
                    if item:
                        return item

        root_index = self.levels_model.index(0,0)
        obj = searchById(root_index, item_id)
        if obj:
            return obj
        else:
            raise ValueError(f"Item with id {item_id} not found")

    def deleteLevelItem(self, item_id):
        def deleteById(level, item_id):
            for idx, item in enumerate(level.get()):
                if item.id == item_id:
                    level.remove(idx)
                elif item.type in ["LEVEL", "SUBLEVEL"]:
                    deleteById(item, item_id)
        def deleteItemById(parent_index, item_id):
            parent_item = self.levels_model.itemFromIndex(parent_index)
            if parent_item.type in ["LEVEL", "SUBLEVEL", "CUTSCENEPROJECT"]:
                for row in range(parent_item.rowCount()):
                    index = self.levels_model.index(row, 0, parent_index)
                    item = self.levels_model.itemFromIndex(index)
                    if item.id == item_id:
                        self.levels_model.removeRow(row, parent_index)
                        return True
                    else:
                        ret = deleteItemById(index, item_id)
                        if ret:
                            return ret

        root_index = self.levels_model.index(0,0)
        deleteById(self.project, item_id)
        deleteItemById(root_index, item_id)
        self.levelsChanged.emit()

    def deleteSceneItem(self, scene_id, item_id):
        scene = self.getInstByID(scene_id)
        scene.delItem(item_id)
        print(f"model deleted scene item with id {item_id}")
        self.sceneModified.emit()

    def deleteSceneEvent(self, scene_id, event_id):
        scene = self.getInstByID(scene_id)
        scene.delEvent(event_id)
        print(f"model deleted scene event with id {event_id}")
        self.sceneModified.emit()

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
        _dict = obj.dict()
        self.type = _dict["type"]
        self.id = _dict["itemID"]
        if self.type == "SCENE":
            icon = QIcon()
            icon.addPixmap(QPixmap(":/levelViewIcons/img/icons/levelViewIcons/videogame_white_96x96.png"), QIcon.Normal, QIcon.Off)
            self.setIcon(icon)


    # def initSceneModel(self, scene):

    #     # item here refers to sceneElement
    #     def newItemEntry(element, parent_item):
    #         item_dict = element.dict()
    #         new_item = StandardItem(element, item_dict["type"])
    #         parent_item.appendRow(new_item)
    #         if item_dict["type"] in ["ANIMATION", "SCENE"]:
    #             for item in element.get():
    #                 newItemEntry(item, new_item)

    #     self.scene_model = QStandardItemModel()
    #     parent_item = self.scene_model.invisibleRootItem()
    #     newItemEntry(scene, parent_item)



        # self._even_odd = ''
        # self._enable_reset = False
