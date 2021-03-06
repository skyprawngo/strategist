from module.pyside6_module_import import *

from func.thread_ccxt import Thread_setKey
from func.func_userdata import Function_DataIO
from gui.themes.load_item_path import Load_Item_Path

from gui.widgets.pages.page_0.walletkey_widget.btn_apikey_enter import Btn_Apikey_enter
from gui.widgets.tp_pushbutton.tp_pushbutton import Tp_PushButton
from gui.widgets.tp_check_box.tp_check_box import Tp_Check_Box



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
        color_three = "#6c98fe",
        color_red = "#fb4646"
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
        self.color_red = color_red
        self.setup_Ui()
        self.setup_thread()
        self.sig_n_slot()
    
    def remember_ckbox_pressed(self):
        if self.key_remember_ckbox.isChecked():
            if not self.key_remember_ckbox_istoggled:
                self.appear_warning_window()
                self.key_remember_ckbox_istoggled = True
        elif not self.key_remember_ckbox.isChecked():
            Function_DataIO.save_AppData("apikey", None)
            Function_DataIO.save_AppData("secret", None)
            Function_DataIO.save_local_parameter("key_save_ckbox", False)
            self.key_remember_ckbox_istoggled = False
    
    def appear_warning_window(self):
        self.warning_window_widget = QWidget(self._parent)
        self.warning_window_widget.setAttribute(Qt.WA_TranslucentBackground)
        self.warning_window_widget.resize(350, 210)
        self.warning_window_widget.move(100, 100)
        self.warning_window_layout = QVBoxLayout(self.warning_window_widget)
        
        self.warning_window_frame = QFrame()
        self.warning_window_frame.setStyleSheet(f'''
            background-color: {self.bg_one}
        ''')
        self.warning_window_vlayout = QVBoxLayout(self.warning_window_frame)
        
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
            background-color: {self.color_red};
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
        self.warning_window_layout.addWidget(self.warning_window_frame, alignment=Qt.AlignCenter)
        self.warning_window_widget.show()
        pass
    
    def btn_yes_clicked(self):
        Function_DataIO.save_AppData("apikey", self.lineedit_apikey.text())
        Function_DataIO.save_AppData("secret", self.lineedit_secretkey.text())
        Function_DataIO.save_local_parameter("key_save_ckbox", True)
        self.warning_window_widget.close()
        pass
    
    def btn_no_clicked(self):
        Function_DataIO.save_AppData("apikey", None)
        Function_DataIO.save_AppData("secret", None)
        Function_DataIO.save_local_parameter("key_save_ckbox", False)
        self.key_remember_ckbox.setChecked(False)
        self.warning_window_widget.close()
        pass
    
    def btn_keyenter_on(self):
        self.remember_ckbox_pressed()
        if not self.thread_setkey.isRunning():
            self.lineedit_apikey.setEnabled(False)
            self.lineedit_secretkey.setEnabled(False)
            
            self.thread_setkey.start()
            self.btn_keyenter.set_toggled(True)
            self.clicked.emit(self.btn_keyenter)
    
    def btn_keyenter_off(self):
        self.lineedit_apikey.setEnabled(True)
        self.lineedit_secretkey.setEnabled(True)
    
    def sig_n_slot(self):
        appdata = Function_DataIO.load_AppData()
        self.lineedit_apikey.setText(appdata["apikey"])
        self.lineedit_apikey.returnPressed.connect(self.lineedit_secretkey.setFocus())
        self.lineedit_secretkey.setText(appdata["secret"])
        
        self.key_remember_ckbox_istoggled = Function_DataIO.load_local_parameter()["key_save_ckbox"]
        self.key_remember_ckbox.setChecked(self.key_remember_ckbox_istoggled)
        self.key_remember_ckbox.clicked.connect(self.remember_ckbox_pressed)
        self.btn_keyenter._on.connect(self.btn_keyenter_on)
        self.btn_keyenter._off.connect(self.btn_keyenter_off)
        
    def setup_thread(self):
        self.thread_setkey = Thread_setKey(
            parent = self,
            app_parent = self._app_parent
        )
        
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
        
        self.btn_keyenter = Tp_PushButton(
            parent = self,
            app_parent = self._app_parent,
            btn_id = "btn_apikey_enter",
            
            icon_file_path = Load_Item_Path().set_svg_icon_path("check.svg"),
            icon_size = [35, 35],
            
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three,
            
            is_toggle_btn = True
        )
        self.btn_keyenter.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.btn_keyenter.setFixedWidth(60)
        
        self.warning_correct_key_label = QLabel("Set Correct Key!")
        self.warning_correct_key_label.setAttribute(Qt.WA_TranslucentBackground)
        
        self.key_remember_ckbox = Tp_Check_Box(
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
        self.walletkey_glayout.addWidget(self.btn_keyenter,1, 1, 2, 1)
        self.walletkey_glayout.addWidget(self.key_remember_ckbox, 3, 0, 1, 2)
        
        self.walletkey_widget_vlayout.addWidget(self.walletkey_frame)
        