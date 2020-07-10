from cutscene.utils import OrderedInstanceHolder, NameDescription
from cutscene.level import Level, SubLevel
from cutscene.scene import Scene
from cutscene.entities import Characters, Objects

class CutSceneProject(OrderedInstanceHolder, NameDescription):
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
        level = Level(*args)
        self.addNew(level)

    def addScene(self, *args):
        scene = Scene(*args)
        self.addNew(scene)