from cutscene.utils import NameDescription, Instantiable, CharacterImage, Image
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

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["CHARACTER"])

    def new(self, item, **kwargs):
        if item == "CHARACTER":
            return self.addCharacter(**kwargs)

    def addCharacter(self, *args, **kwargs):
        character = Character(parentID = self.id, **kwargs)
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

    @property
    def help(self):
        """ Get info on what items can be created by this class, and their required parameters """
        return (paramHelp["OBJECT"])

    def new(self, item, **kwargs):
        if item == "OBJECT":
            return self.addObject(**kwargs)

    def addObject(self, *args, **kwargs):
        misc = Misc(parentID = self.id, **kwargs)
        self.addNew(misc)
        return misc


class Character(NameDescription, Instantiable, CharacterImage):
    """Character object/entity"""
    def __init__(self,
                 name: str,
                 description: str,
                 entityType: str,
                 img: Optional[str] = None,
                 itemID: Optional[int] = None,
                 parentID: Optional[int] = None):
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID, parentID)
        CharacterImage.__init__(self, img)
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

class Misc(NameDescription, Instantiable, Image):
    """Misc object/entity"""
    def __init__(self,
                 name: str,
                 description: str,
                 entityType: str,
                 img: Optional[str] = None,
                 itemID: Optional[int] = None,
                 parentID: Optional[int] = None):
        NameDescription.__init__(self, name, description)
        Instantiable.__init__(self, itemID, parentID)
        Image.__init__(self, img)
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