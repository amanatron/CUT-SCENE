from cutscene.utils import OrderedInstanceHolder, NameDescription, Instantiable, MapImage
from cutscene.scene import Scene
from typing import Optional
from uuid import uuid4

class LevelWrapper(OrderedInstanceHolder, NameDescription, MapImage):
    """Thin wrapper around level and sublevel classes.
    These share many similar methods so a wrapper is used here."""

    def __init__(self,
                 name: str,
                 description: str,
                 img: Optional[str] = None):
        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)
        MapImage.__init__(self, img)

    def addScene(self, *args, **kwargs):
        scene = Scene(*args, parentID = self.id, **kwargs)
        self.addNew(scene)
        return scene

    def new(self, item, **kwargs):
        if item == "SCENE":
            return self.addScene(**kwargs)

class Level(LevelWrapper, Instantiable):
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
                 description: str,
                 img: Optional[str] = None,
                 itemID: Optional[int] = None,
                 parentID: Optional[int] = None):
        LevelWrapper.__init__(self, name, description, img)
        Instantiable.__init__(self, itemID, parentID)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["SUBLEVEL"], paramHelp["SCENE"])

    # extend new() for Level to include addScene
    def new(self, item, **kwargs):
        if item == "SUBLEVEL":
            return self.addSubLevel(**kwargs)
        elif item == "SCENE":
            return self.addScene(**kwargs)

    def addSubLevel(self, *args, **kwargs):
        subLevel = SubLevel(*args, parentID = self.id, **kwargs)
        self.addNew(subLevel)
        return subLevel

class SubLevel(LevelWrapper, Instantiable):
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
                 description: str,
                 img: Optional[str] = None,
                 itemID: Optional[int] = None,
                 parentID: Optional[int] = None):
        LevelWrapper.__init__(self, name, description, img)
        Instantiable.__init__(self, itemID, parentID)

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["SCENE"])