from cutscene.utils import OrderedInstanceHolder, NameDescription, Instantiable
from cutscene.sceneElements.animation import Animation
from cutscene.sceneElements.event import Event
from cutscene.sceneElements.objective import Objective
from typing import Optional

class Scene(OrderedInstanceHolder, NameDescription, Instantiable):
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
        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID)

    def new(self, item, **kwargs):
        if item == "ANIMATION":
            return self.addAnimation(**kwargs)
        elif item == "EVENT":
            return self.addEvent(**kwargs)
        elif item == "OBJECTIVE":
            return self.addObjective(**kwargs)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["ANIMATION"], 
                paramHelp["EVENT"], 
                paramHelp["OBJECTIVE"])

    def addAnimation(self, *args, **kwargs):
        animation = Animation(*args, **kwargs)
        self.addNew(animation)
        return animation

    def addEvent(self, *args, **kwargs):
        event = Event(*args, **kwargs)
        self.addNew(event)
        return event

    def addObjective(self, *args, **kwargs):
        objective = Objective(*args, **kwargs)
        self.addNew(objective)
        return objective