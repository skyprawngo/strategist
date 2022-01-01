from module.pyside6_module_import import *

class MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"Form")
        self.verticalLayout = QVBoxLayout(MainPages)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"stackedWidget")
        
        self.page_0 = QWidget()
        self.page_0.setStyleSheet("background-color: lightblue")
        self.page_0.setObjectName(u"page_1")
        self.pages.addWidget(self.page_0)
        
        self.page_1 = QWidget()
        self.page_1.setStyleSheet("background-color: orange")
        self.page_1.setObjectName(u"page_1")
        self.pages.addWidget(self.page_1)
        self.verticalLayout.addWidget(self.pages)

        self.page_2 = QWidget()
        self.page_2.setStyleSheet("background-color: lightgreen")
        self.page_2.setObjectName(u"page_2")
        self.pages.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.pages)

        self.retranslateUi(MainPages)

        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

