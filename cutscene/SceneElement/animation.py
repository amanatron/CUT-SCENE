from Mechanics import Action
from typing import Optional, Tuple

class Animation(SceneElement):
    """Animation Class"""
    def __init__(self, 
                 name: str,
                 description: str):
        super().__init__(name, description)
        self.__animation = []

    @property
    def animation(self) -> list:
        return self.__animation

    def addAction(self, *args):
        action = Action(*args)
        self.animation.append(action)

    def addTransition(self, *args):
        transition = Transition(*args)
        self.animation.append(transition)

    def addHeading(self, *args):
        heading = Heading(*args)
        self.animation.append(heading)

    def addDialogue(self, *args):
        dialogue = Dialogue(*args)
        self.animation.append(dialogue)

    def remove(self,
               index: int)
        assert type(index) is int
        del self.animation[index]

    def __elementSwap(self,
                      index1,
                      index2):
        """Elementwise swap of two items at specified indexes"""
        self.animation[index1], self.animation[index2] = self.animation[index2], self.animation[index1]

    def moveUp(self,
               index: int):
        assert type(index) is int
        if index == 0:
            raise ValueError("Can't move first element of list up")
        elif 0 > index > len(self.animation):
            raise ValueError("Index out of range: {}".format(Index))
        self.__elementSwap(index, index-1)

    def moveDown(self,
                 index: int):
        assert type(index) is int
        if index == len(self.animation):
            raise ValueError("Can't move last element of list down")
        elif 0 > index > len(self.animation):
            raise ValueError("Index out of range: {}".format(Index))
        self.__elementSwap(index, index+1)

    def move(self,
             index: int,
             newIndex: int)
        assert type(index) is int
        assert type(newIndex) is int
        if 0 > index > len(self.animation):
            raise ValueError("Index out of range: {}".format(Index))
        if 0 > newIndex > len(self.animation)-1:
            raise ValueError("newIndex out of range: {}".format(newIndex))
        item = self.animation.pop(index)
        self.animation.insert(newIndex, item)

class AnimationText(Animation):
    """A piece of text in an animation, wrapper class for Transition and Heading"""
    def __init__(self,
                 text: str):
        self.text = text

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        assert type(text) is str
        self.__text = text

class Transition(AnimationText):
    """Describe a transition in an animation"""
    def __init__(self,
                 text: str):
        super().__init__(text)

class Heading(AnimationText):
    """Add a heading in an animation"""
    def __init__(self,
                 text: str):
        super().__init__(text)

class Dialogue(Animation):
    """A single piece of dialogue from a character"""
    def __init__(self,
                 character_name: str, # character = getCharacter(character_name)
                 dialogue: str,
                 paranthetical: Optional[str] = None)

    @property
    def character_name(self) -> str:
        return self.__character_name

    @character_name.setter
    def character_name(self, character_name: str):
        assert type(character_name) is str
        self.__character_name = character_name

    @property
    def paranthetical(self) -> str:
        return self.__paranthetical

    @paranthetical.setter
    def paranthetical(self, paranthetical: str):
        assert type(paranthetical) is str
        self.__paranthetical = paranthetical

    @property
    def dialogue(self) -> str:
        return self.__dialogue

    @dialogue.setter
    def dialogue(self, dialogue: str):
        assert type(dialogue) is str
        self.__dialogue = dialogue
