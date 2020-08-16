from cutscene.sceneElements.event import Event
from cutscene.sceneElements.action import Action
from cutscene.sceneElements.physics import Physics
from cutscene.sceneElements.pseudocode import Pseudocode
from cutscene.utils import NameDescription, Instantiable, OrderedInstanceHolder
from typing import Optional

class Objective(NameDescription, Instantiable, OrderedInstanceHolder):
    """Objective class

    An Objective describes the instantaneous goal of their gameplay within the scene, for e.g;fetch the ball, fnd the key, kill the boss..etc.
    Any given scene can have n number of objectives within it and thus an objective serves as a sub-section for any given scene. 
    An objective can contain events, animations and more objectives as well. When a user decides to create an objective, they will be prompted to name it and then describe it. 

    init: 
        name: str
        description: str

    methods:
        addControl: 
        addAction:
        addPseudocode:
        addPhysics

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
                 description: str,
                 itemID: Optional[int] = None):
        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["CONTROL"], 
                paramHelp["ACTION"], 
                paramHelp["PHYSICS"], 
                paramHelp["PSEUDOCODE"])
        
    def new(self, item, **kwargs):
        if item == "CONTROL":
            return self.addAnimation(**kwargs)
        elif item == "ACTION":
            return self.addAction(**kwargs)
        elif item == "PHYSICS":
            return self.addPhysics(**kwargs)
        elif item == "PSEUDOCODE":
            return self.addPseudocode(**kwargs)

    def addControl(self, *args, **kwargs):
        control = Control(*args, **kwargs)
        self.addNew(control)
        return control

    def addAction(self, *args, **kwargs):
        action = Action(*args, **kwargs)
        self.addNew(action)
        return action

    def addPseudocode(self, *args, **kwargs):
        pseudocode = Pseudocode(*args, **kwargs)
        self.addNew(pseudocode)
        return pseudocode

    def addPhysics(self, *args, **kwargs):
        physics = Physics(*args, **kwargs)
        self.addNew(physics)
        return physics