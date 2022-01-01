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
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.resize(
            self.theme_settings["login_size"][0],
            self.theme_settings["login_size"][1]
        )
        
        self.login_frame = QFrame()
        self.login_frame.setStyleSheet(f'''
            background-color:{self.themes["app_color"]["bg_two"]};
            border-radius:{self.themes["shape"]["login_window"]["radius"]}
        ''')
        self.login_layout = QVBoxLayout(self.login_frame)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setSpacing(0)
        
        self.login_label = QLabel()
        self.login_label.setFixedHeight(200)
        self.login_label.setStyleSheet("background-color:lightgreen;")
        self.login_layout.addWidget(self.login_label)
        
        self.pushButton2 = QPushButton("click me2")
        self.pushButton2.clicked.connect(self.login_completed)
        self.login_layout.addWidget(self.pushButton2)
        
        self.setCentralWidget(self.login_frame)
    
    def login_completed(self):
        self.hide()
        self._parent.show()