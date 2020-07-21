from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from views.main_view_ui import Ui_MainWindow

# Use Qt designer to create the .ui layout files to the extent that you assign variables names to widgets and adjust their basic properties. 
# Don't bother adding signals or slots as it's generally easier just to connect them to functions from within the view class.
# 
# The .ui layout files are converted to .py layout files when processed with pyuic or pyside-uic. 
# The .py view files can then import the relevant auto-generated classes from the .py layout files.
# 
# The view class(es) should contain the minimal code required to connect to the signals coming from the widgets in your layout. 
# View events can call and pass basic information to a method in the view class and onto a method in a controller class, where any logic should be. 
# 
# The view doesn't do much apart from link widget events to the relevant controller function, 
# and listen for changes in the model, which are emitted as Qt signals.

class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        # connect widgets to controller
        self._ui.spinBox_amount.valueChanged.connect(self._main_controller.change_amount)
        self._ui.pushButton_reset.clicked.connect(lambda: self._main_controller.change_amount(0))

        # listen for model event signals
        self._model.amount_changed.connect(self.on_amount_changed)
        self._model.even_odd_changed.connect(self.on_even_odd_changed)
        self._model.enable_reset_changed.connect(self.on_enable_reset_changed)

        # set a default value
        self._main_controller.change_amount(42)

    @pyqtSlot(int)
    def on_amount_changed(self, value):
        self._ui.spinBox_amount.setValue(value)

    @pyqtSlot(str)
    def on_even_odd_changed(self, value):
        self._ui.label_even_odd.setText(value)