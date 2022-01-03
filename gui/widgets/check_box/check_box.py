from PySide6.QtWidgets import QCheckBox


from module.pyside6_module_import import *

class Check_Box(QCheckBox):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(20)
        self.setStyleSheet('''
            QCheckBox::indicator {
                background-color: qlineargradient(...);
                border: 1px solid #a2a5a9;
                width: 15px;
                height: 15px;
                border-radius: 5px;
                left: 1px;
            }
            QCheckBox::indicator:hover {
                background-color: #e3dbd7;
                border: 1px solid #e3dbd7;
                width: 15px;
                height: 15px;
                border-radius: 5px;
            }
            QCheckBox::indicator:checked {
                background-color: #d0a99a;
                border: 1px solid #d0a99a;
                width: 15px;
                height: 15px;
                border-radius: 5px;
            }
        ''')