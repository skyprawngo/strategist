

from gui.module_import import *

class Title_Button(QPushButton):
    def __init__(
        self,
        parent,
        app_parent,
        icon_file_path,
        tooltip_text = "abcd",

        btn_size = [25, 25],
        btn_radius = 8,

        btn_bg_color = "#ffffff",
        btn_bg_color_hover = "#ffffff",
        btn_bg_color_pressed = "#ffffff",

        btn_icon_color = "#000000",
        btn_icon_color_hover = "#000000",
        btn_icon_color_pressed = "#000000",

    ):
        super().__init__()
        
        self.parent = parent
        self.app_parent = app_parent

        self.icon_file_path = icon_file_path
        self.tooltip_text = tooltip_text

        self.setFixedSize(btn_size[0], btn_size[1])
        self.btn_radius = btn_radius
        
        
        self.btn_bg_color = btn_bg_color
        self.btn_bg_color_hover = btn_bg_color_hover
        self.btn_bg_color_pressed = btn_bg_color_pressed

        self.btn_icon_color = btn_icon_color
        self.btn_icon_color_hover = btn_icon_color_hover
        self.btn_icon_color_pressed = btn_icon_color_pressed

        
        self.setCursor(Qt.PointingHandCursor)

        self.btn_image = QIcon()
        self.btn_image.addFile(self.icon_file_path)
        self.setIcon(self.btn_image)
        self.setIconSize(QSize(btn_size[0],btn_size[1]))

        self.label_tooltip = Btn_Tooltip(
            app_parent,
            tooltip_text = self.tooltip_text,
            tooltip_text_color = self.btn_icon_color,
            tooltip_bg_color = self.btn_bg_color
        )
        # self.label_tooltip.hide()

    
    def enterEvent(self, event):
        self.move_tooltip()
        self.label_tooltip.show()
        print("들어옴")
    
    def leaveEvent(self, event):
        self.move_tooltip()
        self.label_tooltip.hide()
        print("나감")

    def move_tooltip(self):
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSTION
        # Return absolute position of widget inside app
        pos = self.parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        pos_x = (pos.x() - self.label_tooltip.width()) + self.width() + 5
        pos_y = pos.y() + self.height() + 6

        # SET POSITION TO WIDGET
        # Move tooltip position
        self.label_tooltip.move(pos_x, pos_y)

class Btn_Tooltip(QLabel):
    style_tooltip = """ 
    QLabel {{		
        background-color: {tooltip_bg_color};	
        color: {tooltip_text_color};
        padding-left: 10px;
        padding-right: 10px;
        border-radius: 17px;
        border: 0px solid transparent;
    }}
    """    
    def __init__(
        self,
        app_parent, 
        tooltip_text,
        tooltip_text_color,
        tooltip_bg_color
    ):
        QLabel.__init__(self)

        # LABEL SETUP
        style = self.style_tooltip.format(
            tooltip_bg_color = tooltip_bg_color,
            tooltip_text_color = tooltip_text_color
        )
        self.setObjectName(u"label_tooltip")
        self.setStyleSheet(style)
        self.setMinimumHeight(34)
        self.setParent(app_parent)
        self.setText(tooltip_text)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)