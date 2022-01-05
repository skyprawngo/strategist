from module.pyside6_module_import import *

from func.func_ccxt import Function_ccxt
from gui.themes.load_item_path import Load_Item_Path

class Walletstock_Widget(QWidget):
    def __init__(
        self,
        parent,
        bg_one = "#e0e3ea",
        bg_two = "#f5f6fa",
        bg_three = "#fff",
        
        color_one = "#b9cefe",
        color_two = "#8aadff",
        color_three = "#6c98fe"
    ):
        super().__init__()
        self._parent = parent
        self.bg_one = bg_one
        self.bg_two = bg_two
        self.bg_three = bg_three
        
        self.color_one = color_one
        self.color_two = color_two
        self.color_three = color_three
        
        self.setup_Ui()
        self._parent.walletkey_completed_signal.connect(self.key_receiver)
        
    def key_receiver(self):
        print(Function_ccxt.wallet_balance)
        pass
    
    def setup_Ui(self):
        self.walletstock_widget_vlayout = QVBoxLayout(self)
        self.walletstock_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        self.walletstock_widget_vlayout.setSpacing(0)
        
        self.walletstock_frame = QFrame()
        self.walletstock_frame.setStyleSheet(f'''
            background-color: {self.bg_three}                   
        ''')
        
        self.walletstock_widget_vlayout.addWidget(self.walletstock_frame)
        
        pass