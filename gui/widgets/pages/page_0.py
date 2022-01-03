from module.pyside6_module_import import *
from gui.widgets.scroll_area.scroll_area import Scroll_Area

class Page_0(QWidget):
    def __init__(
        self
    ):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.vlayout = QVBoxLayout(self)
        self.setStyleSheet('background-color: "#fff"')
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)
        self.scrollarea = Scroll_Area()
        self.scrollarea_frame = QFrame()
        self.scrollarea_frame.setStyleSheet('background-color: darkgray')
        self.scrollarea_frame.setFixedHeight(1000)
        self.scrollarea_glayout = QGridLayout(self.scrollarea_frame)
        
        self.frame1 = QFrame()
        self.frame1.setStyleSheet("background-color: red;")
        self.scrollarea_glayout.addWidget(self.frame1, 0, 0)
        
        self.frame2 = QFrame()
        self.frame2.setStyleSheet("background-color: blue;")
        self.scrollarea_glayout.addWidget(self.frame2, 1, 0)
        
        self.scrollarea.setWidget(self.scrollarea_frame)
        self.vlayout.addWidget(self.scrollarea)
        