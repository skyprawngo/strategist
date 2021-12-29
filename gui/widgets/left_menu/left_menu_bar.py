# -*- coding: utf-8 -*-
from module.pyside6_module_import import *

from gui.widgets.left_menu.left_menu_button import Left_Menu_Button
from gui.widgets.left_menu.div import Div

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
        bg_color = "#fff",

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
        self.bg_color = bg_color

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
    
    def select_only_one_tab(self, widget: str):
        for btn in self.findChildren(QPushButton):
            if btn.objectName() == widget:
                btn.set_active_tab(True)
            else:
                btn.set_active_tab(False)
    
    def setupUi(self):
        self.left_menu_bar_vlayout = QVBoxLayout(self)
        self.left_menu_bar_vlayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bar_vlayout.setSpacing(0)

        self.btn_toggle_frame = QFrame()
        self.btn_toggle_frame.setStyleSheet(f'''
            background-color: {self.left_menu_bar_bg_color};
            border-top-left-radius: 0px;
        ''')
        self.btn_toggle_vlayout = QVBoxLayout(self.btn_toggle_frame)
        self.btn_toggle_vlayout.setContentsMargins(0, 5, 0, 0)
        self.btn_toggle_vlayout.setSpacing(0)
        self.btn_toggle_vlayout.setAlignment(Qt.AlignHCenter)

        self.btn_menu_toggle = Left_Menu_Button(
            parent = self.parent,
            app_parent = self.app_parent,
            icon_file_path = Load_Item_Path().set_svg_icon_path("menu-burger.svg"),
            tooltip_text = "Menu Toggle",
            
            btn_istoggle = True,
            btn_size = self.left_menu_bar_btn_size,
            btn_radius  = self.left_menu_bar_btn_radius,

            btn_icon_color = self.left_menu_bar_text_color,
            btn_icon_color_hover = self.left_menu_bar_bg_color_hover,
            btn_icon_color_pressed = self.left_menu_bar_bg_color_pressed,
            
            btn_bg_color = self.left_menu_bar_bg_color,
            btn_bg_color_hover = self.left_menu_bar_bg_color_hover,
            btn_bg_color_pressed = self.left_menu_bar_bg_color_pressed
        )
        self.btn_toggle_vlayout.addWidget(self.btn_menu_toggle)
        self.div_1 = Div(self.left_menu_bar_bg_color_pressed)
        self.btn_toggle_vlayout.addWidget(self.div_1)

        self.btn_menu_frame = QFrame()
        self.btn_menu_vlayout = QVBoxLayout(self.btn_menu_frame)
        self.btn_menu_vlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_vlayout.setSpacing(5)

        self.btn_home_toggle = Left_Menu_Button(
            parent = self.parent,
            app_parent = self.app_parent,
            icon_file_path = Load_Item_Path().set_svg_icon_path("home.svg"),
            tooltip_text = "Home",
            
            btn_istoggle = True,
            btn_size = self.left_menu_bar_btn_size,
            btn_radius  = self.left_menu_bar_btn_radius,

            btn_icon_color = self.left_menu_bar_text_color,
            btn_icon_color_hover = self.left_menu_bar_bg_color_hover,
            btn_icon_color_pressed = self.left_menu_bar_bg_color_pressed,
            
            btn_bg_color = self.left_menu_bar_bg_color,
            btn_bg_color_hover = self.left_menu_bar_bg_color_hover,
            btn_bg_color_pressed = self.left_menu_bar_bg_color_pressed
        )
        self.btn_menu_vlayout.addWidget(self.btn_home_toggle)
        
        self.btn_chart_toggle = Left_Menu_Button(
            parent = self.parent,
            app_parent = self.app_parent,
            icon_file_path = Load_Item_Path().set_svg_icon_path("chat-arrow-grow.svg"),
            tooltip_text = "Chart",
            
            btn_istoggle = True,
            btn_size = self.left_menu_bar_btn_size,
            btn_radius  = self.left_menu_bar_btn_radius,

            btn_icon_color = self.left_menu_bar_text_color,
            btn_icon_color_hover = self.left_menu_bar_bg_color_hover,
            btn_icon_color_pressed = self.left_menu_bar_bg_color_pressed,
            
            btn_bg_color = self.left_menu_bar_bg_color,
            btn_bg_color_hover = self.left_menu_bar_bg_color_hover,
            btn_bg_color_pressed = self.left_menu_bar_bg_color_pressed
        )
        self.btn_menu_vlayout.addWidget(self.btn_chart_toggle)


        self.left_menu_bottom_frame = QFrame()
        self.btn_menu_vlayout.addWidget(self.left_menu_bottom_frame)
        self.btn_toggle_vlayout.addWidget(self.btn_menu_frame)
        self.left_menu_bar_vlayout.addWidget(self.btn_toggle_frame)

        
        


        

