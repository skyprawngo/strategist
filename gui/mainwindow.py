# -*- coding: utf-8 -*-
from module.pyside6_module_import import *

from gui.themes.settings import Settings
from gui.themes.themes import Themes
from gui.themes.theme_switch import Theme_Switch


from gui.widgets.pywindow.pywindow import PyWindow
from gui.widgets.title_bar.title_bar import Ui_Title_Bar_Widget
from gui.widgets.left_menu.left_menu_bar import Ui_Left_Menu_Column_Widget



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

        self.app_parent = UiMainWindow
        
        UiMainWindow.resize(
            self.settings["startup_size"][0],
            self.settings["startup_size"][1]
        )
        
        UiMainWindow.setMinimumSize(
            self.settings["minimum_size"][0],
            self.settings["minimum_size"][1]
        )
        


        self.app_parent = UiMainWindow


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
                # PyWindow(
        self.window = PyWindow(
            app_parent = UiMainWindow,
            startup_size = self.settings["startup_size"],
            minimum_size = self.settings["minimum_size"],

            margin = self.themes["shape"]["pywindow"]["margin"],
            spacing = self.themes["shape"]["pywindow"]["margin"],
            bg_color = self.themes["app_color"]["bg_one"],
            text_color = self.themes["app_color"]["dark_one"],
            text_font_size = self.themes["font"]["text_size"],
            border_radius = self.themes["shape"]["pywindow"]["border_radius"],
            border_size = self.themes["shape"]["pywindow"]["border_size"],
            border_color = self.themes["app_color"]["bg_three"],
            custom_title_bar = self.settings["custom_title_bar"]
        )

                    # title_bar_frame(
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.title_bar_frame.setMinimumHeight(self.themes["shape"]["title_bar"]["bg_height"])
        self.title_bar_frame.setMaximumHeight(self.themes["shape"]["title_bar"]["bg_height"])
        self.title_bar_vlayout = QVBoxLayout(self.title_bar_frame)
        self.title_bar_vlayout.setContentsMargins(5, 5, 5, 0)
                    
                        # Title_Bar_Widget(
        self.title_bar_widget = Ui_Title_Bar_Widget(
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
                        # )Title_Bar_Widget
        self.title_bar_vlayout.addWidget(self.title_bar_widget)
                    # )title_bar_frame

                    # not_title_bar_frame(
        self.not_title_bar_frame = QFrame()
        self.not_title_bar_frame.setObjectName(u"not_title_bar_frame")
        self.not_title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.not_title_bar_frame.setFrameShadow(QFrame.Raised)
        self.not_title_bar_hlayout = QHBoxLayout(self.not_title_bar_frame)
        self.not_title_bar_hlayout.setObjectName(u"not_title_bar_hlayout")
        self.not_title_bar_hlayout.setContentsMargins(5, 5, 5, 5)
        self.not_title_bar_hlayout.setSpacing(0)
        
                        # left_menu_bar_frame(
        self.left_menu_bar_frame = QFrame()
        self.left_menu_bar_frame.setFrameShape(QFrame.NoFrame)
        self.left_menu_bar_frame.setMinimumWidth(self.themes["shape"]["left_menu_bar"]["bg_width"])
        self.left_menu_bar_frame.setMaximumWidth(self.themes["shape"]["left_menu_bar"]["bg_width"])
        self.left_menu_bar_vlayout = QVBoxLayout(self.left_menu_bar_frame)
        self.left_menu_bar_vlayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bar_vlayout.setSpacing(0)
                            # Left_Menu_Bar_Widget(
        self.left_menu_bar_widget = Ui_Left_Menu_Column_Widget(
            app_parent = UiMainWindow,
            parent = self.left_menu_bar_frame,
            time_animation = self.settings["time_animation"],
            minimum_width = self.settings["left_menu_size"]["minimum"],
            maximum_width = self.settings["left_menu_size"]["maximum"],
            
            font_type = self.themes["font"]["family"],
            font_size = self.themes["font"]["text_size"],
            bg_color = self.themes["app_color"]["bg_one"],

            left_menu_bar_btn_size = self.themes["shape"]["left_menu_bar"]["btn_size"],
            left_menu_bar_btn_radius = self.themes["shape"]["left_menu_bar"]["btn_radius"],

            left_menu_bar_text_color = self.themes["app_color"]["dark_three"],
            left_menu_bar_text_color_hover = self.themes["app_color"]["dark_two"],
            left_menu_bar_text_color_pressed = self.themes["app_color"]["dark_one"],
            
            left_menu_bar_bg_width = self.themes["shape"]["left_menu_bar"]["bg_width"],
            left_menu_bar_bg_radius = self.themes["shape"]["left_menu_bar"]["bg_radius"],
            left_menu_bar_bg_color = self.themes["app_color"]["bg_two"],
            left_menu_bar_bg_color_hover = self.themes["app_color"]["bg_three"],
            left_menu_bar_bg_color_pressed = self.themes["app_color"]["bg_four"]
        )
                            # )Left_Menu_Bar_Widget
        self.left_menu_bar_vlayout.addWidget(self.left_menu_bar_widget)
                        # )left_menu_bar_frame
                        # left_column_frame(
        self.left_column_frame = QFrame()
        self.left_column_frame.setMinimumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_frame.setMaximumWidth(self.settings["left_column_size"]["minimum"])
        self.left_column_hlayout = QHBoxLayout(self.left_column_frame)
                        # )left_column_frame
                        # main_page_frame(
        self.main_page_frame = QFrame()
        self.main_page_vlayout = QVBoxLayout(self.main_page_frame)
                        # )main_page_frame
                        # right_settings_column_Frame(
        self.right_column_frame = QFrame()
        self.right_column_frame.setMinimumWidth(self.settings["right_column_size"]["minimum"])
        self.right_column_frame.setMaximumWidth(self.settings["right_column_size"]["minimum"])
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

    

        