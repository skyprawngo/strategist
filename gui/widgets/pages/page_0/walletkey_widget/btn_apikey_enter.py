from module.pyside6_module_import import *

class Btn_Apikey_enter(QPushButton):
    def __init__(
        self,
        icon_file_path,
        
        bg_one = "#e0e3ea",
        bg_two = "#f5f6fa",
        bg_three = "#fff",
        
        color_one = "#b9cefe",
        color_two = "#8aadff",
        color_three = "#6c98fe",
        
        btn_istoggle_active = False
        
    ):
        super().__init__()
        self.icon_file_path = icon_file_path
        
        self.bg_one = bg_one
        self.bg_two = bg_two
        self.bg_three = bg_three
        
        self.color_one = color_one
        self.color_two = color_two
        self.color_three = color_three
        
        self.btn_istoggle_active = btn_istoggle_active
        
        self.setup_Ui()
    
    def setup_Ui(self):
        self.setObjectName("btn_walletkey_enter")
        self.setStyleSheet(f"background-color: {self.bg_two}")
        self.vlayout = QVBoxLayout(self)
        self.setIcon(QIcon(self.icon_file_path).pixmap(QSize(50, 50)))
    
    def changetoggleStyle(self, event):
        if event == QEvent.Enter:
            if not self.btn_istoggle_active:
                self.set_btn_bg_color = self.color_one
            self.btnStyle()
        elif event == QEvent.Leave:
            if not self.btn_istoggle_active:
                self.set_btn_bg_color = self.bg_two
            self.btnStyle()
        elif event == QEvent.MouseButtonPress:
            if self.btn_istoggle_active:
                self.set_btn_bg_color = self.bg_one
                self.btn_istoggle_active = False
            elif not self.btn_istoggle_active:
                self.set_btn_bg_color = self.color_three
                self.btn_istoggle_active = True
            self.btnStyle()
        elif event == QEvent.MouseButtonRelease:
            pass
    
    def btnStyle(self):
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(f'''
            background-color: {self.set_btn_bg_color};
        ''')
    
    def enterEvent(self, event):
        self.changetoggleStyle(QEvent.Enter)

    def leaveEvent(self, event):
        self.changetoggleStyle(QEvent.Leave)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.changetoggleStyle(QEvent.MouseButtonPress)
            if self.btn_istoggle_active:
                self.clicked.emit()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.changetoggleStyle(QEvent.MouseButtonRelease)
            if self.btn_istoggle_active:
                self.released.emit()
