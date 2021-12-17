# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowjMVMsu.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from gui.module_import import *

from gui.widgets.left_menu_column.ui_menu_bar import Ui_menu_bar_Form

from gui.widgets.title_bar.title_bar import Ui_title_bar_form


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 895)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFocusPolicy(Qt.NoFocus)
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget_vlayout = QVBoxLayout(self.centralwidget)
        self.centralwidget_vlayout.setSpacing(0)
        self.centralwidget_vlayout.setObjectName(u"centralwidget_vlayout")
        self.centralwidget_vlayout.setContentsMargins(0, 0, 0, 0)
        
        # Import Title Bar
        # /////////////////////////////////////////////////////////////////////
        self.title_bar_frame = QFrame()
        self.title_bar_frame.setFrameShape(QFrame.NoFrame)
        self.title_bar = Ui_title_bar_form()
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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

