from module.pyside6_module_import import *

from gui.themes.theme_settings import Settings
from gui.themes.themes import Themes
from gui.themes.theme_switch import Theme_Switch

from gui.widgets.pywindow.pywindow import PyWindow

class Login_Window(QMainWindow):
    def __init__(
        self,
        parent
    ):
        super().__init__()
        self._parent = parent
        self.setupUi()
        
    def setupUi(self):
            # Load Settings
        theme_settings = Settings()
        self.theme_settings = theme_settings.settings
            # Load Themes
        themes = Themes()
        self.themes = themes.themes
        
        self.resize(
            self.theme_settings["login_size"][0],
            self.theme_settings["login_size"][1]
        )
        
        self.login_Frame = QFrame()
        self.login_layout = QVBoxLayout(self.login_Frame)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setSpacing(0)
        
        self.login_label = QLabel()
        self.login_label.setStyleSheet("background-color:lightgreen;")
        self.login_layout.addWidget(self.login_label)
        
        self.pushButton2 = QPushButton("click me2")
        self.pushButton2.clicked.connect(self.off_pushButton_clicked)
        self.login_layout.addWidget(self.pushButton2)
        
        self.setCentralWidget(self.login_Frame)
    
    def off_pushButton_clicked(self):
        self.hide()
        self._parent.show()