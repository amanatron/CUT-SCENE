from PyQt5.QtCore import QObject, pyqtSlot

# The controller class(es) perform any logic and then sets data in the model.
# An example:The change_amount function takes the new value from the widget, performs logic, and sets attributes on the model.


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @pyqtSlot(int)
    def change_amount(self, value):
        self._model.amount = value

        # calculate even or odd
        self._model.even_odd = 'odd' if value % 2 else 'even'

        # calculate button enabled state
        self._model.enable_reset = True if value else False