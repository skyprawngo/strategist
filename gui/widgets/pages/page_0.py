from module.pyside6_module_import import *
from gui.widgets.scroll_area.scroll_area import Scroll_Area
from gui.widgets.check_box.check_box import Check_Box


class Page_0(QWidget):
    clicked = Signal(object)
    def __init__(
        self
    ):
        super().__init__()
        self.setupUi()
    
    def apikey_return(self):
        self.lineedit_secretkey.setFocus()
    
    def remember_ckbox_pressed(self):
        if self.key_remember_ckbox.isChecked():
            self.appear_warning_window()
            pass
        pass
    
    def appear_warning_window(self):
        self.warning_window = QWidget(self)
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
        self.btn_no.setObjectName("btn_warning1_y")
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
    
    def setupUi(self):
        self.vlayout = QVBoxLayout(self)
        self.setStyleSheet('background-color: "#f7f7f7"')
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)
        
        self.scrollarea = Scroll_Area(self)
        self.scrollarea.setObjectName(u"scrollArea")
        self.scrollarea.setWidgetResizable(True)
        
        self.scrollarea_widget = QWidget()
        self.scrollarea_widget.setGeometry(QRect(0, 0, 763, 1000))
        self.scrollarea_widget.setMinimumSize(QSize(0, 1000))
        self.scrollarea_widget.setStyleSheet('''
            border-radius: 15px;
        ''')
        
        self.scrollarea_glayout = QGridLayout(self.scrollarea_widget)
        self.scrollarea_glayout.setContentsMargins(5, 0, 5, 0)
        
        self.walletkey_frame = QFrame()
        self.walletkey_frame.setStyleSheet("background-color: #fff;")
        self.walletkey_vlayout = QVBoxLayout(self.walletkey_frame)
        self.walletkey_vlayout.setContentsMargins(10, 10, 10, 5)
        self.walletkey_vlayout.setSpacing(5)
        
        self.walletkey_label = QLabel()
        self.walletkey_label.setStyleSheet('''
            padding-left: 5px;
            font: 12px;
        ''')
        self.walletkey_label.setText("Binance API Key")
        self.walletkey_vlayout.addWidget(self.walletkey_label, alignment=Qt.AlignLeft)
        
        self.lineedit_apikey = QLineEdit()
        self.lineedit_apikey.setFixedHeight(50)
        self.lineedit_apikey.setAlignment(Qt.AlignHCenter)
        self.lineedit_apikey.setStyleSheet(f'''
            background-color: "#f7f7f7";
            border-radius: {self.lineedit_apikey.height()/3};
            font: 400 15px;
        ''')
        self.lineedit_apikey.returnPressed.connect(self.apikey_return)
        self.walletkey_vlayout.addWidget(self.lineedit_apikey)
        
        self.lineedit_secretkey = QLineEdit()
        self.lineedit_secretkey.setFixedHeight(50)
        self.lineedit_secretkey.setAlignment(Qt.AlignHCenter)
        self.lineedit_secretkey.setStyleSheet(f'''
            background-color: "#f7f7f7";
            border-radius: {self.lineedit_secretkey.height()/3}px;
            font: 400 15px;
        ''')
        self.walletkey_vlayout.addWidget(self.lineedit_secretkey)
        
        self.key_remember_ckbox = Check_Box()
        self.key_remember_ckbox.setLayoutDirection(Qt.RightToLeft)
        self.key_remember_ckbox.setText("Remember Key")
        self.key_remember_ckbox.clicked.connect(self.remember_ckbox_pressed)
        self.walletkey_vlayout.addWidget(self.key_remember_ckbox)
        
        
        self.scrollarea_glayout.addWidget(self.walletkey_frame, 0, 0, 1, 3)
        
        self.distribution_frame = QFrame()
        self.distribution_frame.setStyleSheet("background-color: blue;")
        self.scrollarea_glayout.addWidget(self.distribution_frame, 0, 3, 1, 2)
        
        self.stock_chart_frame = QFrame()
        self.stock_chart_frame.setStyleSheet("background-color: lightgreen;")
        self.scrollarea_glayout.addWidget(self.stock_chart_frame, 0, 5, 3, 7)
        
        self.wallet_stock_frame = QFrame()
        self.wallet_stock_frame.setStyleSheet("background-color: lightgreen;")
        self.scrollarea_glayout.addWidget(self.wallet_stock_frame, 1, 0, 2, 5)
        
        
        self.frame2 = QFrame()
        self.frame2.setStyleSheet("background-color: lightblue;")
        self.scrollarea_glayout.addWidget(self.frame2, 3, 0)
        
        self.frame3 = QFrame()
        self.frame3.setStyleSheet("background-color: pink;")
        self.scrollarea_glayout.addWidget(self.frame3, 4, 0)
        
        self.scrollarea.setWidget(self.scrollarea_widget)
        
        self.vlayout.addWidget(self.scrollarea)
    