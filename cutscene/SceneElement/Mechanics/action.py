import Descriptive

class Action(Descriptive):
    """This is simply a way for the user to describe that which this action is a child of.
    For example,if the player creates a scene and then chooses action, they can describe the scene or any additional narrative at any given instance.
    Similarly, they can choose to describe an event in any way they want using action."""
    def __init__(self, description: str):
        super().__init__(description)