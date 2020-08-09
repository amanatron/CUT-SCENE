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
        self.itemType = self.itemDict.pop("type").upper()

    def redo(self):
        parent.removeByID(self.itemDict["id"])

    def undo(self):
        parent.new(self.itemType, **self.itemDict)

class CommandEdit(QUndoCommand):
    """ Reversibly edit an item's attributes """
    def __init__(self, *, item, newParams, description):
        super(CommandEdit, self).__init__(description)
        self.item = item
        self.newParams = itemParams
        self.oldParams = obj_to_dict(item)
        self.oldParams.pop("type")     # Not strictly necessary but hey,
        self.oldParams.pop("id")       # let's be nice to the backend

    def redo(self):
        item.edit(self.newParams)

    def undo(self):
        item.edit(self.oldParams)
