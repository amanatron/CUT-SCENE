from cutscene.sceneElements.action import Action
from cutscene.utils import NameDescription, OrderedInstanceHolder
from typing import Optional

class Animation(NameDescription, OrderedInstanceHolder):
    """Animation Class"""
    def __init__(self, 
                 name: str,
                 description: str):
        NameDescription.__init__(self, name, description)
        OrderedInstanceHolder.__init__(self)

    def addAction(self, *args):
        action = Action(*args)
        self.addNew(action)

    def addTransition(self, *args):
        transition = Transition(*args)
        self.addNew(transition)

    def addHeading(self, *args):
        heading = Heading(*args)
        self.addNew(heading)

    def addDialogue(self, *args):
        dialogue = Dialogue(*args)
        self.addNew(dialogue)

    def addAct(self, *args):
        act = Act(*args)
        self.addNew(act)

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

class Act(AnimationText):
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
                 paranthetical: Optional[str] = None):
        self.character_name = character_name
        self.dialogue = dialogue
        self.paranthetical = paranthetical

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
