from module.pyside6_module_import import *

from gui.widgets.pages.page_0 import Page_0
from gui.widgets.pages.page_1 import Page_1
from gui.widgets.pages.page_2 import Page_2
from gui.widgets.pages.page_3 import Page_3

class MainPages(QStackedWidget):
    def __init__(
        self

    ):
        super().__init__()
        self.setupUi()
    
    def page_0_setting(self):
        print(self.page_0.sender().objectName())
        pass
        
    def setupUi(self):
        self.setObjectName("mainPages")
        self.setContentsMargins(0, 0, 0, 0)
        
        self.page_0_frame = QFrame()
        self.page_0_vlayout = QVBoxLayout(self.page_0_frame)
        self.page_0_vlayout.setContentsMargins(0, 0, 0, 0)
        self.page_0 = Page_0()
        self.page_0.clicked.connect(self.page_0_setting)
        self.page_0_vlayout.addWidget(self.page_0)
        self.addWidget(self.page_0_frame)
        
        self.page_1_frame = QFrame()
        self.page_1_frame.setStyleSheet("background-color: lightblue")
        self.page_1_vlayout = QVBoxLayout(self.page_1_frame)
        self.page_1 = Page_1()
        self.page_1_vlayout.addWidget(self.page_1)
        self.addWidget(self.page_1_frame)
        
        self.page_2_frame = QFrame()
        self.page_2_frame.setStyleSheet("background-color: lightblue")
        self.page_2_vlayout = QVBoxLayout(self.page_2_frame)
        self.page_2 = Page_2()
        self.page_2_vlayout.addWidget(self.page_2)
        self.addWidget(self.page_2_frame)
        
        self.page_3_frame = QFrame()
        self.page_3_frame.setStyleSheet("background-color: lightblue")
        self.page_3_vlayout = QVBoxLayout(self.page_3_frame)
        self.page_3 = Page_3()
        self.page_3_vlayout.addWidget(self.page_3)
        self.addWidget(self.page_3_frame)
        
        QMetaObject.connectSlotsByName(self)
