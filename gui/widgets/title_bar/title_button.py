

from gui.module_import import *

class Title_Button(QPushButton):
    def __init__(
        self,
        UiMainWindow,
        icon_file_name,

        btn_bg_color = "#ffffff",
        btn_bg_color_hover = "#ffffff",
        btn_bg_color_pressed = "#ffffff",

        btn_icon_color = "#000000",
        btn_icon_color_hover = "#000000",
        btn_icon_color_pressed = "#000000"
    ):
        super().__init__()
        