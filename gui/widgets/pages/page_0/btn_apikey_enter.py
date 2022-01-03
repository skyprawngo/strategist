from module.pyside6_module_import import *

class Btn_Apickey_enter(QPushButton):
    def __init__(
        self,
        icon_file_path,
        bg_color = "#c3c4c6",
        bg_color_hover = "#e3dbd7",
        bg_color_pressed = "#d0a99a",
        
        btn_istoggle_active = False
        
    ):
        super().__init__()
        self.icon_file_path = icon_file_path
        self.bg_color = bg_color
        self.bg_color_hover = bg_color_hover
        self.bg_color_pressed = bg_color_pressed
        
        self.btn_istoggle_active = btn_istoggle_active
        
        self.setup_Ui()
    
    def setup_Ui(self):
        self.setStyleSheet(f"background-color: {self.bg_color}")
        self.vlayout = QVBoxLayout(self)
        self.setIcon(QIcon(self.icon_file_path).pixmap(QSize(50, 50)))
    
    def changetoggleStyle(self, event):
        if event == QEvent.Enter:
            if not self.btn_istoggle_active:
                self.set_btn_bg_color = self.bg_color_hover
            self.btnStyle()
        elif event == QEvent.Leave:
            if not self.btn_istoggle_active:
                self.set_btn_bg_color = self.bg_color
            self.btnStyle()
        elif event == QEvent.MouseButtonPress:
            if self.btn_istoggle_active:
                self.set_btn_bg_color = self.bg_color_hover
                self.btn_istoggle_active = False
            elif not self.btn_istoggle_active:
                self.set_btn_bg_color = self.bg_color_pressed
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
            self.clicked.emit()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.changetoggleStyle(QEvent.MouseButtonRelease)
            self.setFocus()
            self.released.emit()
