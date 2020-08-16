from PySide2.QtCore import QObject, Signal, Slot, QModelIndex
from PySide2.QtWidgets import QFileDialog, QUndoStack, QUndoCommand
from views.paramdialogue_view import ParamDialogue
import os

# The controller class(es) perform any logic and then sets data in the model.
# An example:The change_amount function takes the new value from the widget, performs logic, and sets attributes on the model.


class MainController(QObject):
    activeSceneChanged = Signal()

    def __init__(self, model):
        super().__init__()
        self._model = model
        self.activeLevelItem = None
        self.activeScene = None
        self.undoStack = QUndoStack()

    @property
    def activeScene(self):
        return self.__activeScene

    @activeScene.setter
    def activeScene(self, item):
        if item:
            self.__activeScene = self._model.getInstByID(item.id)
        else:
            self.__activeScene = None
        self.activeSceneChanged.emit()

    def getParentFor(self, item_type):
        if item_type == "CUTSCENEPROJECT":
            parent_types = []
        elif item_type == "LEVEL":
            parent_types = ["CUTSCENEPROJECT"]
        elif item_type == "SUBLEVEL":
            parent_types = ["LEVEL"]
        elif item_type == "SCENE":
            parent_types = ["LEVEL", "SUBLEVEL"]

        def suitableParentType(active, item_type):
            if active.type in parent_types:
                return active
            else:
                return suitableParentType(active.parent(), item_type)

        return suitableParentType(self.activeLevelItem, item_type)

    def openProject(self):
        # toProceed = self.handleUnsavedChanges()
        toProceed = True
        if not toProceed:
            return
        projectPath = QFileDialog.getOpenFileName(None, 'Open Project', 
                os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            self._model.loadProject(projectPath)
            # bit hacky but mm
            idx = self._model.levels_model.index(0,0)
            self.activeLevelItem = self._model.levels_model.itemFromIndex(idx)


    def newProject(self):
        params = ParamDialogue.getParams(self, "CUTSCENEPROJECT")
        self._model.newProject(params)
        idx = self._model.levels_model.index(0,0)
        self.activeLevelItem = self._model.levels_model.itemFromIndex(idx)

    def saveProject(self):
        projectPath = self._model.projectPath
        if not projectPath:
            projectPath = QFileDialog.getSaveFileName(None, 'Save Project', 
                    os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        self._model.saveProject(projectPath)

    def saveProjectAs(self):
        projectPath = QFileDialog.getSaveFileName(None, 'Save Project As', 
                os.path.expanduser("~"),"CutScene Projects (*.cutscene)")[0]
        if projectPath:
            self._model.saveProject(projectPath)

    def newLevel(self):
        self.newLevelItem("LEVEL")

    def newSubLevel(self):
        self.newLevelItem("SUBLEVEL")

    def newScene(self):
        self.newLevelItem("SCENE")

    def newAnimation(self):
        self.newSceneItem("ANIMATION")

    def newObjective(self):
        self.newSceneItem("OBJECTIVE")

    def newEvent(self, *args):
        self.newSceneEvent(*args)

    def newSceneItem(self, item_type):
        params = ParamDialogue.getParams(self, item_type)
        if not params:
            return
        parent = self.activeScene
        assert parent is not None
        command = newSceneItemCommand(self._model, parent, item_type, params)
        self.undoStack.push(command)

    def newSceneEvent(self, fr_id, to_id):
        params = ParamDialogue.getParams(self, "EVENT")
        if not params:
            return
        scene = self.activeScene
        assert scene is not None
        command = newSceneEventCommand(self._model, scene, fr_id, to_id, params)
        self.undoStack.push(command)

    def testNewEventForCycle(self, fr_id, to_id):
        def check_item(item):
            if item in visited:
                return False
            else:
                visited.append(item)
                for child in event_tree[item]:
                    if not check_item(child): return False
                else:
                    return True

        event_tree = self.activeScene.getEvents()
        # add this event to the tree
        if fr_id in event_tree.keys():
            event_tree[fr_id] += [to_id]
        else:
            event_tree[fr_id] = [to_id]
        # test the tree for a loop
        visited = []
        return check_item(list(event_tree.keys())[0])

    def newLevelItem(self, item_type):
        params = ParamDialogue.getParams(self, item_type)
        if not params:
            return
        parent = self.getParentFor(item_type)
        command = newLevelItemCommand(self._model, parent, item_type, params)
        self.undoStack.push(command)

    def undo(self):
        self.undoStack.undo()

    def redo(self):
        self.undoStack.redo()

    @Slot(int)
    def levelItemSelected(self, index):
        """ function called when an item is selected from the levelsView """
        self.activeLevelItem = self._model.levels_model.itemFromIndex(index)
        if self.activeLevelItem.type == "SCENE":
            self.activeScene = self.activeLevelItem

class newLevelItemCommand(QUndoCommand):
    def __init__(self, model, parent, item_type, params):
        QUndoCommand.__init__(self, f"Add new {item_type}")
        self.parent_id = parent.id
        self.item_type = item_type
        self.params = params
        self._model = model
        self.item_id = None
        
    def redo(self):
        self.params["itemID"] = self.item_id
        parent = self._model.getLevelItemById(self.parent_id)
        self.item_id = self._model.addLevelItem(parent, self.item_type, self.params)

    def undo(self):
        self._model.deleteLevelItem(self.item_id)

class newSceneItemCommand(QUndoCommand):
    def __init__(self, model, parent, item_type, params):
        QUndoCommand.__init__(self, f"Add new {item_type}")
        self.parent_id = parent.id
        self.item_type = item_type
        self.params = params
        self._model = model
        self.item_id = None
        
    def redo(self):
        self.params["itemID"] = self.item_id
        self.item_id = self._model.addSceneItem(self.parent_id, self.item_type, self.params)

    def undo(self):
        self._model.deleteSceneItem(self.scene_id, self.item_id)

class newSceneEventCommand(QUndoCommand):
    def __init__(self, model, scene, fr, to, params):
        QUndoCommand.__init__(self, f"Add Event")
        self.scene_id = scene.id
        self.fr = fr
        self.to = to
        self.params = params
        self._model = model
        self.event_id = None
        
    def redo(self):
        self.params["itemID"] = self.event_id
        self.event_id = self._model.addSceneEvent(self.scene_id, self.fr, self.to, self.params)

    def undo(self):
        self._model.deleteSceneEvent(self.scene_id, self.event_id)