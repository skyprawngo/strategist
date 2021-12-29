

from module.pyside6_module_import import *


class Left_Menu_Button(QPushButton):
    clicked = QEvent
    released = QEvent
    toggled_name = ""
    
    def __init__(
        self,
        parent,
        app_parent,
        icon_file_path,
        tooltip_text = "abcd",

        btn_istoggle = False,
        btn_isactive = False,
        btn_size = [30, 30],
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

        self.btn_istoggle = btn_istoggle
        self.btn_isactive = btn_isactive
        self.btn_size = btn_size
        self.btn_radius = btn_radius
        
        self.btn_bg_color = btn_bg_color
        self.btn_bg_color_hover = btn_bg_color_hover
        self.btn_bg_color_pressed = btn_bg_color_pressed

        self.btn_icon_color = btn_icon_color
        self.btn_icon_color_hover = btn_icon_color_hover
        self.btn_icon_color_pressed = btn_icon_color_pressed


        self.set_btn_bg_color = btn_bg_color
        self.set_btn_bg_color_hover = btn_bg_color_hover
        self.set_btn_bg_color_pressed = btn_bg_color_pressed

        self.set_btn_icon_color = btn_icon_color
        self.set_btn_icon_color_hover = btn_icon_color_hover
        self.set_btn_icon_color_pressed = btn_icon_color_pressed
    



        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumSize(self.btn_size[0], self.btn_size[1]+12)


        self.set_icon(icon_file_path)
        self.set_label(tooltip_text)


    def set_icon(self, icon_file_path):
        self.btn_image = QIcon()
        self.btn_image.addFile(icon_file_path)
        self.setIconSize(QSize(self.btn_size[0],self.btn_size[1]))
        self.repaint()
        self.setIcon(self.btn_image)
    
    def set_label(self, tooltip_text):
        self.label_tooltip = Btn_ToolTip(
            self.app_parent,
            tooltip_text,
            self.btn_icon_color,
            self.btn_bg_color
        )
        self.label_tooltip.hide()
    
    def changetoggleStyle(self, event):
        if event == QEvent.Enter:
            if self.btn_isactive:
                pass
            elif not self.btn_isactive:
                self.set_btn_bg_color = self.btn_bg_color_hover
            self.btnStyle()
        elif event == QEvent.Leave:
            if self.btn_isactive:
                self.set_btn_bg_color = self.btn_bg_color_pressed
            elif not self.btn_isactive:
                self.set_btn_bg_color = self.btn_bg_color
            self.btnStyle()
        elif event == QEvent.MouseButtonPress:
            if self.btn_isactive:
                self.set_btn_bg_color = self.btn_bg_color_hover
                self.btn_isactive = False
            elif not self.btn_isactive:
                self.set_btn_bg_color = self.btn_bg_color_pressed
                self.btn_isactive = True
            self.btnStyle()
        elif event == QEvent.MouseButtonRelease:
            if self.btn_isactive:
                self.set_btn_bg_color = self.btn_bg_color_pressed
            elif not self.btn_isactive:
                self.set_btn_bg_color = self.btn_bg_color_hover

    def btnStyle(self):
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(f'''
            background-color: {self.set_btn_bg_color};
            border-radius: 5px;
        ''')


    def enterEvent(self, event):
        self.changetoggleStyle(QEvent.Enter)
        self.label_tooltip.show()
    
    def leaveEvent(self, event):
        self.changetoggleStyle(QEvent.Leave)
        self.label_tooltip.hide()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.changetoggleStyle(QEvent.MouseButtonPress)
            return self.clicked.emit()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.changetoggleStyle(QEvent.MouseButtonRelease)
            self.label_tooltip.hide()
            self.setFocus()
            return self.released.emit()
    
            


    def move_tooltip(self):
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSTION
        # Return absolute position of widget inside app
        pos = self.parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        pos_x = pos.x() + self.width() + 13
        pos_y = pos.y() + self.height() + 20
        # SET POSITION TO WIDGET
        # Move tooltip position
        self.label_tooltip.move(pos_x, pos_y)

class Btn_ToolTip(QLabel):
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