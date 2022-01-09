from func.thread_ccxt import Thread_getBalance
from module.pyside6_module_import import *

from func.func_ccxt import Function_ccxt
from func.func_exchangerate import Function_exchangerate
from gui.themes.load_item_path import Load_Item_Path
from gui.widgets.tp_table_widget.tp_table_widget import Tp_Table_Widget

class Walletstock_Widget(QWidget):
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
        
    def key_received(self):
        if not self.thread_getbalance.isRunning():
            self.thread_getbalance.start()
        
    def organize_table(self):   
        i = 0
        total_USD = 0
        total_KRW = 0
        df_balance = self.thread_getbalance.df_balance.loc["total"]
        df_balance = df_balance.drop("timestamp")
        datetime = df_balance.pop("datetime")
        print(df_balance.loc["ETH"])
        self.walletstock_table.clear()
        while (self.walletstock_table.rowCount() > 0):
            self.walletstock_table.removeRow(0)
        hheader = ["", "  Coin", "  Price(USD)", "  Amount", "  Value(USD)", "  Value(KRW)"]
        
        for j in range(6):
            self.column_1 = QTableWidgetItem()
            self.column_1.setTextAlignment(Qt.AlignVCenter)
            self.column_1.setText(hheader[j])
            self.walletstock_table.setHorizontalHeaderItem(j, self.column_1)
        
        for coin_name in df_balance:
            pass
        #     self.walletstock_table.setRowHeight(i, 28)
        #     self.walletstock_table.insertRow(i) # Insert row

        #     self.define = RainBow_Label(i, bg=self.bg_two)
            
        #     self.coin_name_item = QTableWidgetItem()
        #     self.coin_name_item.setText(coin_name)

        #     self.USD_value_item = QTableWidgetItem()
        #     self.USD_value = Function_ccxt.get_price_USD(coin_name)
        #     self.USD_value_item.setText(str(self.USD_value))

        #     self.coin_amount_item = QTableWidgetItem()
        #     self.coin_amount = Function_ccxt.df_balance[coin_name]["total"]
        #     self.coin_amount_item.setText(str(round(self.coin_amount,3)))
            
        #     self.coin_to_USD_item = QTableWidgetItem()
        #     self.coin_to_USD = self.coin_amount * Function_ccxt.get_price_USD(coin_name)
        #     self.coin_to_USD_item.setText(str(round(self.coin_to_USD,2)))
            
        #     self.coin_to_KRW_item = QTableWidgetItem()
        #     self.coin_to_KRW = self.coin_to_USD * int(Function_exchangerate.USD_to_KRW())
                
        #     self.coin_to_KRW_item.setText(str(round(self.coin_to_KRW, 0)))
            
        #     self.walletstock_table.setCellWidget(i, 0, self.define)
        #     self.walletstock_table.setItem(i, 1, self.coin_name_item)
        #     self.walletstock_table.setItem(i, 2, self.USD_value_item) 
        #     self.walletstock_table.setItem(i, 3, self.coin_amount_item) 
        #     self.walletstock_table.setItem(i, 4, self.coin_to_USD_item)
        #     self.walletstock_table.setItem(i, 5, self.coin_to_KRW_item)
        #     i += 1
        #     total_USD += self.coin_to_USD
        #     total_KRW += self.coin_to_KRW
        
        # self.walletstock_table.insertRow(i)
        # self.walletstock_table.setItem(i, 3, QTableWidgetItem(str("Total")))
        # self.walletstock_table.setItem(i, 4, QTableWidgetItem("$"+str(round(total_USD, 0))))
        # self.walletstock_table.setItem(i, 5, QTableWidgetItem("\\"+str(round(total_KRW, 0))))
        
        # self.walletstock_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # self.walletstock_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        # self._height = (i+1) * self.walletstock_table.rowHeight(0)
    
    def appear_animation(self):
        # CREATE ANIMATION
        
        self.animation = QPropertyAnimation(
            self.walletstock_table, 
            propertyName=b"opacity",
            targetObject=self.effect,
            duration=500,
            startValue=0.0,
            endValue=0.99,
            
            )
        self._animation = QPropertyAnimation(
            self.ani_frame, 
            propertyName=b"pos",
            targetObject=self.walletstock_table,
            duration=500,
            startValue=QPoint(10, -self.walletstock_frame.height()),
            endValue=QPoint(10, 10),
            
            )
        self.animation.start()
        self._animation.start()
        pass
    
    def sig_n_slot(self):
        self.thread_getbalance.getbalance_donesig.connect(self.organize_table)
        self.thread_getbalance.getbalance_donesig.connect(self.appear_animation)
        pass
    
    def setup_thread(self):
        self.thread_getbalance = Thread_getBalance(
            parent = self,
            app_parent = self._app_parent
        )
        
    def setup_Ui(self):
        self.walletstock_widget_vlayout = QVBoxLayout(self)
        self.walletstock_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        self.walletstock_widget_vlayout.setSpacing(0)
        
        self.walletstock_frame = QFrame()
        self.walletstock_frame.setStyleSheet(f'''background-color: {self.bg_three}''')
        self.walletstock_vlayout = QVBoxLayout(self.walletstock_frame)
        self.walletstock_vlayout.setContentsMargins(10, 5, 10, 10)
        self.walletstock_vlayout.setSpacing(0)
        
        self.walletstock_label = QLabel()
        self.walletstock_label.setStyleSheet('''
            padding-top: 10px;
            padding-left: 5px;
            font: 12px;
        ''')
        self.walletstock_label.setText("Table")
        
        self.ani_frame = QFrame()
        self.ani_vlayout = QVBoxLayout(self.ani_frame)
        
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
        
        self.ani_vlayout.addWidget(self.walletstock_table)
        self.walletstock_vlayout.addWidget(self.walletstock_label)
        self.walletstock_vlayout.addWidget(self.ani_frame)
        # self.walletstock_vlayout.addWidget(self.walletstock_table)
        self.walletstock_widget_vlayout.addWidget(self.walletstock_frame)
        
        self.effect = QGraphicsOpacityEffect(self, opacity=0.0)
        self.walletstock_table.setGraphicsEffect(self.effect)
        
class RainBow_Label(QLabel):
    rainbow = ["red", "orange", "yellow", "lightgreen", "darkgreen", "blue", "navy","purple", "violet", "pink", "lightblue", "darkgray"]
    def __init__(
        self,
        order,
        bg
    ):
        super().__init__()
        self.order = order
        self.bg = bg
        self.setFixedSize(10, 20)
    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(self.bg))
        painter.drawRect(0, 0, 10, 20)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(self.rainbow[self.order]))
        painter.drawEllipse(0, 10, 10, 10)
        painter.end()
        
