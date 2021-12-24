# -*- coding: utf-8 -*-
from gui.module_import import *

from gui.widgets.title_bar.title_button import Title_Button
from gui.widgets.title_bar.div import Div

from gui.themes.load_item_path import Load_Item_Path

window_isMaximised = False
window_oldSize = QSize()

class Ui_Title_Bar_Widget(QWidget):
    def __init__(
            self,
            app_parent,
            parent,
            app_name = "Strategist",
            logo_file_name = "logo_top.svg",
            title_text = "",
            custom_title_bar = None,
            time_animation = 500,
            
            font_type = "Segoe_UI",
            font_size = 10,

            title_bar_btn_size = [30, 30],
            title_bar_btn_radius = 8,

            title_bar_text_color = "#000000",
            title_bar_text_color_hover = "#000000",
            title_bar_text_color_pressed = "#000000",

            title_bar_bg_height = 30,
            title_bar_bg_radius = 10,
            title_bar_bg_color = "#ffffff",
            title_bar_bg_color_hover = "#ffffff",
            title_bar_bg_color_pressed = "#ffffff",
    ):
        super().__init__()
        
        self.app_parent = app_parent
        self.parent = parent
        self.app_name = app_name
        self.logo_file_name = logo_file_name
        self.title_text = title_text
        self.custom_tilte_bar = custom_title_bar
        self.time_animation = time_animation
        
        self.font_type = font_type
        self.font_size = font_size

        self.title_bar_btn_size = title_bar_btn_size
        self.title_bar_btn_radius = title_bar_btn_radius

        self.title_bar_text_color = title_bar_text_color
        self.title_bar_text_color_hover = title_bar_text_color_hover
        self.title_bar_text_color_pressed = title_bar_text_color_pressed

        self.title_bar_bg_height = title_bar_bg_height
        self.title_bar_bg_radius = title_bar_bg_radius
        self.title_bar_bg_color = title_bar_bg_color
        self.title_bar_bg_color_hover = title_bar_bg_color_hover
        self.title_bar_bg_color_pressed = title_bar_bg_color_pressed
        
        self.setupUi()

        self.title_bar_frame.setStyleSheet(f'''
            background-color: {self.title_bar_bg_color};
            border-top-left-radius: {self.title_bar_bg_radius}px;
            border-top-right-radius: {self.title_bar_bg_radius}px;
            border-bottom-right-radius: {self.title_bar_bg_radius}px;
        ''')

        # Function(
        self.title_btn_minimize.released.connect(lambda: app_parent.showMinimized())
        self.title_btn_maximize.released.connect(lambda: self.func_maximize())
        self.title_btn_close.released.connect(lambda: app_parent.close())

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if app_parent.isMaximized():
                self.func_maximize()
                #self.resize(_old_size)
                curso_x = app_parent.pos().x()
                curso_y = event.globalPos().y() - QCursor.pos().y()
                app_parent.move(curso_x, curso_y)
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                app_parent.move(app_parent.pos() + event.globalPos() - app_parent.dragPos)
                app_parent.dragPos = event.globalPos()
                event.accept()

        if custom_title_bar:
            self.div_1.mouseMoveEvent = moveWindow
            self.title_label.mouseMoveEvent = moveWindow
            self.top_logo_label.mouseMoveEvent = moveWindow

            self.div_1.mouseDoubleClickEvent = self.func_maximize
            self.title_label.mouseDoubleClickEvent = self.func_maximize
            self.top_logo_label.mouseDoubleClickEvent = self.func_maximize
        # )

    def func_maximize(self):
        global window_isMaximised
        global window_oldSize

        if self.app_parent.isMaximized():
            window_isMaximised = False
            self.app_parent.showNormal()
            self.title_btn_maximize.set_icon(Load_Item_Path().set_svg_icon_path("square.svg"))
            self.title_btn_maximize.set_label("Maximize")


        elif not self.app_parent.isMaximized():
            window_isMaximised = True
            self.app_parent.showMaximized()
            self.title_btn_maximize.set_icon(Load_Item_Path().set_svg_icon_path("copy.svg"))
            self.title_btn_maximize.set_label("Return Size")
        
    def setupUi(self):
        
        self.title_bar_widget_vlayout = QVBoxLayout(self)
        self.title_bar_widget_vlayout.setContentsMargins(0, 0, 0, 0)
        
        # title_bar_frame(
        self.title_bar_frame = QFrame()
        self.title_bar_hlayout = QHBoxLayout(self.title_bar_frame)
        self.title_bar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar_hlayout.setSpacing(0)
        
            # top_logo_label(
        self.top_logo_label = QLabel()

        self.top_logo_label.setFixedSize(100, 30)
        self.top_logo_label_vlayout = QVBoxLayout(self.top_logo_label)
        self.top_logo_label_vlayout.setContentsMargins(8, 5, 0, 5)
        

                # top_logo_image(
        self.top_logo_image = QSvgWidget()
        self.top_logo_image_path = Load_Item_Path().set_svg_image_path(self.logo_file_name)
        self.top_logo_image.load(self.top_logo_image_path)
                # )
        self.top_logo_label_vlayout.addWidget(self.top_logo_image)
            # )
        self.title_bar_hlayout.addWidget(self.top_logo_label)
        
            # title_frame(
        self.title_frame = QFrame()
        self.title_hlayout = QHBoxLayout(self.title_frame)
        self.title_hlayout.setContentsMargins(10, 0, 0, 0)
        self.title_hlayout.setSpacing(0)

                # title_label(
        self.title_label = QLabel()
        self.title_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.title_label.setText(self.title_text)
                # )
        self.title_hlayout.addWidget(self.title_label)
        
                # title_buttons_frame(
        self.title_buttons_frame = QFrame()
        self.title_buttons_frame.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.title_buttons_hlayout = QHBoxLayout(self.title_buttons_frame)
        self.title_buttons_hlayout.setContentsMargins(0, 0, 5, 0)
        self.title_buttons_hlayout.setSpacing(0)

                    # Menu(
        self.menu = Title_Button(
            parent = self.parent,
            app_parent = self.app_parent,
            icon_file_path = Load_Item_Path().set_svg_icon_path("settings.svg"),
            tooltip_text = "Settings",
            
            btn_istoggle = True,
            btn_size = self.title_bar_btn_size,
            btn_radius  = self.title_bar_btn_radius,

            btn_icon_color = self.title_bar_text_color,
            btn_icon_color_hover = self.title_bar_bg_color_hover,
            btn_icon_color_pressed = self.title_bar_bg_color_pressed,
            
            btn_bg_color = self.title_bar_bg_color,
            btn_bg_color_hover = self.title_bar_bg_color_hover,
            btn_bg_color_pressed = self.title_bar_bg_color_pressed
        )
                    # )
        self.title_buttons_hlayout.addWidget(self.menu)

                    # Import Div(
        self.div_1 = Div(self.title_bar_bg_color_pressed)
                    # )
        self.title_buttons_hlayout.addWidget(self.div_1)

                    # minimize_button(
        self.title_btn_minimize = Title_Button(
            parent = self.parent,
            app_parent = self.app_parent,
            icon_file_path = Load_Item_Path().set_svg_icon_path("minus.svg"),
            tooltip_text = "Minimize",
            
            btn_istoggle = False,
            btn_size = self.title_bar_btn_size,
            btn_radius  = self.title_bar_btn_radius,

            btn_icon_color = self.title_bar_text_color,
            btn_icon_color_hover = self.title_bar_bg_color_hover,
            btn_icon_color_pressed = self.title_bar_bg_color_pressed,
            
            btn_bg_color = self.title_bar_bg_color,
            btn_bg_color_hover = self.title_bar_bg_color_hover,
            btn_bg_color_pressed = self.title_bar_bg_color_pressed
        )
                    # )
        self.title_buttons_hlayout.addWidget(self.title_btn_minimize)

                    # maximize_button(
        self.title_btn_maximize = Title_Button(
            self.parent,
            self.app_parent,
            icon_file_path = Load_Item_Path().set_svg_icon_path("square.svg"),
            tooltip_text = "Maximize",

            btn_istoggle = False,
            btn_size = self.title_bar_btn_size,
            btn_radius  =self.title_bar_btn_radius,

            btn_icon_color = self.title_bar_text_color,
            btn_icon_color_hover = self.title_bar_bg_color_hover,
            btn_icon_color_pressed = self.title_bar_bg_color_pressed,
            
            btn_bg_color = self.title_bar_bg_color,
            btn_bg_color_hover = self.title_bar_bg_color_hover,
            btn_bg_color_pressed = self.title_bar_bg_color_pressed

        )
                    # )
        self.title_buttons_hlayout.addWidget(self.title_btn_maximize)

                    # close_button(
        self.title_btn_close = Title_Button(
            self.parent,
            self.app_parent,
            icon_file_path = Load_Item_Path().set_svg_icon_path("cross.svg"),
            tooltip_text = "Close",

            btn_istoggle = False,
            btn_size = self.title_bar_btn_size,
            btn_radius  =self.title_bar_btn_radius,

            btn_icon_color = self.title_bar_text_color,
            btn_icon_color_hover = self.title_bar_bg_color_hover,
            btn_icon_color_pressed = self.title_bar_bg_color_pressed,
            
            btn_bg_color = self.title_bar_bg_color,
            btn_bg_color_hover = self.title_bar_bg_color_hover,
            btn_bg_color_pressed = self.title_bar_bg_color_pressed

        )
                    # )
        self.title_buttons_hlayout.addWidget(self.title_btn_close)
                # )
        self.title_hlayout.addWidget(self.title_buttons_frame)
            # )
        self.title_bar_hlayout.addWidget(self.title_frame)
        # )
        self.title_bar_widget_vlayout.addWidget(self.title_bar_frame)

