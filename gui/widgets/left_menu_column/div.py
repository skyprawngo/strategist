from gui.module_import import *
# CUSTOM LEFT MENU
class Div(QWidget):
    def __init__(self, color):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(3,0,3,0)
        self.frame_line = QFrame()
        self.frame_line.setStyleSheet(f"background: {color};")
        self.frame_line.setMaximumHeight(1)
        self.frame_line.setMinimumHeight(1)
        self.layout.addWidget(self.frame_line)
        self.setMaximumHeight(10)
        self.setMinimumHeight(10)