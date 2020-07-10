from cutscene.utils import OrderedInstanceHolder, NameDescription
from cutscene.level import Level, SubLevel
from cutscene.scene import Scene
from cutscene.entities import Characters, Objects

class CutSceneProject(OrderedInstanceHolder, NameDescription):
    """ Highest level class for the entire cutscene project. 
    init: 
        name: str,
        description: str,
        genre: str,
        author: str

    methods:
        addLevel: Add a new level to the project 
            name: str,
            description: str
        addScene: Add a new scene to the project 
            name: str,
            description: str
        get: Get a list of all the highest level elements of the project (scenes, levels)
        remove: Delete an element
            index: int; index of element in project elements list
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
                 genre: str,
                 author: str):

        OrderedInstanceHolder.__init__(self)
        NameDescription.__init__(self, name, description)

        assert type(genre) is str
        assert type(author) is str

        self.genre = genre
        self.author = author

        self.characters = Characters()
        self.objects = Objects()
        
    def addLevel(self, *args):
        """ Add a new level to the project """
        level = Level(*args)
        self.addNew(level)
        return level

    def addScene(self, *args):
        """ Add a new scene to the project """
        scene = Scene(*args)
        self.addNew(scene)
        return scene