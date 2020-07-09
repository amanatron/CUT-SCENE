class Mechanics(object):
    """Base class for all Mechanics classes"""
    def __init__(self):
        pass

class Descriptive(Mechanics):
    """Base class for descriptive classes: Action, Physics"""
    def __init__(self, description: str):
        self.description = description

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        assert type(description) is str
        self.__description = description
