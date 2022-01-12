from module.pyside6_module_import import *
from gui.widgets.tp_scroll_area.tp_scroll_area import Scroll_Area
from gui.widgets.tp_check_box.tp_check_box import Tp_Check_Box

from .walletkey_widget.walletkey_widget import Walletkey_Widget
from .walletstock_widget.walletstock_widget import Walletstock_Widget
from .walletchart_widget.walletchart_widget import walletchart_widget


class Page_0(QWidget):
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
        self.sig_n_slot()

    def sig_n_slot(self):
        self.walletkey_widget.thread_setkey.setkey_donesig.connect(self.walletstock_widget.key_received)
        self.walletstock_widget.thread_getbalance.getbalance_donesig.connect(self.walletchart_widget.wallet_received)
        pass
        
    def setupUi(self):
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.vlayout = QVBoxLayout(self)
        self.vlayout.setContentsMargins(0, 5, 0, 0)
        self.vlayout.setSpacing(0)
        
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(self.shadow)
        
        self.scrollarea = Scroll_Area(

            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three
        )
        self.scrollarea.setObjectName(u"scrollArea")
        self.scrollarea.setWidgetResizable(True)
        
        self.scrollarea_widget = QWidget()
        self.scrollarea_widget.setAttribute(Qt.WA_TranslucentBackground)
        self.scrollarea_widget.setGeometry(QRect(0, 0, 763, 1000))
        self.scrollarea_widget.setMinimumSize(QSize(0, 1000))
        self.scrollarea_widget.setStyleSheet('''
            border-radius: 15px;
        ''')
        
        self.scrollarea_glayout = QGridLayout(self.scrollarea_widget)
        self.scrollarea_glayout.setContentsMargins(5, 0, 5, 0)
        
        self.walletkey_widget = Walletkey_Widget(
            parent = self,
            app_parent = self._app_parent,
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three,
            color_red = self.color_red
        )
        
        self.distribution_frame = QFrame()
        self.distribution_frame.setStyleSheet(f"background-color: {self.bg_three};")
        
        self.walletstock_widget = Walletstock_Widget(
            parent = self,
            app_parent = self._app_parent,
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three
        )
        
        self.walletchart_widget = walletchart_widget(
            parent = self,
            app_parent = self._app_parent,
            bg_one = self.bg_one,
            bg_two = self.bg_two,
            bg_three = self.bg_three,

            color_one = self.color_one,
            color_two = self.color_two,
            color_three = self.color_three
        )
        
        self.frame2 = QFrame()
        self.frame2.setStyleSheet("background-color: lightblue;")
        
        self.frame3 = QFrame()
        self.frame3.setStyleSheet("background-color: pink;")
        
        self.scrollarea_glayout.addWidget(self.walletkey_widget, 0, 0, 1, 3)
        self.scrollarea_glayout.addWidget(self.distribution_frame, 0, 3, 1, 2)
        self.scrollarea_glayout.addWidget(self.walletstock_widget, 1, 0, 2, 5)
        self.scrollarea_glayout.addWidget(self.walletchart_widget, 0, 5, 3, 7)
        self.scrollarea_glayout.addWidget(self.frame2, 3, 0)
        self.scrollarea_glayout.addWidget(self.frame3, 4, 0)
        self.scrollarea.setWidget(self.scrollarea_widget)
        
        
        self.vlayout.addWidget(self.scrollarea)
    