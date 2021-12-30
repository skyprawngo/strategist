# -*- coding: utf-8 -*-
from module.pyside6_module_import import *

from gui.widgets.left_menu.left_menu_button import Left_Menu_Button
from gui.widgets.left_menu.div import Div

from gui.themes.load_item_path import Load_Item_Path

button_streched = False

class Ui_Left_Menu_Column_Widget(QWidget):
    clicked = Signal(object)
    released = Signal(object)
    
    def __init__(
        self,
        app_parent,
        parent,
        time_animation,
        minimum_width = 50,
        maximum_width = 240,
        
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

        self._app_parent = app_parent
        self._parent = parent
        self._time_animation = time_animation
        self.minimum_width = minimum_width
        self.maximum_width = maximum_width
        
        self._font_type = font_type
        self._font_size = font_size
        self._bg_color = bg_color

        self._left_menu_bar_btn_size = left_menu_bar_btn_size
        self._left_menu_bar_btn_radius = left_menu_bar_btn_radius

        self._left_menu_bar_text_color = left_menu_bar_text_color
        self._left_menu_bar_text_color_hover = left_menu_bar_text_color_hover
        self._left_menu_bar_text_color_pressed = left_menu_bar_text_color_pressed

        self._left_menu_bar_bg_width = left_menu_bar_bg_width
        self._left_menu_bar_bg_radius = left_menu_bar_bg_radius
        self._left_menu_bar_bg_color = left_menu_bar_bg_color
        self._left_menu_bar_bg_color_hover = left_menu_bar_bg_color_hover
        self._left_menu_bar_bg_color_pressed = left_menu_bar_bg_color_pressed

        self.setupUi()
        
        self.btn_menu_toggle = Left_Menu_Button(
            parent = self._parent,
            app_parent = self._app_parent,
            btn_id = "btn_menu",
            icon_file_path = Load_Item_Path().set_svg_icon_path("menu-burger.svg"),
            tooltip_text = "Menu Toggle",
            
            btn_istoggle = True,
            btn_size = self._left_menu_bar_btn_size,
            btn_radius  = self._left_menu_bar_btn_radius,

            btn_icon_color = self._left_menu_bar_text_color,
            btn_icon_color_hover = self._left_menu_bar_bg_color_hover,
            btn_icon_color_pressed = self._left_menu_bar_bg_color_pressed,
            
            btn_bg_color = self._left_menu_bar_bg_color,
            btn_bg_color_hover = self._left_menu_bar_bg_color_hover,
            btn_bg_color_pressed = self._left_menu_bar_bg_color_pressed
        )
        self.btn_toggle_vlayout.addWidget(self.btn_menu_toggle)
        
        self.div_1 = Div(self._left_menu_bar_bg_color_pressed)
        self.btn_toggle_vlayout.addWidget(self.div_1)
        
        self.left_menu_bar_vlayout.addWidget(self.btn_toggle_frame)
        self.btn_toggle_vlayout.addWidget(self.btn_menu_frame)
    
    def add_menus(self, parameters):
        if parameters != None:
            for parameter in parameters:
                _btn_id = parameter["btn_id"]
                _icon_file_name = parameter["icon_file_name"]
                _tooltip_text = parameter["tooltip_text"]
                _btn_istoggle = parameter["btn_istoggle"]
                _btn_istoggle_active = parameter["btn_istoggle_active"]
                _btn_isactive = parameter["btn_isactive"]
                
                self.menu = Left_Menu_Button(
                    parent = self._parent,
                    app_parent = self._app_parent,
                    btn_id = _btn_id,
                    icon_file_path = Load_Item_Path().set_svg_icon_path(_icon_file_name),
                    tooltip_text = _tooltip_text,
                    
                    btn_istoggle = _btn_istoggle,
                    btn_istoggle_active = _btn_istoggle_active,
                    btn_isactive = _btn_isactive,
                    btn_size = self._left_menu_bar_btn_size,
                    btn_radius  = self._left_menu_bar_btn_radius,

                    btn_icon_color = self._left_menu_bar_text_color,
                    btn_icon_color_hover = self._left_menu_bar_bg_color_hover,
                    btn_icon_color_pressed = self._left_menu_bar_bg_color_pressed,
                    
                    btn_bg_color = self._left_menu_bar_bg_color,
                    btn_bg_color_hover = self._left_menu_bar_bg_color_hover,
                    btn_bg_color_pressed = self._left_menu_bar_bg_color_pressed
                )
                self.menu.clicked.connect(self.btn_clicked)
                self.menu.released.connect(self.btn_released)
                self.menu.clicked.connect(self.select_only_one)
                
                self.btn_menu_vlayout.addWidget(self.menu)
                
    def select_only_one(self):
        self.btn= self.sender()
        for self.left_menu_btn in self.btn_menu_frame.findChildren(QPushButton):
            self.left_menu_btn.set_switch_toggle(False)
            if self.left_menu_btn.objectName() == self.btn.objectName():
                self.left_menu_btn.set_switch_toggle(True)
                
    def btn_clicked(self):
        self.clicked.emit(self.menu)
    
    def btn_released(self):
        self.released.emit(self.menu)
    
    def toggle_animation(self):
        # CREATE ANIMATION
        self.animation = QPropertyAnimation(self._parent, b"minimumWidth")
        self.animation.stop()
        if self.width() == self._minimum_width:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._maximum_width)
            self.toggle_button.set_active_toggle(True)
            self.toggle_button.set_icon(self._icon_path_close)
        else:
            self.animation.setStartValue(self.width())
            self.animation.setEndValue(self._minimum_width)
            self.toggle_button.set_active_toggle(False)
            self.toggle_button.set_icon(self._icon_path)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setDuration(self._duration_time)
        self.animation.start()

    def setupUi(self):
        self.left_menu_bar_vlayout = QVBoxLayout(self)
        self.left_menu_bar_vlayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bar_vlayout.setSpacing(0)

        self.btn_toggle_frame = QFrame()
        self.btn_toggle_frame.setStyleSheet(f'''
            background-color: {self._left_menu_bar_bg_color};
            border-top-left-radius: 0px;
        ''')
        self.btn_toggle_vlayout = QVBoxLayout(self.btn_toggle_frame)
        self.btn_toggle_vlayout.setContentsMargins(0, 5, 0, 0)
        self.btn_toggle_vlayout.setSpacing(0)
        self.btn_toggle_vlayout.setAlignment(Qt.AlignHCenter)

        self.btn_menu_frame = QFrame()
        self.btn_menu_vlayout = QVBoxLayout(self.btn_menu_frame)
        self.btn_menu_vlayout.setAlignment(Qt.AlignTop)
        self.btn_menu_vlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_vlayout.setSpacing(5)
