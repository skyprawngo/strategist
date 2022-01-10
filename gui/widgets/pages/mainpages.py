from module.pyside6_module_import import *

from gui.widgets.pages.page_0.page_0 import Page_0
from gui.widgets.pages.page_1.page_1 import Page_1
from gui.widgets.pages.page_2 import Page_2
from gui.widgets.pages.page_3 import Page_3

from gui.themes.themes import Themes

class MainPages(QStackedWidget):
    def __init__(
        self,
        app_parent

    ):
        super().__init__()
        self._app_parent = app_parent
        self.setupUi()
        self.sig_n_slot()
        
    def sig_n_slot(self):
        
        pass
        
    def setupUi(self):
        
        themes = Themes()
        self.themes = themes.themes
        
        self.setObjectName("mainPages")
        self.setContentsMargins(0, 0, 0, 0)
        self.page_0_frame = QFrame()
        self.page_0_frame.setStyleSheet("background-color: none;")
        self.page_0_vlayout = QVBoxLayout(self.page_0_frame)
        self.page_0_vlayout.setContentsMargins(0, 0, 0, 0)
        self.page_0 = Page_0(
            app_parent = self._app_parent,
            bg_one = self.themes["app_color"]["bg_one"],
            bg_two = self.themes["app_color"]["bg_two"],
            bg_three = self.themes["app_color"]["bg_three"],
            
            color_one = self.themes["app_color"]["color_one"],
            color_two = self.themes["app_color"]["color_two"],
            color_three = self.themes["app_color"]["color_three"],
            color_red = self.themes["app_color"]["color_red2"]
        )
        self.page_0_vlayout.addWidget(self.page_0)
        self.addWidget(self.page_0_frame)
        
        self.page_1_frame = QFrame()
        self.page_1_vlayout = QVBoxLayout(self.page_1_frame)
        self.page_1_vlayout.setContentsMargins(0, 0, 0, 0)
        self.page_1 = Page_1(
            app_parent = self._app_parent,
            bg_one = self.themes["app_color"]["bg_one"],
            bg_two = self.themes["app_color"]["bg_two"],
            bg_three = self.themes["app_color"]["bg_three"],
            
            color_one = self.themes["app_color"]["color_one"],
            color_two = self.themes["app_color"]["color_two"],
            color_three = self.themes["app_color"]["color_three"],
            color_red = self.themes["app_color"]["color_red2"]
        )
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
