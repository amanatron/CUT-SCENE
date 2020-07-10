from cutscene.utils import NameDescription

class EntitiesWrapper(object):
    def __init__(self):
        self.__entities = []

    def addNew(self, item):
        self.__entities.append(item)

    def get(self) -> list:
        return self.__entities

    def remove(self,
               index: int):
        assert type(index) is int
        del self.__entities[index]

class Characters(EntitiesWrapper):
    """ This is the class you want to import for Characters.
    eg. from entities import Characters, Objects
    it is a manager for all the characters, allowing you to add, get, and remove characters"""
    def __init__(self):
        super().__init__()

    def addCharacter(self, *args):
        character = Character(*args)
        self.addNew(character)

class Objects(EntitiesWrapper):
    """ This is the class you want to import for Objects.
    it is a manager for all the objects, allowing you to add, get, and remove characters"""
    def __init__(self):
        super().__init__()

    def addObject(self, *args):
        misc = Misc(*args)
        self.addNew(misc)



class EntityWrapper(NameDescription):
    """Thin wrapper around character and misc entity classes.
    These share many similar methods so a wrapper is used here.
    This base class is not to be imported, instead use Character and Misc."""
    def __init__(self, 
                 name: str,
                 description: str,
                 entityType: str):
        NameDescription.__init__(self, name, description)
        self.entityType = entityType

    @property
    def entityType(self) -> str:
        return self.__entityType

    @entityType.setter
    def entityType(self, entityType: str):
        assert type(entityType) is str
        assert entityType.upper() in entityTypes
        self.__entityType = entityType

class Character(EntityWrapper):
    """Character object/entity"""
    entityTypes = ["PLAYER", "ENEMY", "OTHER"]

    def __init__(self, 
                 name: str,
                 description: str,
                 entityType: str):
        super().__init__(name, description, entityType)

        ## TODO add image of character, character.face

class Misc(EntityWrapper):
    """Misc object/entity"""
    entityTypes = ["RESPONSIVE", "NON-RESPONSIVE"]

    def __init__(self, 
                 name: str,
                 description: str,
                 entityType: str):
        super().__init__(name, description, entityType)