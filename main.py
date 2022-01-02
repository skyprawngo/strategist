import sys
import os

from module.pyside6_module_import import *

from gui.widgets.mainwindow.mainwindow import Ui_MainWindow
from gui.widgets.mainwindow.setup_mainwindow import Setup_MainWindow
from gui.widgets.mainwindow.func_mainwindow import MainFunctions


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        Setup_MainWindow.setup_gui(self)

        
        Setup_MainWindow.login_window_appear(self)
    
    

    def btn_clicked(self):
        btn = Setup_MainWindow.setup_btns(self)
        
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()
        
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)
        
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_0_frame)
        
        if btn.objectName() == "btn_chart":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_1_frame)
        
        if btn.objectName() == "btn_purchased":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2_frame)
        
        if btn.objectName() == "btn_shop":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_3_frame)
            
    
    def resizeEvent(self, event):
        Setup_MainWindow.resize_grips(self)

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        p = event.globalPosition()
        globalPos = p.toPoint()
        self.dragPos = globalPos
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    # window.show()
    app.exec()