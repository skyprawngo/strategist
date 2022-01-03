from PySide6.QtWidgets import QCheckBox


from module.pyside6_module_import import *

class Check_Box(QCheckBox):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(20)
        self.setStyleSheet('''
            QCheckBox::indicator {
                background-color: qlineargradient(...);
                border: 1px solid #000;
                width: 15px;
                height: 15px;
                border-radius: 5px;
                left: 1px;
            }
            QCheckBox::indicator:hover {
                background-color: #9dabbe;
                border: 1px solid #9dabbe;
                width: 15px;
                height: 15px;
                border-radius: 5px;
            }
            QCheckBox::indicator:checked {
                background-color: #3867a8;
                border: 1px solid #3867a8;
                width: 15px;
                height: 15px;
                border-radius: 5px;
            }
        ''')