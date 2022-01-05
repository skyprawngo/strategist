from module.pyside6_module_import import *

from func.func_ccxt import Function_ccxt
from func.thread_ccxt import Thread_ccxt
from func.func_userdata import Function_Login
from gui.themes.load_item_path import Load_Item_Path

from gui.widgets.pages.page_0.walletkey_widget.btn_apikey_enter import Btn_Apikey_enter
from gui.widgets.check_box.check_box import Check_Box



class Walletkey_Widget(QWidget):
    clicked = Signal(object)
    
    def __init__(
        self,
        parent,
        app_parent,
        bg_one = "#e0e3ea",
        bg_two = "#f5f6fa",
        bg_three = "#fff",
        
        color_one = "#b9cefe",
        color_two = "#8aadff",
        color_three = "#6c98fe"
        ):
        super().__init__()
        self._parent = parent
        self._app_parent = app_parent
        self.bg_one = bg_one
        self.bg_two = bg_two
        self.bg_three = bg_three
        
        self.color_one = color_one
        self.color_two = color_two
        self.color_three = color_three
        self.setup_Ui()
        self.setup_thread()
        self.sig_n_slot()
        
    def apikey_return(self):
        self.lineedit_secretkey.setFocus()
    
    def remember_ckbox_pressed(self):
        if self.key_remember_ckbox.isChecked():
            if not self.key_remember_ckbox_istoggled:
                self.appear_warning_window()
            self.key_remember_ckbox_istoggled = True
        elif not self.key_remember_ckbox.isChecked():
            Function_Login.save_key(None, None)
            Function_Login.save_ckbox_remember_key(False)
            self.key_remember_ckbox_istoggled = False
    
    def appear_warning_window(self):
        self.warning_window = QWidget(self._parent)
        self.warning_window.setStyleSheet(f'''
            background-color: {self.bg_one}
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
        self.warning_label.setStyleSheet(f'''background-color: {self.bg_three}''')
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
        self.btn_yes.setStyleSheet(f'''
            background-color: #fb4646;
            font: bold 13px;
            color: {self.bg_three};
            height: 40px;
            border-radius: 10px;
        ''')
        self.btn_yes.clicked.connect(self.btn_yes_clicked)
        self.btn_hlayout.addWidget(self.btn_yes)
        
        self.btn_no = QPushButton()
        self.btn_no.setObjectName("btn_warning1_n")
        self.btn_no.setText("No, I don't")
        self.btn_no.setStyleSheet(f'''
            background-color: {self.bg_three};
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
        Function_Login.save_key(
            apikey = self.lineedit_apikey.text(),
            secretkey = self.lineedit_secretkey.text()
        )
        Function_Login.save_ckbox_remember_key(True)
        self.warning_window.close()
        pass
    
    def btn_no_clicked(self):
        self.clicked.emit(self.btn_no)
        Function_Login.save_key(None, None)
        Function_Login.save_ckbox_remember_key(False)
        self.key_remember_ckbox.setChecked(False)
        self.warning_window.close()
        pass
    
    def btn_key_enter_clicked(self):
        self.remember_ckbox_pressed()
        
        Function_ccxt.set_account(
            self.lineedit_apikey.text(),
            self.lineedit_secretkey.text()
        )
        balance = Function_ccxt.get_balance()
        if not balance:
            self.walletkey_glayout.addWidget(self.warning_correct_key_label, 3, 0, 1, 1)
            self.btn_key_enter.btn_istoggle_active = True
            self.btn_key_enter.changetoggleStyle(QEvent.MouseButtonPress)
        
        if self.btn_key_enter.btn_istoggle_active:
            self.lineedit_apikey.setEnabled(False)
            self.lineedit_secretkey.setEnabled(False)
        elif not self.btn_key_enter.btn_istoggle_active:
            self.lineedit_apikey.setEnabled(True)
            self.lineedit_secretkey.setEnabled(True)
        
        if balance:
            self.warning_correct_key_label.hide()
            self.clicked.emit(balance)
            pass
    
    def setup_thread(self):
        self.wallet_update = Thread_ccxt()
        pass
    
    def thread_operation(self):
        pass
    
    def thread_operation_completed(self):
        pass
    
    def sig_n_slot(self):
        self.lineedit_apikey.returnPressed.connect(self.apikey_return)
        self.lineedit_apikey.setText(Function_Login.load_key()[0])
        self.lineedit_secretkey.setText(Function_Login.load_key()[1])
        self.btn_key_enter.clicked.connect(self.btn_key_enter_clicked)
        self.btn_key_enter.clicked.connect(self.thread_operation)
        self.btn_key_enter.clicked.connect(self.thread_operation_completed)
        self.key_remember_ckbox.clicked.connect(self.remember_ckbox_pressed)
        self.key_remember_ckbox.setChecked(Function_Login.load_ckbox_remember_key())
        self.key_remember_ckbox_istoggled = Function_Login.load_ckbox_remember_key()
        pass

            
    def setup_Ui(self):
        self.walletkey_widget_vlayout = QVBoxLayout(self)
        self.walletkey_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        self.walletkey_widget_vlayout.setSpacing(0)
        self.walletkey_frame = QFrame()
        self.setStyleSheet(f"background-color: {self.bg_three};")
        
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
            background-color: {self.bg_two};
            border-radius: {self.lineedit_apikey.height()/3};
            font: 400 15px;
        ''')
        
        self.lineedit_secretkey = QLineEdit()
        self.lineedit_secretkey.setFixedHeight(50)
        self.lineedit_secretkey.setAlignment(Qt.AlignHCenter)
        self.lineedit_secretkey.setStyleSheet(f'''
            background-color: {self.bg_two};
            border-radius: {self.lineedit_secretkey.height()/3}px;
            font: 400 15px;
        ''')
        
        self.btn_key_enter = Btn_Apikey_enter(
            icon_file_path = Load_Item_Path().set_svg_icon_path("check.svg"),
            
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three
        )
        self.btn_key_enter.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.btn_key_enter.setFixedWidth(60)
        
        self.warning_correct_key_label = QLabel("Set Correct Key!")
        self.warning_correct_key_label.setAttribute(Qt.WA_TranslucentBackground)
        
        self.key_remember_ckbox = Check_Box(
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three
        )
        self.key_remember_ckbox.setText("Remember Key")
        self.key_remember_ckbox.setLayoutDirection(Qt.RightToLeft)
        
        self.walletkey_glayout.addWidget(self.walletkey_label,0, 0, 1, 1)
        self.walletkey_glayout.addWidget(self.lineedit_apikey,1, 0, 1, 1)
        self.walletkey_glayout.addWidget(self.lineedit_secretkey,2, 0, 1, 1)
        self.walletkey_glayout.addWidget(self.btn_key_enter,1, 1, 2, 1)
        self.walletkey_glayout.addWidget(self.key_remember_ckbox, 3, 0, 1, 2)
        
        self.walletkey_widget_vlayout.addWidget(self.walletkey_frame)
        