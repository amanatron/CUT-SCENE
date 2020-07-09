class EntityWrapper(object):
    """Thin wrapper around character and misc entity classes.
    These share many similar methods so a wrapper is used here.
    This base class is not to be imported, instead use Character and Misc."""
    def __init__(self, 
                 name: str,
                 description: str,
                 entityType: str):
        super().__init__(name, description)
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
    """Character object/entity"""
    entityTypes = ["RESPONSIVE", "NON-RESPONSIVE"]

    def __init__(self, 
                 name: str,
                 description: str,
                 entityType: str):
        super().__init__(name, description, entityType)