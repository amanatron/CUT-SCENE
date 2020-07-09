import Event
import Animation

class Objective(SceneElement):
    """Objective class"""
    def __init__(self,
                 name: str,
                 description: str):
        super().__init__(name, description)

    def addEvent(self, *args):
        Event(*args)

    def addAnimation(self, *args):
        Animation(*args)

    def addObjective(self, *args):
        Objective(*args)