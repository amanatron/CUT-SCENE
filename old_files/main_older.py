from PySide2.QtWidgets import QApplication

import frontend
import cutscene
import sys
import os

class CutSceneApp(QApplication):

  def __init__(self, args):
    super(CutSceneApp, self).__init__(args)
    if len(args) > 1:
        projectPath = args[1]
    else:
        projectPath = None

    self.mainWindow = frontend.MainWindow(projectPath=projectPath)
    self.mainWindow.show()
    self.exec_()

app = CutSceneApp(sys.argv)
sys.exit(0)