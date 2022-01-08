from module.pyside6_module_import import *

from func.func_ccxt import Function_ccxt

class walletchart_widget(QWidget):
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
        
        
    def setup_Ui(self):
        self.walletchart_widget_vlayout = QVBoxLayout(self)
        self.walletchart_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        self.walletchart_widget_vlayout.setSpacing(0)
        
        self.walletchart_frame = QFrame()
        self.walletchart_frame.setStyleSheet(f'''background-color: {self.bg_three}''')
        self.walletchart_vlayout = QVBoxLayout(self.walletchart_frame)
        self.walletchart_vlayout.setContentsMargins(10, 10, 10, 10)
        
        self.walletchart_label = QLabel()
        self.walletchart_label.setStyleSheet('''
            padding-left: 5px;
            font: 12px;
        ''')
        self.walletchart_label.setText("Chart")
        
        
        
        self.walletchart_vlayout.addWidget(self.walletchart_label)
        
        self.walletchart_widget_vlayout.addWidget(self.walletchart_frame)
        
        