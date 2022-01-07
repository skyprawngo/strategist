from func.thread_ccxt import Thread_getbalance
from module.pyside6_module_import import *

from func.func_ccxt import Function_ccxt
from func.func_exchangerate import Function_exchangerate
from gui.themes.load_item_path import Load_Item_Path
from gui.widgets.tp_table_widget.tp_table_widget import Tp_Table_Widget

class Walletstock_Widget(QWidget):
    ani_signal = Signal()
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
        self._parent.walletkey_widget.thread_operation_completed_signal.connect(self.key_receiver)
        self.ani_signal.connect(self.appear_animation)
        
    def key_receiver(self):
        # self.walletstock_table.horizontalHeader().setVisible(True)
        i = 0
        total_USD = 0
        total_KRW = 0
        
        for coin_name in Function_ccxt.wallet_balance:
            self.walletstock_table.setRowHeight(i, 28)
            self.walletstock_table.insertRow(i) # Insert row

            self.define = RainBow_Label(i)
            
            self.coin_name_item = QTableWidgetItem()
            self.coin_name_item.setText(coin_name)

            self.USD_value_item = QTableWidgetItem()
            self.USD_value = Function_ccxt.get_price_USD(coin_name)
            self.USD_value_item.setText(str(self.USD_value))

            self.coin_amount_item = QTableWidgetItem()
            self.coin_amount = Function_ccxt.wallet_balance[coin_name]["total"]
            self.coin_amount_item.setText(str(round(self.coin_amount,3)))
            
            self.coin_to_USD_item = QTableWidgetItem()
            self.coin_to_USD = self.coin_amount * Function_ccxt.get_price_USD(coin_name)
            self.coin_to_USD_item.setText(str(round(self.coin_to_USD,2)))
            
            self.coin_to_KRW_item = QTableWidgetItem()
            self.coin_to_KRW = self.coin_to_USD * int(Function_exchangerate.USD_to_KRW())
                
            self.coin_to_KRW_item.setText(str(round(self.coin_to_KRW, 0)))
            
            self.walletstock_table.setCellWidget(i, 0, self.define)
            self.walletstock_table.setItem(i, 1, self.coin_name_item)
            self.walletstock_table.setItem(i, 2, self.USD_value_item) 
            self.walletstock_table.setItem(i, 3, self.coin_amount_item) 
            self.walletstock_table.setItem(i, 4, self.coin_to_USD_item)
            self.walletstock_table.setItem(i, 5, self.coin_to_KRW_item)
            i += 1
            total_USD += self.coin_to_USD
            total_KRW += self.coin_to_KRW
        
        self.walletstock_table.insertRow(i)
        self.walletstock_table.setItem(i, 3, QTableWidgetItem(str("Total")))
        self.walletstock_table.setItem(i, 4, QTableWidgetItem(str(round(total_USD, 0))))
        self.walletstock_table.setItem(i, 5, QTableWidgetItem(str(round(total_KRW, 0))))
        
        self.walletstock_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.walletstock_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self._height = (i+1) * self.walletstock_table.rowHeight(0)
        self.ani_signal.emit()
        
    def appear_animation(self):
        # CREATE ANIMATION
        self.animation = QPropertyAnimation(self.ani_frame, b"pos")
        self.animation.stop()
        
        self.animation.setStartValue(QPoint(0, -self.walletstock_frame.height()))
        self.animation.setEndValue(QPoint(0, 0))
            
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(1500)
        self.animation.start()
        self.ani_frame.show()
        pass
    
    def setup_Ui(self):
        self.walletstock_widget_vlayout = QVBoxLayout(self)
        self.walletstock_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        self.walletstock_widget_vlayout.setSpacing(0)
        
        self.walletstock_frame = QFrame()
        self.walletstock_frame.setStyleSheet(f'''background-color: {self.bg_three}''')
        self.walletstock_vlayout = QVBoxLayout(self.walletstock_frame)
        
        self.ani_frame = QFrame()
        self.ani_frame.hide()
        self.ani_vlayout = QVBoxLayout(self.ani_frame)
        self.ani_frame.move(self.walletstock_frame.pos().x(), self.walletstock_frame.pos().y() -self.walletstock_frame.height())
        
        self.walletstock_table = Tp_Table_Widget(
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three,
        )
        self.walletstock_table.setObjectName("wallettable")
        self.walletstock_table.setEnabled(False)
        
        self.walletstock_table.setColumnCount(6)
        self.walletstock_table.verticalHeader().setVisible(False)
        self.walletstock_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.walletstock_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.walletstock_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.column_1 = QTableWidgetItem()
        self.column_1.setTextAlignment(Qt.AlignCenter)
        self.column_1.setText("")

        self.column_2 = QTableWidgetItem()
        self.column_2.setTextAlignment(Qt.AlignVCenter)
        self.column_2.setText("  Coin")

        self.column_3 = QTableWidgetItem()
        self.column_3.setTextAlignment(Qt.AlignVCenter)
        self.column_3.setText("  Price(USD)")

        self.column_4 = QTableWidgetItem()
        self.column_4.setTextAlignment(Qt.AlignVCenter)
        self.column_4.setText("  Amount")
       
        self.column_5 = QTableWidgetItem()
        self.column_5.setTextAlignment(Qt.AlignVCenter)
        self.column_5.setText("  Value(USD)")
        
        self.column_6 = QTableWidgetItem()
        self.column_6.setTextAlignment(Qt.AlignVCenter)
        self.column_6.setText("  Value(KRW)")
        
        self.walletstock_table.setHorizontalHeaderItem(0, self.column_1)
        self.walletstock_table.setHorizontalHeaderItem(1, self.column_2)
        self.walletstock_table.setHorizontalHeaderItem(2, self.column_3)
        self.walletstock_table.setHorizontalHeaderItem(3, self.column_4)
        self.walletstock_table.setHorizontalHeaderItem(4, self.column_5)
        self.walletstock_table.setHorizontalHeaderItem(5, self.column_6)
        
        self.ani_vlayout.addWidget(self.walletstock_table)
        self.walletstock_vlayout.addWidget(self.ani_frame)
        self.walletstock_widget_vlayout.addWidget(self.walletstock_frame)

        

        
        
class RainBow_Label(QLabel):
    rainbow = ["red", "orange", "yellow", "lightgreen", "darkgreen", "blue", "navy","purple", "violet", "pink", "lightblue", "darkgray"]
    def __init__(
        self,
        order
    ):
        super().__init__()
        self.order = order
        self.setFixedSize(10, 20)
    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(self.rainbow[self.order]))
        painter.drawEllipse(0, 10, 10, 10)
        painter.end()
        
