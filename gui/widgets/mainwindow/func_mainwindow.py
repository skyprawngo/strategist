from gui.widgets.mainwindow.mainwindow import *

class MainFunctions():
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    def set_page(self, page):
        self.ui.load_pages.setCurrentWidget(page)
        
    def get_title_bar_btn(self, object_name):
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    def get_left_menu_btn(self, object_name):
        return self.ui.left_menu.findChild(QPushButton, object_name)
    
    # SET left_column
    def set_left_column_menu(
        self,
        menu,
        title,
        icon_path
    ):
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)
            
    # SET right_column
    def set_right_column_menu(self, menu):
        self.ui.right_column.menus.setCurrentWidget(menu)
    
    # VISIBLE left_column 
    def left_column_is_visible(self):
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # VISIBLE right_column 
    def right_column_is_visible(self):
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # TOGGLE left_column
    def toggle_left_column(self):
        # GET ACTUAL CLUMNS SIZE
        left_column_width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, right_column_width, "left")
        
    # TOGGLE right_column
    def toggle_right_column(self):
        # GET ACTUAL CLUMNS SIZE
        left_column_width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, right_column_width, "right")
        
    def start_frame_animation(self, left_frame_width, right_frame_width, direction):
        right_width = 0
        left_width = 0
        time_animation = self.ui.theme_settings["time_animation"]
        minimum_left = self.ui.theme_settings["left_menu_size"]["minimum"]
        maximum_left = self.ui.theme_settings["left_menu_size"]["maximum"]
        minimum_right = self.ui.theme_settings["right_column_size"]["minimum"]
        maximum_right = self.ui.theme_settings["right_column_size"]["maximum"]

        # Check Left Values        
        if left_frame_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # Check Right values        
        if right_frame_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.left_menu_bar_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_frame_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_frame_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()