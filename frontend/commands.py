from PySide2.QtWidgets import QUndoCommand

class CommandNew(QUndoCommand):

    def __init__(self, parent, itemType, itemParams, description):
        super(CommandNew, self).__init__(description)
        self.parent = parent
        self.itemType = itemType.Upper()
        self.itemParams = itemParams

    def redo(self):
        parent.new(self.itemType, **item)

    def undo(self):
        item = self.listWidget.takeItem(self.row)
        del item