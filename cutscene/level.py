from cutscene.utils import OrderedInstanceHolder, NameDescription
from cutscene.scene import Scene

class LevelWrapper(OrderedInstanceHolder, NameDescription):
    """Thin wrapper around level and sublevel classes.
    These share many similar methods so a wrapper is used here."""

    def __init__(self, 
                 name: str,
                 description: str):
        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)

    def addScene(self, *args):
        scene = Scene(*args)
        self.addNew(scene)
        return scene

class Level(LevelWrapper):
    """Level object

    init: 
        name: str
        description: str

    methods:
        addScene: Add a scene to the level
            name: str
            description: str
        addSubLevel: Add a sublevel to the level
            name: str
            description: str

        get: Get a list of all the elements of the level
        remove: Delete a level element
            index: int; index of element in level elements list
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
        super().__init__(name, description)

    def addSubLevel(self, *args):
        subLevel = SubLevel(*args)
        self.addNew(subLevel)
        return subLevel

class SubLevel(LevelWrapper):
    """Sublevel object

    init: 
        name: str
        description: str

    methods:
        Same as Level, but without addSubLevel
        See Level methods
    """
    def __init__(self, 
                 name: str,
                 description: str):
        super().__init__(name, description)