# CUTSCENE # 

class LevelWrapper(object):
    """Thin wrapper around level and sublevel classes.
    These share many similar methods so a wrapper is used here."""
    def __init__(self, 
                 name: str,
                 description: str):
        self.name = name
        self.description = description

    @property
    def description(self) -> str:
        return self.__description

    @property
    def name(self) -> str:
        return self.__name

    @description.setter
    def description(self, description: str):
        assert type(description) is str
        self.__description = description

    @name.setter
    def name(self, name: str):
        assert type(name) is str
        self.__name = name

    def addScene(self):
        pass