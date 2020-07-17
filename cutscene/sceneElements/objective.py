from cutscene.sceneElements.event import Event
from cutscene.sceneElements.animation import Animation
from cutscene.utils import NameDescription, ID

class Objective(NameDescription, ID):
    """Objective class

    An Objective describes the instantaneous goal of their gameplay within the scene, for e.g;fetch the ball, fnd the key, kill the boss..etc.
    Any given scene can have n number of objectives within it and thus an objective serves as a sub-section for any given scene. 
    An objective can contain events, animations and more objectives as well. When a user decides to create an objective, they will be prompted to name it and then describe it. 

    init: 
        name: str
        description: str

    methods:
        addAnimation: Add an Animation to the objective
            name: str
            description: str
        addEvent: Add an Event to the objective
            name: str
            description: str
        addObjective: Add an Objective to the objective
            name: str
            description: str

        get: Get a list of all the elements of the objective
        remove: Delete an objective element
            index: int; index of element in objective elements list
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
        ID.__init__(self)


    def new(self, item, **kwargs):
        if item == "ANIMATION":
            return self.addAnimation(**kwargs)
        elif item == "EVENT":
            return self.addEvent(**kwargs)
        elif item == "OBJECTIVE":
            return self.addObjective(**kwargs)

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