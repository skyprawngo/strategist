# PySide6 module import
import sys

from gui.module_import import *

from gui.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.theme = "dafault"
        
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.setup_gui()
        self.ui.resize_grips()
    
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