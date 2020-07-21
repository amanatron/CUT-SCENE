from PyQt5.QtCore import QObject, pyqtSignal

# The model class stores program data and state and some minimal logic for announcing changes to this data. 
# This model shouldn't be confused with the Qt model (see http://qt-project.org/doc/qt-4.8/model-view-programming.html) as it's not really the same thing.
# 
# The model might look like:
# 
# Writes to the model automatically emit signals to any listening views via code in the setter decorated functions. 
# Alternatively the controller could manually trigger the signal whenever it decides.
# 
# In the case where Qt model types (e.g. QStringListModel) have been connected with a widget then the view containing 
# that widget does not need to be updated at all; this happens automatically via the Qt framework.


class Model(QObject):
    amount_changed = pyqtSignal(int)
    even_odd_changed = pyqtSignal(str)
    enable_reset_changed = pyqtSignal(bool)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
        self.amount_changed.emit(value)

    @property
    def even_odd(self):
        return self._even_odd

    @even_odd.setter
    def even_odd(self, value):
        self._even_odd = value
        self.even_odd_changed.emit(value)

    @property
    def enable_reset(self):
        return self._enable_reset

    @enable_reset.setter
    def enable_reset(self, value):
        self._enable_reset = value
        self.enable_reset_changed.emit(value)

    def __init__(self):
        super().__init__()

        self._amount = 0
        self._even_odd = ''
        self._enable_reset = False