from module.pyside6_module_import import *

from func.func_ccxt import Function_ccxt
from gui.themes.load_item_path import Load_Item_Path
from gui.widgets.tp_table_widget.tp_table_widget import Tp_Table_Widget

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
        i = 0
        for coin_name in Function_ccxt.wallet_balance:
            
            self.walletstock_table.insertRow(i) # Insert row
            self.walletstock_table.setCellWidget(i, 0, RainBow_Label(i))
            self.coin_name = QTableWidgetItem()
            self.coin_name.setText(coin_name)
            # self.coin_name.setTextAlignment(Qt.AlignTop)
            self.walletstock_table.setItem(i, 1, self.coin_name)
            self.walletstock_table.setItem(i, 2, QTableWidgetItem(str("Wanderson"))) # Add name
            self.walletstock_table.setItem(i, 3, QTableWidgetItem(str("vfx_on_fire_" + str(i)))) # Add nick
            self.pass_text = QTableWidgetItem()
            self.pass_text.setTextAlignment(Qt.AlignCenter)
            self.pass_text.setText("12345" + str(i))
            self.walletstock_table.setItem(i, 4, self.pass_text) # Add pass
            self.walletstock_table.setRowHeight(i, 22)
            
            # self.walletstock_table.setSpan(i+1, 0, 1, 4)
            i += 1
        
        
        pass
    
    def setup_Ui(self):
        self.walletstock_widget_vlayout = QVBoxLayout(self)
        self.walletstock_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        self.walletstock_widget_vlayout.setSpacing(0)
        
        self.walletstock_frame = QFrame()
        self.walletstock_frame.setStyleSheet('''background-color: #fff''')
        self.walletstock_vlayout = QVBoxLayout(self.walletstock_frame)
        
        self.walletstock_table = Tp_Table_Widget()
        self.walletstock_table.setEnabled(False)
        
        self.walletstock_table.setColumnCount(3)
        self.walletstock_table.verticalHeader().setVisible(False)
        self.walletstock_table.horizontalHeader().setVisible(False)
        self.walletstock_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.walletstock_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.walletstock_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.walletstock_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.walletstock_vlayout.addWidget(self.walletstock_table)
        self.walletstock_widget_vlayout.addWidget(self.walletstock_frame)

        

        
        
class RainBow_Label(QLabel):
    rainbow = ["red", "orange", "yellow", "lightgreen", "darkgreen", "blue", "navy","purple", "violet", "pink", "lightblue", "darkgray"]
    def __init__(
        self,
        order
    ):
        super().__init__()
        self.order = order
        self.setFixedSize(15, 15)
    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(self.rainbow[self.order]))
        painter.drawEllipse(0, 5, 10, 10)
        painter.end()
        
