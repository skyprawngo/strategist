from PySide6.QtWidgets import QCheckBox


from module.pyside6_module_import import *

class Check_Box(QCheckBox):
    def __init__(
        self,
        bg_one = "#e0e3ea",
        bg_two = "#f5f6fa",
        bg_three = "#fff",
        
        color_one = "#b9cefe",
        color_two = "#8aadff",
        color_three = "#6c98fe"
        ):
        super().__init__()
        self.bg_one = bg_one
        self.bg_two = bg_two
        self.bg_three = bg_three
        
        self.color_one = color_one
        self.color_two = color_two
        self.color_three = color_three
        self.setFixedHeight(20)
        qcheckbox_indicator = f'''
            background-color: qlineargradient(...);
            border: 1px solid #a2a5a9;
            width: 15px;
            height: 15px;
            border-radius: 5px;
            left: 1px;
        '''
        qcheckbox_indicator_hover = f'''
            background-color: {self.color_one};
            border: 1px solid {self.color_one};
            width: 15px;
            height: 15px;
            border-radius: 5px;
        '''
        qcheckbox_indicator_pressed = f'''
            background-color: {self.color_three};
            border: 1px solid {self.color_three};
            width: 15px;
            height: 15px;
            border-radius: 5px;
        '''
        qcheckbox_indicator = "{"+qcheckbox_indicator+"}"
        qcheckbox_indicator_hover = "{"+qcheckbox_indicator_hover+"}"
        qcheckbox_indicator_pressed = "{"+qcheckbox_indicator_pressed+"}"
        
        _style = f'''
        QCheckBox::indicator {qcheckbox_indicator}
        QCheckBox::indicator:hover {qcheckbox_indicator_hover}
        QCheckBox::indicator:checked {qcheckbox_indicator_pressed}
        '''
        
        self.setStyleSheet(_style)