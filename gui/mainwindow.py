# -*- coding: utf-8 -*-
from gui.module_import import *

from gui.themes.settings import Settings
from gui.themes.themes import Themes
from gui.themes.theme_switch import Theme_Switch

from gui.widgets.pywindow.pywindow import PyWindow
from gui.widgets.pygrips.py_grips import PyGrips
from gui.widgets.title_bar.title_bar import Ui_Title_Bar_Widget
from gui.widgets.left_menu_column.ui_menu_bar import Ui_Menu_Bar_Widget



class Ui_MainWindow(object):
    def setupUi(self, UiMainWindow):
        # MainWindow(
        if not UiMainWindow.objectName():
            UiMainWindow.setObjectName(u"MainWindow")
        
            # Load Settings
        settings = Settings()
        self.settings = settings.settings
            # Load Themes
        themes = Themes()
        self.themes = themes.themes
        
        UiMainWindow.resize(
            self.settings["startup_size"][0],
            self.settings["startup_size"][1]
        )
        
        UiMainWindow.setMinimumSize(
            self.settings["minimum_size"][0],
            self.settings["minimum_size"][1]
        )
        UiMainWindow.setWindowFlags(Qt.FramelessWindowHint)
        UiMainWindow.setAttribute(Qt.WA_TranslucentBackground)


        self.app_parent = UiMainWindow

        self.window = PyWindow(
            app_parent = UiMainWindow,
            startup_size = self.settings["startup_size"],
            minimum_size = self.settings["minimum_size"],

            margin = self.themes["shape"]["pywindow"]["margin"],
            spacing = self.themes["shape"]["pywindow"]["margin"],
            bg_color = self.themes["app_color"]["bg_one"],
            text_color = self.themes["app_color"]["dark_one"],
            text_font = self.themes["font"]["text_size"],
            border_radius = self.themes["shape"]["pywindow"]["border_radius"],
            border_size = self.themes["shape"]["pywindow"]["border_size"],
            border_color = self.themes["app_color"]["bg_three"],
            custom_title_bar = self.settings["custom_title_bar"]
        )

        

            # Centralwidget(
        self.centralwidget = QWidget(UiMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.centralwidget.setStyleSheet(f'''
            background-color: {self.themes["app_color"]["bg_one"]};
            border-radius: 10px
        ''')
        self.centralwidget_vlayout = QVBoxLayout(self.centralwidget)
        self.centralwidget_vlayout.setSpacing(0)
        self.centralwidget_vlayout.setObjectName(u"centralwidget_vlayout")
        self.centralwidget_vlayout.setContentsMargins(0, 0, 0, 0)
        
                # Set Title Bar Frame(
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.title_bar_frame.setMinimumHeight(self.themes["shape"]["title_bar"]["bg_height"])
        self.title_bar_frame.setMaximumHeight(self.themes["shape"]["title_bar"]["bg_height"])
        self.title_bar_vlayout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_vlayout.setContentsMargins(4, 4, 4, 0)
                    
                    # Import Title Bar(
        self.title_bar = Ui_Title_Bar_Widget(
            app_parent = UiMainWindow,
            parent = self.title_bar_frame,
            app_name = self.settings["app_name"],
            logo_file_name = self.settings["logo_file_name"],
            title_text = self.settings["title_text"],
            custom_title_bar = self.settings["custom_title_bar"],
            time_animation = self.settings["time_animation"],
            
            font_type = self.themes["font"]["family"],
            font_size = self.themes["font"]["title_size"],

            title_bar_btn_size = self.themes["shape"]["title_bar"]["btn_size"],
            title_bar_btn_radius = self.themes["shape"]["title_bar"]["btn_radius"],

            title_bar_text_color = self.themes["app_color"]["dark_three"],
            title_bar_text_color_hover = self.themes["app_color"]["dark_two"],
            title_bar_text_color_pressed = self.themes["app_color"]["dark_one"],
            
            title_bar_bg_height = self.themes["shape"]["title_bar"]["bg_height"],
            title_bar_bg_radius = self.themes["shape"]["title_bar"]["bg_radius"],
            title_bar_bg_color = self.themes["app_color"]["bg_two"],
            title_bar_bg_color_hover = self.themes["app_color"]["bg_three"],
            title_bar_bg_color_pressed = self.themes["app_color"]["bg_four"]
        
        
        )
                    # )
        self.title_bar_vlayout.addWidget(self.title_bar)
                # )

                # not_title_bar_frame(
        self.not_title_bar_frame = QFrame()
        self.not_title_bar_frame.setObjectName(u"not_title_bar_frame")
        self.not_title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.not_title_bar_frame.setFrameShadow(QFrame.Raised)
        self.not_title_bar_hlayout = QHBoxLayout(self.not_title_bar_frame)
        self.not_title_bar_hlayout.setSpacing(0)
        self.not_title_bar_hlayout.setObjectName(u"not_title_bar_hlayout")
        self.not_title_bar_hlayout.setContentsMargins(0, 0, 0, 0)
        
                    # Import Menu Bar(
        self.menu_bar_frame = QFrame()
        self.menu_bar_frame.setFrameShape(QFrame.NoFrame)
        self.menu_bar = Ui_Menu_Bar_Widget()
        self.menu_bar.setupUi(self.menu_bar_frame)
        self.not_title_bar_hlayout.addWidget(self.menu_bar_frame)
        
        self.menu_bar_frame = QFrame()
        self.menu_bar_frame.setObjectName(u"menu_bar_frame")
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_bar_frame.sizePolicy().hasHeightForWidth())
        self.menu_bar_frame.setSizePolicy(sizePolicy)
        self.menu_bar_frame.setMinimumSize(QSize(40, 0))
        self.menu_bar_frame.setMaximumSize(QSize(40, 16777215))
        self.menu_bar_frame.setStyleSheet(u"")
        self.menu_bar_frame.setFrameShape(QFrame.NoFrame)
        self.menu_bar_frame.setFrameShadow(QFrame.Raised)
        self.menu_bar_vlayout = QVBoxLayout(self.menu_bar_frame)
        self.menu_bar_vlayout.setSpacing(0)
        self.menu_bar_vlayout.setObjectName(u"menu_bar_vlayout")
        self.menu_bar_vlayout.setContentsMargins(0, 0, 0, 0)

        self.not_title_bar_hlayout.addWidget(self.menu_bar_frame)

        self.main_page_frame = QFrame()
        self.main_page_frame.setObjectName(u"main_page_frame")
        self.main_page_frame.setFrameShape(QFrame.NoFrame)
        self.main_page_frame.setFrameShadow(QFrame.Raised)

        self.not_title_bar_hlayout.addWidget(self.main_page_frame)

        self.window.vlayout.addWidget(self.title_bar_frame)
        self.window.vlayout.addWidget(self.not_title_bar_frame)
        
        self.centralwidget_vlayout.addWidget(self.window)

        UiMainWindow.setCentralWidget(self.centralwidget)
            # )
        # )

    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            print(self.window.height())
            print(self.app_parent.height())
            self.left_grip.setGeometry(0, 0, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    def setup_gui(self):
        self.hide_grips = False
        self.left_grip = PyGrips(self.app_parent, "left", self.hide_grips)
        self.right_grip = PyGrips(self.app_parent, "right", self.hide_grips)
        self.top_grip = PyGrips(self.app_parent, "top", self.hide_grips)
        self.bottom_grip = PyGrips(self.app_parent, "bottom", self.hide_grips)
        self.top_left_grip = PyGrips(self.app_parent, "top_left", self.hide_grips)
        self.top_right_grip = PyGrips(self.app_parent, "top_right", self.hide_grips)
        self.bottom_left_grip = PyGrips(self.app_parent, "bottom_left", self.hide_grips)
        self.bottom_right_grip = PyGrips(self.app_parent, "bottom_right", self.hide_grips)

        