# -*- coding: utf-8 -*-


from gui.module_import import *

from gui.themes.settings import Settings

from gui.themes.themes import Themes

from gui.themes.theme_switch import ThemeSwitch

from gui.widgets.left_menu_column.ui_menu_bar import Ui_menu_bar_Form

from gui.widgets.title_bar.title_bar import Ui_Title_Bar_Widget


class Ui_MainWindow(object):
    def setupUi(self, UiMainWindow):
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
        
        
        self.centralwidget = QWidget(UiMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.centralwidget.setStyleSheet(f'background-color: {self.themes["app_color"]["bg_one"]};')
        self.centralwidget_vlayout = QVBoxLayout(self.centralwidget)
        self.centralwidget_vlayout.setSpacing(0)
        self.centralwidget_vlayout.setObjectName(u"centralwidget_vlayout")
        self.centralwidget_vlayout.setContentsMargins(0, 0, 0, 0)
        
        # Import Title Bar
        # /////////////////////////////////////////////////////////////////////
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.title_bar = Ui_Title_Bar_Widget(
                        UiMainWindow,
                        app_name = self.settings["app_name"],
                        custom_title_bar = self.settings["custom_title_bar"],
                        time_animation = self.settings["time_animation"],
                        font_type = self.settings["font"]["family"],
                        font_size = self.settings["font"]["title_size"]
        )

                
        self.title_bar.setupUi(self.title_bar_frame)
        self.centralwidget_vlayout.addWidget(self.title_bar_frame)
        # /////////////////////////////////////////////////////////////////////

        self.not_title_bar_frame = QFrame(self.centralwidget)
        self.not_title_bar_frame.setObjectName(u"not_title_bar_frame")
        self.not_title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.not_title_bar_frame.setFrameShadow(QFrame.Raised)
        self.not_title_bar_hlayout = QHBoxLayout(self.not_title_bar_frame)
        self.not_title_bar_hlayout.setSpacing(0)
        self.not_title_bar_hlayout.setObjectName(u"not_title_bar_hlayout")
        self.not_title_bar_hlayout.setContentsMargins(0, 0, 0, 0)
        
        # Import Menu Bar
        # /////////////////////////////////////////////////////////////////////
        self.menu_bar_frame = QFrame()
        self.menu_bar_frame.setFrameShape(QFrame.NoFrame)
        self.menu_bar = Ui_menu_bar_Form()
        self.menu_bar.setupUi(self.menu_bar_frame)
        self.not_title_bar_hlayout.addWidget(self.menu_bar_frame)
        # /////////////////////////////////////////////////////////////////////
        
        self.menu_bar_frame = QFrame(self.not_title_bar_frame)
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

        self.main_page_frame = QFrame(self.not_title_bar_frame)
        self.main_page_frame.setObjectName(u"main_page_frame")
        self.main_page_frame.setFrameShape(QFrame.NoFrame)
        self.main_page_frame.setFrameShadow(QFrame.Raised)

        self.not_title_bar_hlayout.addWidget(self.main_page_frame)


        self.centralwidget_vlayout.addWidget(self.not_title_bar_frame)

        UiMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UiMainWindow)

        QMetaObject.connectSlotsByName(UiMainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi
