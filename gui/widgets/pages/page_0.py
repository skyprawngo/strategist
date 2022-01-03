from module.pyside6_module_import import *
from gui.widgets.scroll_area.scroll_area import Scroll_Area
from gui.widgets.check_box.check_box import Check_Box


class Page_0(QWidget):
    def __init__(
        self
    ):
        super().__init__()
        self.setupUi()
    
    def remember_key_pressed(self):
        if self.key_remember_ckbox.isChecked():
            pass
        print("asdf")
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
        
        self.walletkey_vlayout.addWidget(self.walletkey_label)
        
        self.label_apikey = QLineEdit()
        self.label_apikey.setFixedHeight(50)
        self.label_apikey.setAlignment(Qt.AlignHCenter)
        self.label_apikey.setStyleSheet(f'''
            background-color: "#f7f7f7";
            border-radius: {self.label_apikey.height()/3};
            font: 400 15px;
        ''')
        self.walletkey_vlayout.addWidget(self.label_apikey)
        
        self.label_secretkey = QLineEdit()
        self.label_secretkey.setFixedHeight(50)
        self.label_secretkey.setAlignment(Qt.AlignHCenter)
        self.label_secretkey.setStyleSheet(f'''
            background-color: "#f7f7f7";
            border-radius: {self.label_secretkey.height()/3}px;
            font: 400 15px;
        ''')
        self.walletkey_vlayout.addWidget(self.label_secretkey)
        
        self.key_remember_ckbox = Check_Box()
        self.key_remember_ckbox.setLayoutDirection(Qt.RightToLeft)
        self.key_remember_ckbox.setText("Remember Key")
        self.key_remember_ckbox.clicked.connect(self.remember_key_pressed)
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
    