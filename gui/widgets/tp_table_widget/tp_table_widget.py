from module.pyside6_module_import import *
from .style import *

class Tp_Table_Widget(QTableWidget):
    def __init__(
        self,
        bg_one = "#e0e3ea",
        bg_two = "#f5f6fa",
        bg_three = "#fff",
        
        color_one = "#b9cefe",
        color_two = "#8aadff",
        color_three = "#6c98fe",
        
        border_radius = 15
    ):
        super().__init__()
        
        self.set_stylesheet(
            bg_one,
            bg_two,
            bg_three,
            
            color_one,
            color_two,
            color_three,
            
            border_radius
        )
        self.setShowGrid(False)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
    def set_stylesheet(
        self,
        bg_one,
        bg_two,
        bg_three,
        
        color_one,
        color_two,
        color_three,
        border_radius
        ):
        style_format = style.format(
            _bg_one = bg_one,
            _bg_two = bg_two,
            _bg_three = bg_three,
            
            _color_one = color_one,
            _color_two = color_two,
            _color_three = color_three,
            _border_radius = border_radius
        )
        self.setStyleSheet(style_format)