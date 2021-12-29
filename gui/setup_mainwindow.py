from module.pyside6_module_import import *

from gui.mainwindow import Ui_MainWindow

from gui.widgets.pygrips.py_grips import PyGrips

class Setup_MainWindow:
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    def setup_gui(self):

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.hide_grips = True
        self.left_grip = PyGrips(self, "left", self.hide_grips)
        self.right_grip = PyGrips(self, "right", self.hide_grips)
        self.top_grip = PyGrips(self, "top", self.hide_grips)
        self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
        self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
        self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
        self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
        self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)
    
    def resize_grips(self):
            self.left_grip.setGeometry(0, 15, 10, self.height()-10)
            self.right_grip.setGeometry(self.width() - 10, 15, 10, self.height()-10)
            self.top_grip.setGeometry(15, 0, self.width() - 10, 10)
            self.bottom_grip.setGeometry(15, self.height() - 10, self.width() - 30, 10)
            self.top_left_grip.setGeometry(0, 0, 15, 15)
            self.top_right_grip.setGeometry(self.width() - 15, 0, 15, 15)
            self.bottom_left_grip.setGeometry(0, self.height() - 15, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 15, self.height() - 15, 15, 15)