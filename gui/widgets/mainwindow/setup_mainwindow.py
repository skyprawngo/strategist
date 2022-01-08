from module.pyside6_module_import import *

from gui.widgets.mainwindow.mainwindow import Ui_MainWindow
from gui.widgets.loginwindow.login_window import Login_Window
from gui.widgets.pages.mainpages import MainPages
from gui.widgets.tp_grips.tp_grips import TpGrips

class Setup_MainWindow:
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
    add_left_menus = [
        {
            "btn_id" : "btn_home",
            "icon_file_name" : "home.svg",
            "tooltip_text" : "Home",
            "btn_istoggle" : True,
            "btn_istoggle_active" : True,
            "btn_isactive" : False
        },
        {
            "btn_id" : "btn_chart",
            "icon_file_name" : "chat-arrow-grow.svg",
            "tooltip_text" : "Chart",
            "btn_istoggle" : True,
            "btn_istoggle_active" : False,
            "btn_isactive" : False
            
        },
        {
            "btn_id" : "btn_purchased",
            "icon_file_name" : "book.svg",
            "tooltip_text" : "Purchased",
            "btn_istoggle" : True,
            "btn_istoggle_active" : False,
            "btn_isactive" : False
        },
        {
            "btn_id" : "btn_shop",
            "icon_file_name" : "shopping-cart.svg",
            "tooltip_text" : "Shop",
            "btn_istoggle" : True,
            "btn_istoggle_active" : False,
            "btn_isactive" : False
        }
    ]
    
    def login_window_appear(self):
        self.login_window = Login_Window(self)
        self.login_window.show()
        
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.load_pages.page_0.walletkey_widget.sender() != None:
            # print(self.ui.load_pages.page_0.walletkey_widget.sender())
            return self.ui.load_pages.page_0.walletkey_widget.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()
            
           
    
    def setup_gui(self):

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        self.hide_grips = True
        self.left_grip = TpGrips(self, "left", self.hide_grips)
        self.right_grip = TpGrips(self, "right", self.hide_grips)
        self.top_grip = TpGrips(self, "top", self.hide_grips)
        self.bottom_grip = TpGrips(self, "bottom", self.hide_grips)
        self.top_left_grip = TpGrips(self, "top_left", self.hide_grips)
        self.top_right_grip = TpGrips(self, "top_right", self.hide_grips)
        self.bottom_left_grip = TpGrips(self, "bottom_left", self.hide_grips)
        self.bottom_right_grip = TpGrips(self, "bottom_right", self.hide_grips)
    
        self.ui.left_menu.add_menus(Setup_MainWindow.add_left_menus)
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        # self.ui.load_pages.page_0.walletkey_completed_signal.connect(self.btn_clicked)
        
        
        
        
    def resize_grips(self):
        self.left_grip.setGeometry(0, 15, 10, self.height()-10)
        self.right_grip.setGeometry(self.width() - 10, 15, 10, self.height()-10)
        self.top_grip.setGeometry(15, 0, self.width() - 10, 10)
        self.bottom_grip.setGeometry(15, self.height() - 10, self.width() - 30, 10)
        self.top_left_grip.setGeometry(0, 0, 15, 15)
        self.top_right_grip.setGeometry(self.width() - 15, 0, 15, 15)
        self.bottom_left_grip.setGeometry(0, self.height() - 15, 15, 15)
        self.bottom_right_grip.setGeometry(self.width() - 15, self.height() - 15, 15, 15)