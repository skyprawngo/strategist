from module.pyside6_module_import import *

from gui.themes.theme_settings import Settings
from gui.themes.themes import Themes

from gui.themes.load_item_path import Load_Item_Path
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
            border-radius:{self.themes["login_window"]["radius"]}
        ''')
        self.login_layout = QVBoxLayout(self.login_frame)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setSpacing(50)
        self.login_layout.setAlignment(Qt.AlignCenter)
        
        self.login_logo_frame = QFrame()
        self.login_logo_frame.setFixedHeight(200)
        self.login_logo_vlayout = QVBoxLayout(self.login_logo_frame)
        self.login_logo_vlayout.setContentsMargins(0, 40, 0, 0)
        self.login_logo_vlayout.setSpacing(0)
        
        self.logo_svg_1 = QSvgWidget()
        self.logo_svg_1.setFixedSize(320, 80)
        self.logo_svg_1.load(Load_Item_Path().set_svg_image_path("logo_top_80_30.svg"))
        self.login_logo_vlayout.addWidget(self.logo_svg_1, alignment=Qt.AlignHCenter)
        
        self.logo_subtext = QLabel()
        self.logo_subtext.setText(self.theme_settings["title_text"])
        self.login_logo_vlayout.addWidget(self.logo_subtext, alignment=Qt.AlignHCenter)
        
        self.lineedit_frame = QFrame()
        self.lineedit_vlayout = QVBoxLayout(self.lineedit_frame)
        self.lineedit_vlayout.setAlignment(Qt.AlignHCenter)
        self.lineedit_vlayout.setSpacing(10)

        self.lineedit_id = QLineEdit()
        self.lineedit_id.setFixedSize(300, 50)
        self.lineedit_id.setAlignment(Qt.AlignHCenter)
        self.lineedit_id.setStyleSheet(f'''
            background-color: #ffffff;
            border-radius: {self.lineedit_id.height()/2};
            font: bold 15px;
        ''')
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        self.lineedit_password.setFixedSize(300, 50)
        self.lineedit_password.setAlignment(Qt.AlignHCenter)
        self.lineedit_password.setStyleSheet(f'''
            background-color: #ffffff;
            border-radius: {self.lineedit_password.height()/2};
            font: bold 15px;
        ''')
        
        self.btn_login_frame = QFrame()
        self.btn_login_vlayout = QVBoxLayout(self.btn_login_frame)
        self.btn_login_vlayout.setAlignment(Qt.AlignHCenter)
        self.btn_login = QPushButton()
        self.btn_login.setFixedSize(250, 60)
        self.btn_login.setStyleSheet(f'''
            background-color: {self.themes["app_color"]["bg_three"]};
            border-radius: {self.btn_login.height()/3};
        ''')
        self.btn_login.clicked.connect(self.login_completed)
        self.btn_login_vlayout.addWidget(self.btn_login)
        
        self.lineedit_vlayout.addWidget(self.lineedit_id)
        self.lineedit_vlayout.addWidget(self.lineedit_password)
        
        self.login_layout.addWidget(self.login_logo_frame)
        self.login_layout.addWidget(self.lineedit_frame)
        self.login_layout.addWidget(self.btn_login_frame)
        
        self.setCentralWidget(self.login_frame)
    
    def login_completed(self):
        self.hide()
        self._parent.show()