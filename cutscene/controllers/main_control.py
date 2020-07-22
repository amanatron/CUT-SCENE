from PySide2.QtCore import QObject, Slot

# The controller class(es) perform any logic and then sets data in the model.
# An example:The change_amount function takes the new value from the widget, performs logic, and sets attributes on the model.


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @Slot(int)
    def levelItemSelected(self, item):
        self._model.levelItemSelected()

        # # calculate even or odd
        # self._model.even_odd = 'odd' if value % 2 else 'even'

        # # calculate button enabled state
        # self._model.enable_reset = True if value else False

    @Slot(str)
    def loadProject(self, projectPath):
        self._model.loadProject(projectPath)