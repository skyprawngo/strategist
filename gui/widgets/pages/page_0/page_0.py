from module.pyside6_module_import import *
from gui.widgets.scroll_area.scroll_area import Scroll_Area
from gui.widgets.check_box.check_box import Check_Box

from .walletkey_widget import Walletkey_Widget


class Page_0(QWidget):
    def __init__(
        self
    ):
        super().__init__()
        self.setupUi()
    
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
        
        self.walletkey_widget = Walletkey_Widget(
            parent = self
        )
        self.scrollarea_glayout.addWidget(self.walletkey_widget, 0, 0, 1, 3)
        
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
    