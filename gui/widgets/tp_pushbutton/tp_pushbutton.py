# PySide6 Module Import
from module.pyside6_module_import import *

# Pushbutton_Template
class Tp_PushButton(QPushButton):
    clicked = Signal
    released = Signal
    _on = Signal
    _off = Signal
    
    def __init__(
        self,
        parent,
        app_parent,
        btn_id = "",
        btn_layout = "vlayout",
        btn_sizepolicy = [QSizePolicy.Preferred, QSizePolicy.Preferred],
        btn_size = [None, None],
        
        icon_file_path = "",
        icon_size = [50, 50],
        
        tooltip_text = "",
        tooltip_position = [0, 0],

        bg_one = "#e0e3ea",
        bg_two = "#f5f6fa",
        bg_three = "#fff",
        
        color_one = "#b9cefe",
        color_two = "#8aadff",
        color_three = "#6c98fe",
        
        icon_color_one = "#000000",
        icon_color_two = "#000000",
        icon_color_three = "#000000",

        is_toggle_btn = False,
        is_tooltip_btn = False,
        btn_toggled = False,
    ):
        super().__init__()
        self._parent = parent
        self.app_parent = app_parent
        self.btn_id = btn_id
        self.btn_layout = btn_layout
        self.btn_sizepolicy = btn_sizepolicy
        self.btn_size = btn_size
        
        self.icon_file_path = icon_file_path
        self.icon_size = icon_size
        
        self.tooltip_text = tooltip_text
        self.tooltip_position = tooltip_position
        
        self.bg_one = bg_one # btn bg color
        self.bg_two = bg_two # tooltip bg color
        self.bg_three = bg_three 
        
        self.color_one = color_one # btn hover color
        self.color_two = color_two
        self.color_three = color_three # btn pressed color
        
        self.icon_color_one = icon_color_one # tooltip text color
        self.icon_color_two = icon_color_two,
        self.icon_color_three = icon_color_three,
        
        self.is_toggle_btn = is_toggle_btn,
        self.is_tooltip_btn = is_tooltip_btn,
        self.btn_toggled = btn_toggled,
        
        self.setup_Ui()
    
    def setup_Ui(self):
        self.setObjectName(self.btn_id)
        self.setCursor(Qt.PointingHandCursor)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setSizePolicy(self.btn_sizepolicy[0],self.btn_sizepolicy[1])
        self.setStyleSheet(f"background-color: {self.bg_one}")
        
        if self.btn_layout == "vlayout":
            self._layout = QVBoxLayout(self)
        elif self.btn_layout == "hlayout":
            self._layout = QHBoxLayout(self)

        self.btn_image = QSvgWidget()
        self.btn_image.setFixedSize(self.icon_size[0], self.icon_size[1])
        self.set_icon(self.icon_file_path)
        self._layout.addWidget(self.btn_image)
        
        self.btn_text = QLabel()
        self.btn_text.setText(self.tooltip_text)
        self._layout.addWidget(self.btn_text)
        self.btn_text.hide()
        
        self.label_tooltip = Btn_ToolTip(
            app_parent = self.app_parent,
            tooltip_text = self.tooltip_text,
            tooltip_text_color = self.icon_color_one,
            tooltip_bg_color= self.bg_two
        )
        self.set_tooltip(self.is_tooltip_btn)
            
        # self.setIcon(QIcon(self.icon_file_path).pixmap(QSize(self.icon_size[0], self.icon_size[1])))
        
    def changeStyle(self, event):
        if event == QEvent.Enter:
            self.set_btn_bg_color = self.color_one
            self.btnStyle()
        elif event == QEvent.Leave:
            if self.is_toggle_btn:
                if self.btn_toggled:
                    self.set_btn_bg_color = self.color_three
                elif not self.btn_toggled:
                    self.set_btn_bg_color = self.bg_one
            elif not self.is_toggle_btn:
                self.set_btn_bg_color = self.bg_one
            self.btnStyle()
        elif event == QEvent.MouseButtonPress:
            if self.is_toggle_btn:
                if self.btn_toggled:
                    self.btn_toggled = False
                    self.set_btn_bg_color = self.color_one
                    self._off.emit()
                elif not self.btn_toggled:
                    self.btn_toggled = True
                    self.set_btn_bg_color = self.color_three
                    self._on.emit()
            elif not self.is_toggle_btn:
                self.set_btn_bg_color = self.color_three
            self.btnStyle()
        elif event == QEvent.MouseButtonRelease:
            pass
    
    def btnStyle(self):
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(f'''
            background-color: {self.set_btn_bg_color};
        ''')
    
    def enterEvent(self, event):
        self.changeStyle(QEvent.Enter)

    def leaveEvent(self, event):
        self.changeStyle(QEvent.Leave)
    
    def mousePressEvent(self, event):
        self.changeStyle(QEvent.MouseButtonPress)
        self.clicked.emit()
    
    def mouseReleaseEvent(self, event):
        self.changStyle(QEvent.MouseButtonRelease)
        self.released.emit()
                
    def set_icon(self, icon_file_path):
        self.btn_image.load(icon_file_path)
        
    def set_text(self, text_appear):
        if text_appear:
            self.btn_text.show()
        else:
            self.btn_text.hide()

    def set_toggled(self, set):
        self.btn_toggled = not set
        self.changeStyle(QEvent.MouseButtonPress)
        pass
    
    def set_tooltip(self, set):
        self.is_tooltip_btn = set
        if self.is_tooltip_btn:
            self.label_tooltip.show()
        elif not self.is_tooltip_btn:
            self.label_tooltip.hide()
        pass

    def move_tooltip(self):
        # GET MAIN WINDOW PARENT
        gp = self.mapToGlobal(QPoint(0, 0))

        # SET WIDGET TO GET POSTION
        # Return absolute position of widget inside app
        pos = self._parent.mapFromGlobal(gp)

        # FORMAT POSITION
        # Adjust tooltip position with offset
        pos_x = pos.x() + self.tooltip_position[0]
        pos_y = pos.y() + self.tooltip_position[1]
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
