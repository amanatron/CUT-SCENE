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

class Level(LevelWrapper):
    """Level object"""
    def __init__(self, 
                 name: str,
                 description: str):
        super().__init__(name, description)

    def addSubLevel(self, *args):
        subLevel = SubLevel(*args)
        self.addNew(subLevel)

class SubLevel(LevelWrapper):
    """docstring for SceneElement"""
    def __init__(self, 
                 name: str,
                 description: str):
        super().__init__(name, description)