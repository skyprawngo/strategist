

from gui.module_import import *

class Title_Button(QPushButton):
    def __init__(
        self,
        parent,
        app_parent,
        icon_file_path,
        tooltip_text = "",
        btn_height = 30,
        radius = 8,

        btn_bg_color = "#ffffff",
        btn_bg_color_hover = "#ffffff",
        btn_bg_color_pressed = "#ffffff",

        btn_icon_color = "#000000",
        btn_icon_color_hover = "#000000",
        btn_icon_color_pressed = "#000000",

    ):
        super().__init__()
        
        self.setFixedSize(btn_height,btn_height)
        self.setCursor(Qt.PointingHandCursor)

        self.icon_file_path = icon_file_path
        self.tooltip_text = tooltip_text
        
        self.btn_bg_color = btn_bg_color
        self.btn_bg_color_hover = btn_bg_color_hover
        self.btn_bg_color_pressed = btn_bg_color_pressed

        self.btn_icon_color = btn_icon_color
        self.btn_icon_color_hover = btn_icon_color_hover
        self.btn_icon_color_pressed = btn_icon_color_pressed


        self.tooltip_text = tooltip_text
        self.btn_tooltip = Btn_Tooltip(
            parent,
            tooltip_text = self.tooltip_text,
            tooltip_text_color = self.btn_icon_color,
            tooltip_bg_color = self.btn_bg_color
        )
        self.btn_tooltip.hide()


    
    def enterEvent(self, event):
        self.btn_tooltip.show()
    
    def leaveEvent(self, event):
        self.btn_tooltip.hide()

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
        parent, 
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
        self.setParent(parent)
        self.setText(tooltip_text)
        self.adjustSize()

        # SET DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(self.shadow)