# -*- coding: utf-8 -*-
from gui.module_import import *

from gui.widgets.left_menu_column.left_menu_button import Left_Menu_Button

from gui.themes.load_item_path import Load_Item_Path

button_streched = False

class Ui_Left_Menu_Column_Widget(QWidget):
    def __init__(
        self,
        app_parent,
        parent,
        time_animation,
        
        font_type = "Segoi UI",
        font_size = 10,

        left_menu_bar_btn_size = [30, 30],
        left_menu_bar_btn_radius = 8,

        left_menu_bar_text_color = "#000",
        left_menu_bar_text_color_hover = "#000",
        left_menu_bar_text_color_pressed = "#000",
        
        left_menu_bar_bg_width = 30,
        left_menu_bar_bg_radius = 10,
        left_menu_bar_bg_color = "#fff",
        left_menu_bar_bg_color_hover = "#fff",
        left_menu_bar_bg_color_pressed = "#fff"
    ):
        super().__init__()

        self.app_parent = app_parent
        self.parent = parent
        self.time_animation = time_animation
        
        self.font_type = font_type
        self.font_size = font_size

        self.left_menu_bar_btn_size = left_menu_bar_btn_size
        self.left_menu_bar_btn_radius = left_menu_bar_btn_radius

        self.left_menu_bar_text_color = left_menu_bar_text_color
        self.left_menu_bar_text_color_hover = left_menu_bar_text_color_hover
        self.left_menu_bar_text_color_pressed = left_menu_bar_text_color_pressed

        self.left_menu_bar_bg_width = left_menu_bar_bg_width
        self.left_menu_bar_bg_radius = left_menu_bar_bg_radius
        self.left_menu_bar_bg_color = left_menu_bar_bg_color
        self.left_menu_bar_bg_color_hover = left_menu_bar_bg_color_hover
        self.left_menu_bar_bg_color_pressed = left_menu_bar_bg_color_pressed

        self.setupUi()
    
    def setupUi(self):
        self.left_menu_bar_vlayout = QVBoxLayout(self)
        self.left_menu_bar_vlayout.setContentsMargins(0, 0, 0, 0)

        self.btn_toggle_frame = QFrame()
        self.btn_toggle_frame.setStyleSheet('''
            background-color: lightblue;
        ''')
        self.btn_toggle_vlayout = QVBoxLayout(self.btn_toggle_frame)
        self.btn_toggle_vlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_vlayout.setSpacing(0)

        self.left_menu_bar_vlayout.addWidget(self.btn_toggle_frame)
        


        

