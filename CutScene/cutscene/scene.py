from cutscene.utils import NameDescription, Instantiable
from cutscene.sceneElements.animation import Animation
from cutscene.sceneElements.event import Event
from cutscene.sceneElements.objective import Objective
from typing import Optional

class Scene(NameDescription, Instantiable):
    """Scene object. Everything in cutscene happens in a Scene.

    init: 
        name: str
        description: str

    methods:
        addAnimation: Add an Animation to the scene
            name: str
            description: str
        addEvent: Add an Event to the scene
            name: str
            description: str
        addObjective: Add an Objective to the scene
            name: str
            description: str

        get: Get a list of all the elements of the scene
        remove: Delete a scene element
            index: int; index of element in scene elements list
        moveUp: move element at index one place up in the list
            index: int
        moveDown: move element at index one place down the list
            index: int
        move: move element from one index to another
            index: int, which element you want
            newIndex: int, where you want the element to go
    """
    def __init__(self, 
                 name: str,
                 description: str,
                 itemID: Optional[int] = None):
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID)
        self.elements = []
        self.sceneMatrix = []

    def __itemIdxFromId(self, elem_id):
        for idx, element in enumerate(self.elements):
            if element.id == elem_id:
                return idx

    def __eventIdxFromId(self, event_id):
        for x, row in enumerate(self.sceneMatrix):
            for y, event in enumerate(row):
                if event is not None:
                    if event.id == event_id:
                        return (x, y)

    @property
    def __elementCount(self):
        return len(self.elements)
        # returns number of scene elements

    def addNew(self, item):
        # add row at bottom of scene matrix
        self.sceneMatrix.append([None for i in range(self.__elementCount)])
        # add column
        for element in self.sceneMatrix:
            element.append(None)
        # add to item list
        self.elements.append(item)
        # make link?
        pass

    def addEvent(self, id1, id2, **kwargs):
        x = self.__itemIdxFromId(id1)
        y = self.__itemIdxFromId(id2)
        event = Event(**kwargs)
        self.sceneMatrix[x][y] = event
        self.sceneMatrix[y][x] = event

    def delEvent(self, event_id):
        x, y = self.__eventIdxFromId(event_id)
        self.sceneMatrix[x][y] = None
        self.sceneMatrix[y][x] = None

    def moveEvent(self, event_id, new_id1, new_id2):
        x, y = self.__eventIdxFromId(event_id)
        event = self.sceneMatrix[x][y]
        self.sceneMatrix[x][y] = None
        self.sceneMatrix[y][x] = None
        self.sceneMatrix[new_id1][new_id2] = event
        self.sceneMatrix[new_id2][new_id1] = event

    def getEvent(self, event_id):
        x, y = self.__eventIdxFromId(event_id)
        return self.sceneMatrix[x][y]

    def new(self, item, **kwargs):
        if item == "ANIMATION":
            return self.addAnimation(**kwargs)
        elif item == "OBJECTIVE":
            return self.addObjective(**kwargs)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["ANIMATION"], 
                paramHelp["OBJECTIVE"])

    def addAnimation(self, *args, **kwargs):
        animation = Animation(*args, **kwargs)
        self.addNew(animation)
        return animation

    def addObjective(self, *args, **kwargs):
        objective = Objective(*args, **kwargs)
        self.addNew(objective)
        return objective