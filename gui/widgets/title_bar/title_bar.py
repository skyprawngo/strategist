# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'title_barXZOjAB.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from gui.module_import import *

from gui.themes.load_item_path import Load_Item_Path

class Ui_Title_Bar_Widget(QWidget):
    def __init__(
            self,
            UiMainWindow,
            app_name = "Strategist",
            logo_file_name = "logo_top.svg",
            title_text = "",
            custom_title_bar = None,
            title_bar_height = 30,
            time_animation = 500,
            
            font_type = "Segoe_UI",
            font_size = 10,
    ):
        super().__init__()
        
        self.app_name = app_name
        self.logo_file_name = logo_file_name
        self.title_text = title_text
        self.custom_tilte_bar = custom_title_bar
        self.title_bar_height = title_bar_height
        self.time_animation = time_animation
        
        self.font_type = font_type
        self.font_size = font_size
        
        self.setupUi()
        
    
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
        self.top_logo_label.setMaximumSize(85, 30)
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
        self.title_label.setStyleSheet("background-color: lightblue")
        self.title_label.setText(self.title_text)
        self.title_label.setFont(self.font_type)
                # )
        self.title_hlayout.addWidget(self.title_label)
        
                # title_buttons_frame(
        self.title_buttons_frame = QFrame()
        self.title_buttons_hlayout = QHBoxLayout(self.title_buttons_frame)
        self.title_buttons_hlayout.setContentsMargins(0, 0, 0, 0)
        self.title_buttons_hlayout.setSpacing(0)
        
                # )
        self.title_hlayout.addWidget(self.title_buttons_frame)
            # )
        self.title_bar_hlayout.addWidget(self.title_frame)
        # )
        self.title_bar_widget_vlayout.addWidget(self.title_bar_frame)

