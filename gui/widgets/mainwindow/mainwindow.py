# -*- coding: utf-8 -*-
import os
from module.pyside6_module_import import *

from gui.themes.theme_settings import Settings
from gui.themes.themes import Themes
from gui.themes.theme_switch import Theme_Switch


from gui.widgets.pywindow.pywindow import PyWindow
from gui.widgets.title_bar.title_bar import Ui_Title_Bar_Widget
from gui.widgets.left_menu.left_menu_bar import Ui_Left_Menu_Column_Widget
from gui.widgets.pages.mainpages import MainPages

class Ui_MainWindow(object):
    def setupUi(self, UiMainWindow):
        # MainWindow(
        if not UiMainWindow.objectName():
            UiMainWindow.setObjectName(u"MainWindow")
        
            # Load Settings
        theme_settings = Settings()
        self.theme_settings = theme_settings.settings
            # Load Themes
        themes = Themes()
        self.themes = themes.themes

        self.app_parent = UiMainWindow
        
        
        UiMainWindow.resize(
            self.theme_settings["startup_size"][0],
            self.theme_settings["startup_size"][1]
        )
        
        UiMainWindow.setMinimumSize(
            self.theme_settings["minimum_size"][0],
            self.theme_settings["minimum_size"][1]
        )

            # Centralwidget(
        self.centralwidget = QWidget(UiMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.centralwidget.setStyleSheet(f'''
            border-radius: {self.themes["pywindow"]["border_radius"]};
        ''')
        
        self.centralwidget_vlayout = QVBoxLayout(self.centralwidget)
        self.centralwidget_vlayout.setObjectName(u"centralwidget_vlayout")
        self.centralwidget_vlayout.setContentsMargins(0,0,0,0)
        if self.theme_settings["custom_title_bar"]:
            self.centralwidget_vlayout.setContentsMargins(10,10,10,10)
        else:
            self.centralwidget_vlayout.setContentsMargins(0,0,0,0)


                # PyWindow(
        self.window = PyWindow(
            app_parent = UiMainWindow,
            startup_size = self.theme_settings["startup_size"],
            minimum_size = self.theme_settings["minimum_size"],

            margin = self.themes["pywindow"]["margin"],
            spacing = self.themes["pywindow"]["margin"],
            bg_color = self.themes["app_color"]["bg_one"],
            text_color = self.themes["app_color"]["dark_one"],
            text_font_size = self.themes["font"]["text_size"],
            border_radius = self.themes["pywindow"]["border_radius"],
            border_size = self.themes["pywindow"]["border_size"],
            border_color = self.themes["app_color"]["color_one"],
            custom_title_bar = self.theme_settings["custom_title_bar"]
        )
        
                    # title_bar_frame(
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.title_bar_frame.setMinimumHeight(self.themes["title_bar"]["bg_height"])
        self.title_bar_frame.setMaximumHeight(self.themes["title_bar"]["bg_height"])
        self.title_bar_vlayout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_vlayout.setContentsMargins(3, 3, 3, 0)
                    
                        # Title_Bar(
        self.title_bar = Ui_Title_Bar_Widget(
            app_parent = UiMainWindow,
            parent = self.title_bar_frame,
            app_name = self.theme_settings["app_name"],
            logo_file_name = self.theme_settings["logo_file_name"],
            title_text = self.theme_settings["title_text"],
            custom_title_bar = self.theme_settings["custom_title_bar"],
            time_animation = self.theme_settings["time_animation"],
            
            font_type = self.themes["font"]["family"],
            font_size = self.themes["font"]["title_size"],

            title_bar_btn_size = self.themes["title_bar"]["btn_size"],
            title_bar_btn_radius = self.themes["title_bar"]["btn_radius"],

            title_bar_text_color = self.themes["app_color"]["dark_three"],
            title_bar_text_color_hover = self.themes["app_color"]["dark_two"],
            title_bar_text_color_pressed = self.themes["app_color"]["dark_one"],
            
            title_bar_bg_height = self.themes["title_bar"]["bg_height"],
            title_bar_bg_radius = self.themes["title_bar"]["bg_radius"],
            title_bar_bg_color = self.themes["app_color"]["bg_two"],
            title_bar_bg_color_hover = self.themes["app_color"]["color_two"],
            title_bar_bg_color_pressed = self.themes["app_color"]["color_four"]
        )
                        # )Title_Bar
        self.title_bar_vlayout.addWidget(self.title_bar)
                    # )title_bar_frame

                    # not_title_bar_frame(
        self.not_title_bar_frame = QFrame()
        self.not_title_bar_frame.setObjectName(u"not_title_bar_frame")
        self.not_title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.not_title_bar_frame.setFrameShadow(QFrame.Raised)
        self.not_title_bar_hlayout = QHBoxLayout(self.not_title_bar_frame)
        self.not_title_bar_hlayout.setObjectName(u"not_title_bar_hlayout")
        self.not_title_bar_hlayout.setContentsMargins(3, 0, 3, 3)
        self.not_title_bar_hlayout.setSpacing(0)
        
                        # left_menu_bar_frame(
        self.left_menu_bar_frame = QFrame()
        self.left_menu_bar_frame.setFrameShape(QFrame.NoFrame)
        self.left_menu_bar_frame.setMinimumWidth(self.theme_settings["left_menu_size"]["bg_width_minimum"])
        self.left_menu_bar_frame.setMaximumWidth(self.theme_settings["left_menu_size"]["bg_width_minimum"])
        self.left_menu_bar_vlayout = QVBoxLayout(self.left_menu_bar_frame)
        self.left_menu_bar_vlayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bar_vlayout.setSpacing(0)
                            # Left_Menu(
        self.left_menu = Ui_Left_Menu_Column_Widget(
            app_parent = UiMainWindow,
            parent = self.left_menu_bar_frame,
            time_animation = self.theme_settings["time_animation"],
            minimum_width = self.theme_settings["left_menu_size"]["bg_width_minimum"],
            maximum_width = self.theme_settings["left_menu_size"]["bg_width_maximum"],
            
            font_type = self.themes["font"]["family"],
            font_size = self.themes["font"]["left_menu_text_size"],
            bg_color = self.themes["app_color"]["bg_one"],

            left_menu_bar_btn_size = self.theme_settings["left_menu_size"]["btn_size"],
            left_menu_bar_btn_radius = self.theme_settings["left_menu_size"]["btn_radius"],

            left_menu_bar_text_color = self.themes["app_color"]["dark_three"],
            left_menu_bar_text_color_hover = self.themes["app_color"]["dark_two"],
            left_menu_bar_text_color_pressed = self.themes["app_color"]["dark_one"],
            
            left_menu_bar_bg_width_minimum = self.theme_settings["left_menu_size"]["bg_width_minimum"],
            left_menu_bar_bg_width_maximum = self.theme_settings["left_menu_size"]["bg_width_maximum"],
            left_menu_bar_bg_radius = self.theme_settings["left_menu_size"]["bg_radius"],
            left_menu_bar_bg_color = self.themes["app_color"]["bg_two"],
            left_menu_bar_bg_color_hover = self.themes["app_color"]["color_one"],
            left_menu_bar_bg_color_pressed = self.themes["app_color"]["color_three"]
        )
                            # )Left_Menu
        self.left_menu_bar_vlayout.addWidget(self.left_menu)
                        # )left_menu_bar_frame
                        # left_column_frame(
        self.left_column_frame = QFrame()
        self.left_column_frame.setMinimumWidth(self.theme_settings["left_column_size"]["minimum"])
        self.left_column_frame.setMaximumWidth(self.theme_settings["left_column_size"]["minimum"])
        self.left_column_hlayout = QHBoxLayout(self.left_column_frame)
                        # )left_column_frame
                        # main_page_frame(
        self.main_page_frame = QFrame()
        self.main_page_vlayout = QVBoxLayout(self.main_page_frame)
        self.main_page_vlayout.setContentsMargins(0, 0, 0, 0)
        self.main_page_vlayout.setSpacing(0)
                            # load_page(
        self.load_pages = MainPages(
            app_parent = UiMainWindow,
        )
                            # )load_page
        self.main_page_vlayout.addWidget(self.load_pages)
                        # )main_page_frame
                        # right_settings_column_Frame(
        self.right_column_frame = QFrame()
        self.right_column_frame.setMinimumWidth(self.theme_settings["right_column_size"]["minimum"])
        self.right_column_frame.setMaximumWidth(self.theme_settings["right_column_size"]["minimum"])
        self.right_column_frame.setStyleSheet("background-color: lightblue")
        self.right_column_hlayout = QHBoxLayout(self.right_column_frame)
        
                        # )right_settings_column_Frame
        self.not_title_bar_hlayout.addWidget(self.left_menu_bar_frame)
        self.not_title_bar_hlayout.addWidget(self.main_page_frame)
        self.not_title_bar_hlayout.addWidget(self.right_column_frame)
                    # )not_title_bar_frame
        self.window.vlayout.addWidget(self.title_bar_frame)
        self.window.vlayout.addWidget(self.not_title_bar_frame)
        
                # )PyWindow
        self.centralwidget_vlayout.addWidget(self.window)
            # )Centralwidget
        UiMainWindow.setCentralWidget(self.centralwidget)
        # )MainWindow

    

        