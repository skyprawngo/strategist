from module.pyside6_module_import import *

class Page_0(QWidget):
    def __init__(
        self
    ):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        self.vlayout = QVBoxLayout(self)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)
        self.widget1 = QWidget()
        self.widget1.setStyleSheet("background-color: lightgreen;")
        self.vlayout.addWidget(self.widget1)
        