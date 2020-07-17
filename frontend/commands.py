from PySide2.QtWidgets import QUndoCommand
from cutscene import obj_to_dict

class CommandNew(QUndoCommand):
    """ Reversibly add a new instance of an item to its parent """
    def __init__(self, *, parent, itemType, itemParams, description):
        super(CommandNew, self).__init__(description)
        self.parent = parent
        self.itemType = itemType.upper()
        self.itemParams = itemParams

    def redo(self):
        parent.new(self.itemType, **itemParams)

    def undo(self):
        parent.removeByID(self.itemDict["id"])

class CommandRemove(QUndoCommand):
    """ Reversibly remove an item from its parent """
    def __init__(self, *, parent, item, description):
        super(CommandRemove, self).__init__(description)
        self.parent = parent
        self.itemDict = obj_to_dict(item)
        self.itemType = self.itemDict.pop("__type__").upper()

    def redo(self):
        parent.removeByID(self.itemDict["id"])

    def undo(self):
        parent.new(self.itemType, **self.itemDict)
