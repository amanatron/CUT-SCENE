from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QSettings
from model.model import Model
from controllers.main_control import MainController
from views.mainwindow_view import MainView
#import qdarkstyle
import cutscene
import sys

# mvc_app.py would be responsible for instantiating each of the view, controllers, 
# and model(s) and passing references between them. This can be quite minimal:

class CutSceneApp(QApplication):

    def __init__(self, args):
        # Initialise
        super(CutSceneApp, self).__init__(args)
        
        # Initialise and Load settings
        self.settings = QSettings("AmanTrivedi", "CUTSCENE")

        # Styling
        #self.setStyle("Windows")
        # setup stylesheet
        #app.setStyleSheet(qdarkstyle.load_stylesheet_pyside2())
        # or in new API
        #self.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside2'))

        # Initalise Model, controllers, and views
        self.model = Model()
        self.mainController = MainController(self.model)
        self.mainView = MainView(self.model, self.mainController, self.settings)

        # Load Project from projectPath (first arg to program)
        if len(args) > 1:
            self.mainController.loadProject(args[1])        

        # Show window
        self.mainView.show()
        self.exec_()

if __name__ == "__main__":
    app = CutSceneApp(sys.argv)
    sys.exit(0)