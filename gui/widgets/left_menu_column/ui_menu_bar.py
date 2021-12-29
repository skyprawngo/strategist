# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_barEvENta.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from module.pyside6_module_import import *

class Ui_Menu_Bar_Widget(object):
    def setupUi(self, menu_bar_Form):
        if not menu_bar_Form.objectName():
            menu_bar_Form.setObjectName(u"menu_bar_Form")
        menu_bar_Form.resize(100, 902)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu_bar_Form.sizePolicy().hasHeightForWidth())
        menu_bar_Form.setSizePolicy(sizePolicy)
        menu_bar_Form.setMinimumSize(QSize(40, 0))
        menu_bar_Form.setMaximumSize(QSize(100, 16777215))
        self.menu_bar_form_vlayout = QVBoxLayout(menu_bar_Form)
        self.menu_bar_form_vlayout.setSpacing(0)
        self.menu_bar_form_vlayout.setObjectName(u"menu_bar_form_vlayout")
        self.menu_bar_form_vlayout.setContentsMargins(0, 0, 0, 0)
        self.menu_bar_frame = QFrame(menu_bar_Form)
        self.menu_bar_frame.setObjectName(u"menu_bar_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_bar_frame.sizePolicy().hasHeightForWidth())
        self.menu_bar_frame.setSizePolicy(sizePolicy1)
        self.menu_bar_frame.setMinimumSize(QSize(40, 0))
        self.menu_bar_frame.setMaximumSize(QSize(40, 16777215))
        self.menu_bar_frame.setStyleSheet(u"background-color: rgb(245, 251, 255)")
        self.menu_bar_frame.setFrameShape(QFrame.NoFrame)
        self.menu_bar_frame.setFrameShadow(QFrame.Raised)
        self.menu_bar_vlayout = QVBoxLayout(self.menu_bar_frame)
        self.menu_bar_vlayout.setSpacing(0)
        self.menu_bar_vlayout.setObjectName(u"menu_bar_vlayout")
        self.menu_bar_vlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_togle_menu_frame = QFrame(self.menu_bar_frame)
        self.btn_togle_menu_frame.setObjectName(u"btn_togle_menu_frame")
        self.btn_togle_menu_frame.setMaximumSize(QSize(16777215, 40))
        self.btn_togle_menu_frame.setStyleSheet(u"background-color: rgb(245, 251, 255);\n"
"")
        self.btn_togle_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_togle_menu_frame.setFrameShadow(QFrame.Raised)
        self.btn_toggle_menu_layout = QVBoxLayout(self.btn_togle_menu_frame)
        self.btn_toggle_menu_layout.setSpacing(0)
        self.btn_toggle_menu_layout.setObjectName(u"btn_toggle_menu_layout")
        self.btn_toggle_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.btn_togle_menu_frame)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy2)
        self.btn_toggle_menu.setMinimumSize(QSize(0, 40))
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icon/images/icons/icon_menu.png);\n"
"	border:none;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(215, 225, 244);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(187, 204, 236);\n"
"}")

        self.btn_toggle_menu_layout.addWidget(self.btn_toggle_menu)


        self.menu_bar_vlayout.addWidget(self.btn_togle_menu_frame)

        self.btn_menu_frame = QFrame(self.menu_bar_frame)
        self.btn_menu_frame.setObjectName(u"btn_menu_frame")
        self.btn_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_menu_frame.setFrameShadow(QFrame.Raised)
        self.btn_menu_vlayout = QVBoxLayout(self.btn_menu_frame)
        self.btn_menu_vlayout.setSpacing(0)
        self.btn_menu_vlayout.setObjectName(u"btn_menu_vlayout")
        self.btn_menu_vlayout.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.btn_menu_frame)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy2.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy2)
        self.btn_home.setMinimumSize(QSize(0, 40))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icon/images/icons/cil-home.png);\n"
"	border:none;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(215, 225, 244);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(187, 204, 236);\n"
"}")

        self.btn_menu_vlayout.addWidget(self.btn_home)

        self.btn_chart = QPushButton(self.btn_menu_frame)
        self.btn_chart.setObjectName(u"btn_chart")
        sizePolicy2.setHeightForWidth(self.btn_chart.sizePolicy().hasHeightForWidth())
        self.btn_chart.setSizePolicy(sizePolicy2)
        self.btn_chart.setMinimumSize(QSize(0, 40))
        self.btn_chart.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icon/images/icons/cil-chart.png);\n"
"	border:none;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(215, 225, 244);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(187, 204, 236);\n"
"}")

        self.btn_menu_vlayout.addWidget(self.btn_chart)

        self.btn_graph = QPushButton(self.btn_menu_frame)
        self.btn_graph.setObjectName(u"btn_graph")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_graph.sizePolicy().hasHeightForWidth())
        self.btn_graph.setSizePolicy(sizePolicy3)
        self.btn_graph.setMinimumSize(QSize(0, 40))
        self.btn_graph.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icon/images/icons/cil-chart-line.png);\n"
"	border:none;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(215, 225, 244);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(187, 204, 236);\n"
"}")

        self.btn_menu_vlayout.addWidget(self.btn_graph)

        self.btn_shopping = QPushButton(self.btn_menu_frame)
        self.btn_shopping.setObjectName(u"btn_shopping")
        sizePolicy3.setHeightForWidth(self.btn_shopping.sizePolicy().hasHeightForWidth())
        self.btn_shopping.setSizePolicy(sizePolicy3)
        self.btn_shopping.setMinimumSize(QSize(0, 40))
        self.btn_shopping.setStyleSheet(u"QPushButton {\n"
"	image: url(:/icon/images/icons/cil-cart.png);\n"
"	border:none;	\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(215, 225, 244);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(187, 204, 236);\n"
"}")

        self.btn_menu_vlayout.addWidget(self.btn_shopping)


        self.menu_bar_vlayout.addWidget(self.btn_menu_frame, 0, Qt.AlignTop)


        self.menu_bar_form_vlayout.addWidget(self.menu_bar_frame)


        self.retranslateUi(menu_bar_Form)

        QMetaObject.connectSlotsByName(menu_bar_Form)
    # setupUi

    def retranslateUi(self, menu_bar_Form):
        menu_bar_Form.setWindowTitle(QCoreApplication.translate("menu_bar_Form", u"Form", None))
        self.btn_toggle_menu.setText("")
        self.btn_home.setText("")
        self.btn_chart.setText("")
        self.btn_graph.setText("")
        self.btn_shopping.setText("")
    # retranslateUi

