from module.pyside6_module_import import *

from gui.widgets.pages.page_0.btn_apikey_enter import Btn_Apikey_enter
from gui.widgets.check_box.check_box import Check_Box

from gui.themes.load_item_path import Load_Item_Path


class Walletkey_Widget(QWidget):
    clicked = Signal(object)
    
    def __init__(
        self,
        parent
        ):
        super().__init__()
        self._parent = parent
        self.setup_Ui()
        
    def apikey_return(self):
        self.lineedit_secretkey.setFocus()
    
    def remember_ckbox_pressed(self):
        if self.key_remember_ckbox.isChecked():
            self.appear_warning_window()
            pass
        pass
    
    def appear_warning_window(self):
        self.warning_window = QWidget(self._parent)
        self.warning_window.setStyleSheet('''
            background-color: #eaebec
        ''')
        self.warning_window.resize(350, 200)
        self.warning_window.move(100, 100)
        self.warning_window_vlayout = QVBoxLayout(self.warning_window)
        
        self.warning_title = QLabel()
        self.warning_title.setStyleSheet('''
            font: bold 14px;
        ''')
        self.warning_title.setText("WARNING")
        self.warning_window_vlayout.addWidget(self.warning_title, alignment=Qt.AlignHCenter)
        self.warning_label = QLabel()
        self.warning_label.setContentsMargins(10, 10, 10, 10)
        self.warning_label.setStyleSheet('''background-color: "#fff"''')
        self.warning_label.setWordWrap(True)
        self.warning_label.setText('''Strategist don't collect your API Key (Of course), but It isn't recommendable for you to Remembering API Key in your PC. It can target your wallet to be hacked. And Strategist do not GUARANTEE against loss of your wallet if your computer is hacked. Are you sure to remembering API Key?''')
        self.warning_window_vlayout.addWidget(self.warning_label)
        
        self.btn_frame = QFrame()
        self.btn_hlayout = QHBoxLayout(self.btn_frame)
        self.btn_hlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_hlayout.setSpacing(10)
        
        self.btn_yes = QPushButton()
        self.btn_yes.setObjectName("btn_warning1_y")
        self.btn_yes.setText("Yes. I Remember Key")
        self.btn_yes.setStyleSheet('''
            background-color: #8b0e0e;
            font: bold 13px;
            color: #fff;
            height: 40px;
            border-radius: 10px;
        ''')
        self.btn_yes.clicked.connect(self.btn_yes_clicked)
        self.btn_hlayout.addWidget(self.btn_yes)
        
        self.btn_no = QPushButton()
        self.btn_no.setObjectName("btn_warning1_n")
        self.btn_no.setText("No, I don't")
        self.btn_no.setStyleSheet('''
            background-color: #fff;
            font: bold 13px;
            height: 40px;
            border-radius: 10px;
        ''')
        self.btn_no.clicked.connect(self.btn_no_clicked)
        self.btn_hlayout.addWidget(self.btn_no)
        
        
        self.warning_window_vlayout.addWidget(self.btn_frame)
        self.warning_window.show()
        pass
    
    def btn_yes_clicked(self):
        self.clicked.emit(self.btn_yes)
        self.warning_window.close()
        pass
    
    def btn_no_clicked(self):
        self.clicked.emit(self.btn_no)
        self.key_remember_ckbox.setChecked(False)
        self.warning_window.close()
        pass
    
    def btn_key_enter_clicked(self):
        self.clicked.emit(self.btn_key_enter)
        
        print("asdf")
        pass
    
    def setup_Ui(self):
        self.walletkey_widget_vlayout = QVBoxLayout(self)
        self.walletkey_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        self.walletkey_widget_vlayout.setSpacing(0)
        self.walletkey_frame = QFrame()
        self.setStyleSheet("background-color: #fff;")
        self.walletkey_glayout = QGridLayout(self.walletkey_frame)
        self.walletkey_glayout.setContentsMargins(10, 10, 10, 5)
        self.walletkey_glayout.setSpacing(5)
        
        self.walletkey_label = QLabel()
        self.walletkey_label.setStyleSheet('''
            padding-left: 5px;
            font: 12px;
        ''')
        self.walletkey_label.setText("Binance API Key")
        
        self.lineedit_apikey = QLineEdit()
        self.lineedit_apikey.setFixedHeight(50)
        self.lineedit_apikey.setAlignment(Qt.AlignHCenter)
        self.lineedit_apikey.setStyleSheet(f'''
            background-color: "#f7f7f7";
            border-radius: {self.lineedit_apikey.height()/3};
            font: 400 15px;
        ''')
        self.lineedit_apikey.returnPressed.connect(self.apikey_return)
        
        self.lineedit_secretkey = QLineEdit()
        self.lineedit_secretkey.setFixedHeight(50)
        self.lineedit_secretkey.setAlignment(Qt.AlignHCenter)
        self.lineedit_secretkey.setStyleSheet(f'''
            background-color: "#f7f7f7";
            border-radius: {self.lineedit_secretkey.height()/3}px;
            font: 400 15px;
        ''')
        
        self.btn_key_enter = Btn_Apikey_enter(
            icon_file_path = Load_Item_Path().set_svg_icon_path("check.svg"),
        )
        self.btn_key_enter.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.btn_key_enter.setFixedWidth(60)
        self.btn_key_enter.clicked.connect(self.btn_key_enter_clicked)
        
        self.key_remember_ckbox = Check_Box()
        self.key_remember_ckbox.setLayoutDirection(Qt.RightToLeft)
        self.key_remember_ckbox.setText("Remember Key")
        self.key_remember_ckbox.clicked.connect(self.remember_ckbox_pressed)
        
        self.walletkey_glayout.addWidget(self.walletkey_label,0, 0, 1, 1)
        self.walletkey_glayout.addWidget(self.lineedit_apikey,1, 0, 1, 1)
        self.walletkey_glayout.addWidget(self.lineedit_secretkey,2, 0, 1, 1)
        self.walletkey_glayout.addWidget(self.btn_key_enter,1, 1, 2, 1)
        self.walletkey_glayout.addWidget(self.key_remember_ckbox, 3, 0, 1, 2)
        
        self.walletkey_widget_vlayout.addWidget(self.walletkey_frame)
        