from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile, QIODevice, QStringListModel, QSettings
import cutscene
import sys

class CutSceneApp(QApplication):

    def __init__(self, args):
        # Initialise
        super(CutSceneApp, self).__init__(args)
        # Load Project from projectPath (first arg to program)
        if len(args) > 1:
            self.projectPath = args[1]
            self.project = cutscene.loadProject(self.projectPath)
        else:
            self.project = None
        
        # Initialise and Load settings
        self.settings = QSettings("AmanTrivedi", "CUTSCENE")

        # Load ui window
        ui_file_name = "frontend/mainwindow.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)
        loader = QUiLoader()
        self.mainWindow = loader.load(ui_file)
        ui_file.close()
        if not self.mainWindow:
            print(loader.errorString())
            sys.exit(-1)

        # Restore window geometry if it's saved in settings
        if any(self.settings.value(x) is None for x in ["geometry", "windowState"]):
            qtRectangle = QRect(0, 0, *defaultWindowSize)
            centerPoint = QDesktopWidget().availableGeometry().center()
            qtRectangle.moveCenter(centerPoint)
            self.mainWindow.setGeometry(qtRectangle)
        else:
            self.mainWindow.restoreGeometry(self.settings.value("geometry"))
            self.mainWindow.restoreState(self.settings.value("windowState"))

        # Show window
        self.mainWindow.show()
        self.exec_()

if __name__ == "__main__":
    app = CutSceneApp(sys.argv)
    sys.exit(0)