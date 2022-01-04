from module.pyside6_module_import import *
from func.func_ccxt import Function_ccxt
from func.func_userdata import Function_Login
from gui.themes.load_item_path import Load_Item_Path

from gui.themes.theme_settings import Settings
from gui.themes.themes import Themes

from gui.widgets.check_box.check_box import Check_Box

class Login_Window(QMainWindow):
    def __init__(
        self,
        app_parent
    ):
        super().__init__()
        self.app_parent = app_parent
        self.setupUi()
        
    def lineedit_enter(self):
        print(self.sender().objectName())
        if self.sender().objectName() == "login_id":
            self.lineedit_password.setFocus()
        
        elif self.sender().objectName() == "login_password":
            if self.login_remember_ckbox.isChecked():
                # Function_Login.save_login_id(self.lineedit_id.text())
                pass
            self.btn_login.mouseReleaseEvent(event=QEvent.MouseButtonRelease)
            pass
    
    def btn_login_clicked(self):
        Function_Login()
        self.close()
        self.app_parent.show()
        pass
           
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
            background-color:{self.themes["app_color"]["bg_one"]};
            border-radius:{self.themes["login_window"]["radius"]}
        ''')
        self.login_layout = QVBoxLayout(self.login_frame)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setSpacing(50)
        self.login_layout.setAlignment(Qt.AlignCenter)
        
        self.login_logo_frame = QFrame()
        self.login_logo_frame.setFixedHeight(200)
        self.login_logo_vlayout = QVBoxLayout(self.login_logo_frame)
        self.login_logo_vlayout.setContentsMargins(50, 40, 50, 0)
        self.login_logo_vlayout.setSpacing(0)
        
        self.logo_svg_1 = QSvgWidget()
        self.logo_svg_1.setFixedSize(320, 80)
        self.logo_svg_1.load(Load_Item_Path().set_svg_image_path("logo_top_90_30.svg"))
        self.login_logo_vlayout.addWidget(self.logo_svg_1, alignment=Qt.AlignHCenter)
        
        self.logo_subtext = QLabel()
        self.logo_subtext.setText(self.theme_settings["title_text"])
        self.login_logo_vlayout.addWidget(self.logo_subtext, alignment=Qt.AlignHCenter)

        self.logo_subtext_1 = QLabel()
        self.logo_subtext_1.setText('''
            This Window is just emitation log-in window,
                   So Press "Log in" Button and go ahead
        ''')
        self.login_logo_vlayout.addWidget(self.logo_subtext_1, alignment=Qt.AlignRight)
        
        self.lineedit_frame = QFrame()
        self.lineedit_vlayout = QVBoxLayout(self.lineedit_frame)
        self.lineedit_vlayout.setAlignment(Qt.AlignHCenter)
        self.lineedit_vlayout.setSpacing(10)

        self.lineedit_id = QLineEdit()
        self.lineedit_id.setObjectName("login_id")
        self.lineedit_id.setFixedSize(300, 50)
        self.lineedit_id.setAlignment(Qt.AlignHCenter)
        self.lineedit_id.setStyleSheet(f'''
            background-color: {self.themes["app_color"]["bg_three"]};
            border-radius: {self.lineedit_id.height()/2};
            font: bold 15px;
        ''')
        self.lineedit_id.returnPressed.connect(self.lineedit_enter)
        
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setObjectName("login_password")
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        self.lineedit_password.setFixedSize(300, 50)
        self.lineedit_password.setAlignment(Qt.AlignHCenter)
        self.lineedit_password.setStyleSheet(f'''
            background-color: {self.themes["app_color"]["bg_three"]};
            border-radius: {self.lineedit_password.height()/2};
            font: bold 15px;
        ''')
        self.lineedit_password.returnPressed.connect(self.btn_login_clicked)
        
        self.login_remember_ckbox = Check_Box()
        self.login_remember_ckbox.setText("Remember Login Id and Password")

        self.btn_login_frame = QFrame()
        self.btn_login_vlayout = QVBoxLayout(self.btn_login_frame)
        self.btn_login_vlayout.setAlignment(Qt.AlignHCenter)
        
        self.btn_login = Btn_Login(
            self.app_parent,
            parent = self,
            
            bg_color = self.themes["app_color"]["color_two"],
            bg_color_hover = self.themes["app_color"]["color_three"],
            bg_color_pressed = self.themes["app_color"]["color_four"]
        )
        self.btn_login.released.connect(self.btn_login_clicked)
        
        self.sign_in_label = QLabel()
        self.sign_in_label.setText("Sign in")
        
        self.btn_login_vlayout.addWidget(self.btn_login)
        self.btn_login_vlayout.addWidget(self.sign_in_label, alignment=Qt.AlignHCenter)
        
        self.lineedit_vlayout.addWidget(self.lineedit_id)
        self.lineedit_vlayout.addWidget(self.lineedit_password)
        self.lineedit_vlayout.addWidget(self.login_remember_ckbox, alignment=Qt.AlignHCenter)
        
        self.login_layout.addWidget(self.login_logo_frame)
        self.login_layout.addWidget(self.lineedit_frame)
        self.login_layout.addWidget(self.btn_login_frame)
        
        self.setCentralWidget(self.login_frame)
        
    
    
    
        
class Btn_Login(QPushButton):
    def __init__(
        self,
        app_parent,
        parent,
        bg_color,
        bg_color_hover,
        bg_color_pressed
    ):
        super().__init__()
        self.app_parent = app_parent
        self._parent = parent
        self.bg_color = bg_color
        self.bg_color_hover = bg_color_hover
        self.bg_color_pressed = bg_color_pressed
        
        self.set_bg_color = bg_color
        
        self.setFixedSize(250, 60)
        self.btn_login_vlayout = QVBoxLayout(self)
        self.login_svg_1 = QSvgWidget()
        self.login_svg_1.setFixedSize(100, 30)
        self.login_svg_1.load(Load_Item_Path().set_svg_image_path("login_80_30.svg"))
        self.btn_login_vlayout.addWidget(self.login_svg_1, alignment=Qt.AlignHCenter)
        self.btn_style(self.bg_color)
        
    def enterEvent(self, event):
        self.btn_style(self.bg_color_hover)
    
    def leaveEvent(self, event):
        self.btn_style(self.bg_color)
    
    def mousePressEvent(self, event):
        self.btn_style(self.bg_color_pressed)

    def mouseReleaseEvent(self, event):
        self.btn_style(self.bg_color)
        self.released.emit()
        
    def btn_style(self, bg_color):
        self.set_bg_color = bg_color
        self.setStyleSheet(f'''
            background-color: {self.set_bg_color};
            border-radius: {self.height()/2.5};
        ''')
        