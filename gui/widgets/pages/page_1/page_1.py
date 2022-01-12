from module.pyside6_module_import import *
from gui.themes.load_item_path import Load_Item_Path
from gui.widgets.pages.page_1.candlestick_chart import Candlestick_Chart

from gui.widgets.tp_scroll_area.tp_scroll_area import Scroll_Area
from gui.widgets.tp_pushbutton.tp_pushbutton import Tp_PushButton


class Page_1(QWidget):
    def __init__(
        self,
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
        self._app_parent = app_parent
        self.bg_one = bg_one
        self.bg_two = bg_two
        self.bg_three = bg_three
        
        self.color_one = color_one
        self.color_two = color_two
        self.color_three = color_three
        self.color_red = color_red
        
        self.setupUi()
    
    def sig_n_slot(self):
        
        pass
    
    def setupUi(self):
        self.setObjectName("page_1")
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setStyleSheet('''
            border-radius: 15px;
        ''')
        self.glayout = QGridLayout(self)
        self.glayout.setContentsMargins(5, 5, 5, 5)
        self.glayout.setSpacing(5)
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(self.shadow)
        
    
        self.btn_frame = QFrame()
        self.btn_frame.setStyleSheet(f"background-color: {self.bg_three};")
        self.btn_vlayout = QVBoxLayout(self.btn_frame)
        self.btn_vlayout.setAlignment(Qt.AlignTop)
        self.btn_vlayout.setContentsMargins(5, 5, 5, 5)
        self.btn_vlayout.setSpacing(10)
        
        self.btn_choose_strategy = Tp_PushButton(
            parent = self,
            app_parent = self._app_parent,
            btn_id = "btn_VBS",
            btn_layout = "hlayout",
            btn_radius = 8,
            
            icon_file_path = Load_Item_Path().set_svg_icon_path("pulse.svg"),
            icon_size = [35, 35],
            
            tooltip_text="Volatility BreakThrough",
            
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three,
            
            is_toggle_btn = True
        )
        self.btn_choose_strategy.setFixedHeight(50)
        self.btn_choose_strategy.set_text(True)
        self.btn_vlayout.addWidget(self.btn_choose_strategy)
        
        self.strategy_chart_frame = QFrame()
        self.strategy_chart_frame.setStyleSheet(f"background-color: {self.bg_three};")
        self.strategy_chart_layout = QHBoxLayout(self.strategy_chart_frame)
        self.strategy_chart_layout.setContentsMargins(0, 0, 0, 0)
        
        self.chart = Candlestick_Chart(
            parent = self,
            app_parent = self._app_parent,
        )
        self.strategy_chart_layout.addWidget(self.chart)
        
        self.market_frame = QFrame()
        self.market_frame.setStyleSheet(f"background-color: {self.bg_three};")
        self.market_vlayout = QVBoxLayout(self.market_frame)
        self.market_vlayout.setContentsMargins(0, 0, 0, 0)
        self.market_vlayout.setAlignment(Qt.AlignTop)
        
        self.btn_btc = Tp_PushButton(
            parent = self,
            app_parent = self._app_parent,
            btn_id = "btn_BTC",
            btn_layout = "hlayout",
            btn_radius = 8,
            
            icon_visible = False,
            
            tooltip_text="BTC/USDT",
            
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three,
            
            is_toggle_btn = True
        )
        self.btn_btc.setFixedHeight(50)
        self.btn_btc.set_text(True)
        self.market_vlayout.addWidget(self.btn_btc)
        
        self.btn_btc.btn_clicked.connect(self.chart.sig_received)
        
        self.strategy_inform_frame = QFrame()
        self.strategy_inform_frame.setStyleSheet(f"background-color: {self.bg_three};")
        self.strategy_inform_frame.setFixedHeight(200)
        self.strategy_inform_hlayout = QHBoxLayout(self.strategy_inform_frame)
        self.strategy_inform_hlayout.setContentsMargins(0, 0, 0, 0)
        
        self.glayout.addWidget(self.btn_frame, 0, 0, 7, 2)
        self.glayout.addWidget(self.strategy_chart_frame, 0, 3, 5, 7)
        self.glayout.addWidget(self.market_frame, 0, 10, 5, 2)
        self.glayout.addWidget(self.strategy_inform_frame, 5, 3, 2, 9)