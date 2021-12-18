# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'title_barXZOjAB.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from gui.module_import import *



class Ui_title_bar_form(object):
    def __init__(
            self,
            UiMainWindow,
            app_name = "Strategist",
            custom_title_bar = None,
            time_animation = 500,
            font_type = "Segoe_UI",
            font_size = 10
    ):
        super().__init__()
        
        self.app_name = app_name
        self.custom_tilte_bar = custom_title_bar
        self.time_animation = time_animation
        self.font_type = font_type
        self.font_size = font_size
        
    
    def setupUi(self, title_bar_form):
        if not title_bar_form.objectName():
            title_bar_form.setObjectName(u"title_bar_form")
        title_bar_form.resize(1168, 24)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(title_bar_form.sizePolicy().hasHeightForWidth())
        title_bar_form.setSizePolicy(sizePolicy)
        title_bar_form.setMinimumSize(QSize(0, 24))
        title_bar_form.setMaximumSize(QSize(16777215, 24))
        self.horizontalLayout = QHBoxLayout(title_bar_form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar_frame = QFrame(title_bar_form)
        self.title_bar_frame.setObjectName(u"title_bar_frame")
        self.title_bar_frame.setMaximumSize(QSize(16777215, 24))
        self.title_bar_frame.setStyleSheet(u"background-color: rgb(245, 251, 255)")
        self.title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.title_bar_frame.setFrameShadow(QFrame.Raised)
        self.title_bar_hlayout = QHBoxLayout(self.title_bar_frame)
        self.title_bar_hlayout.setSpacing(0)
        self.title_bar_hlayout.setObjectName(u"title_bar_hlayout")
        self.title_bar_hlayout.setContentsMargins(0, 0, 0, 0)
        self.logo_n_title_frame = QFrame(self.title_bar_frame)
        self.logo_n_title_frame.setObjectName(u"logo_n_title_frame")
        self.logo_n_title_frame.setFrameShape(QFrame.NoFrame)
        self.logo_n_title_frame.setFrameShadow(QFrame.Raised)
        self.logo_n_title_layout = QHBoxLayout(self.logo_n_title_frame)
        self.logo_n_title_layout.setSpacing(0)
        self.logo_n_title_layout.setObjectName(u"logo_n_title_layout")
        self.logo_n_title_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_widget = QWidget(self.logo_n_title_frame)
        self.logo_widget.setObjectName(u"logo_widget")
        self.logo_widget.setMaximumSize(QSize(100, 16777215))
        self.logo_widget.setStyleSheet(u"border-image: url(:/image/images/images/logo.png) 0 0 0 0 stretch stretch;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"\n"
"")

        self.logo_n_title_layout.addWidget(self.logo_widget)

        self.title_frame = QFrame(self.logo_n_title_frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)

        self.logo_n_title_layout.addWidget(self.title_frame)


        self.title_bar_hlayout.addWidget(self.logo_n_title_frame)

        self.btn_window_frame = QFrame(self.title_bar_frame)
        self.btn_window_frame.setObjectName(u"btn_window_frame")
        self.btn_window_frame.setMaximumSize(QSize(100, 16777215))
        self.btn_window_frame.setStyleSheet(u"")
        self.btn_window_frame.setFrameShape(QFrame.NoFrame)
        self.btn_window_frame.setFrameShadow(QFrame.Raised)
        self.btn_window_hlayout = QHBoxLayout(self.btn_window_frame)
        self.btn_window_hlayout.setSpacing(0)
        self.btn_window_hlayout.setObjectName(u"btn_window_hlayout")
        self.btn_window_hlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.btn_window_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icon/images/icons/icon_minimize.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	border:none;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(215, 225, 244);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(187, 204, 236);\n"
"}")

        self.btn_window_hlayout.addWidget(self.btn_minimize)

        self.btn_maxi_n_undo = QPushButton(self.btn_window_frame)
        self.btn_maxi_n_undo.setObjectName(u"btn_maxi_n_undo")
        sizePolicy1.setHeightForWidth(self.btn_maxi_n_undo.sizePolicy().hasHeightForWidth())
        self.btn_maxi_n_undo.setSizePolicy(sizePolicy1)
        self.btn_maxi_n_undo.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icon/images/icons/icon_restore.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	border:none;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(215, 225, 244);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(187, 204, 236);\n"
"}")

        self.btn_window_hlayout.addWidget(self.btn_maxi_n_undo)

        self.btn_close = QPushButton(self.btn_window_frame)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/icon/images/icons/icon_close.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	border:none;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(245, 80, 72);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(245, 80, 72);\n"
"}")

        self.btn_window_hlayout.addWidget(self.btn_close)


        self.title_bar_hlayout.addWidget(self.btn_window_frame)


        self.horizontalLayout.addWidget(self.title_bar_frame)


        self.retranslateUi(title_bar_form)

        QMetaObject.connectSlotsByName(title_bar_form)
    # setupUi

    def retranslateUi(self, title_bar_form):
        title_bar_form.setWindowTitle(QCoreApplication.translate("title_bar_form", u"Form", None))
        self.btn_minimize.setText("")
        self.btn_maxi_n_undo.setText("")
        self.btn_close.setText("")
    # retranslateUi

