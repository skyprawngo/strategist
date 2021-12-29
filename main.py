# PySide6 module import
import sys

from module.pyside6_module_import import *

from gui.mainwindow import Ui_MainWindow
from gui.setup_mainwindow import Setup_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.theme = "dafault"
        
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        Setup_MainWindow.setup_gui(self)
    
    def resizeEvent(self, event):
        Setup_MainWindow.resize_grips(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()