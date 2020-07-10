from cutscene.utils import OrderedInstanceHolder, NameDescription
from cutscene.sceneElements.animation import Animation
from cutscene.sceneElements.event import Event
from cutscene.sceneElements.objective import Objective

class Scene(OrderedInstanceHolder, NameDescription):
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
                 description: str):
        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)

    def addAnimation(self, *args):
        animation = Animation(*args)
        self.addNew(animation)
        return animation

    def addEvent(self, *args):
        event = Event(*args)
        self.addNew(event)
        return event

    def addObjective(self, *args):
        objective = Objective(*args)
        self.addNew(objective)
        return objective