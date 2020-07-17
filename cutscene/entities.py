from cutscene.utils import NameDescription, Instantiable
from typing import Optional

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

    def removeByID(self,
                   itemID: int):
        assert type(itemID) is int
        for index, item in enumerate(self.__entities):
            if item.id == itemID:               
                del self.__entities[index]
                break

class Characters(EntitiesWrapper):
    """ Manager for all the characters, allowing you to add, get, and remove characters

    init: 
        None

    methods:
        addCharacter: Add a new character to the project 
            name: str,
            description: str,
            entityType: str in ["PLAYER", "ENEMY", "OTHER"]
        get: Get a list of characters in the project 
        remove: Delete a character from the project
            index: int; index of character in character list 
    """
    def __init__(self):
        super().__init__()

    def new(self, item, **kwargs):
        if item == "CHARACTER":
            return self.addCharacter(**kwargs)

    def addCharacter(self, *args, **kwargs):
        character = Character(**kwargs)
        self.addNew(character)
        return character

class Objects(EntitiesWrapper):
    """ Manager for all the objects, allowing you to add, get, and remove objects

    init: 
        None

    methods:
        addObject: Add a new object to the project 
            name: str,
            description: str,
            entityType: str in ["RESPONSIVE", "NON-RESPONSIVE"]
        get: Get a list of objects in the project 
        remove: Delete a object from the project
            index: int; index of object in object list 
    """
    def __init__(self):
        super().__init__()

    def new(self, item, **kwargs):
        if item == "OBJECT":
            return self.addObject(**kwargs)

    def addObject(self, *args, **kwargs):
        misc = Misc(**kwargs)
        self.addNew(misc)
        return misc


class Character(NameDescription, Instantiable):
    """Character object/entity"""
    def __init__(self,
                 name: str,
                 description: str,
                 entityType: str,
                 itemID: Optional[int] = None):
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID)
        self.entityType = entityType
        ## TODO add image of character, character.face

    @property
    def entityType(self) -> str:
        return self.__entityType

    @entityType.setter
    def entityType(self, entityType: str):
        assert type(entityType) is str
        assert entityType.upper() in ["PLAYER", "ENEMY", "OTHER"]
        self.__entityType = entityType

class Misc(NameDescription, Instantiable):
    """Misc object/entity"""
    def __init__(self,
                 name: str,
                 description: str,
                 entityType: str,
                 itemID: Optional[int] = None):
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID)
        self.entityType = entityType
        ## TODO add image of character, character.face

    @property
    def entityType(self) -> str:
        return self.__entityType

    @entityType.setter
    def entityType(self, entityType: str):
        assert type(entityType) is str
        assert entityType.upper() in ["RESPONSIVE", "NON-RESPONSIVE"]
        self.__entityType = entityType