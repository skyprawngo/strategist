from module.pyside6_module_import import *
from gui.themes.load_item_path import Load_Item_Path


class TpWindow(QFrame):
    def __init__(
        self,
        app_parent,
        startup_size,
        minimum_size,
        margin = 0,
        spacing = 0,
        bg_color = "#fff",
        text_color = "#000",
        text_font_size = "9pt",
        border_radius = 10,
        border_size = 2,
        border_color = "#000",
        custom_title_bar = True,
        enable_shadow = True
    ):
        super().__init__()

        self.app_parent = app_parent
        self.margin = margin
        self.spacing = spacing
        self.bg_color = bg_color
        self.text_color = text_color
        self.text_font_size = text_font_size
        self.border_radius = border_radius
        self.border_size = border_size
        self.border_color = border_color
        self.custom_title_bar = custom_title_bar
        self.enable_shadow = enable_shadow

        self.setObjectName("pod_bg_app")

        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(margin, margin, margin, margin)
        self._layout.setSpacing(0)
        
        
        self.background = QSvgWidget()
        self.background.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.internal_bg_image = Load_Item_Path().set_svg_image_path("background_1000_600_1.svg")
        self.background.load(self.internal_bg_image)
        self.background.setStyleSheet(f"border-radius: {self.border_radius}")
        self._layout.addWidget(self.background)

        self.vlayout = QVBoxLayout(self.background)
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)

        self.set_stylesheet()
        if custom_title_bar:
            if enable_shadow:
                self.shadow = QGraphicsDropShadowEffect()
                self.shadow.setBlurRadius(20)
                self.shadow.setXOffset(0)
                self.shadow.setYOffset(0)
                self.shadow.setColor(QColor(0, 0, 0, 160))
                self.setGraphicsEffect(self.shadow)

    def set_stylesheet(
        self,
        bg_color = None,
        border_radius = None,
        border_size = None,
        border_color = None,
        text_color = None,
        text_font_size = None
    ):
        # CHECK BG COLOR
        if bg_color != None: internal_bg_color = bg_color
        else: internal_bg_color = self.bg_color

        # CHECK BORDER RADIUS
        if border_radius != None: internal_border_radius = border_radius
        else: internal_border_radius = self.border_radius

        # CHECK BORDER SIZE
        if border_size != None: internal_border_size = border_size
        else: internal_border_size = self.border_size

        # CHECK BORDER COLOR
        if text_color != None: internal_text_color = text_color
        else: internal_text_color = self.text_color

        # CHECK TEXT COLOR
        if border_color != None: internal_border_color = border_color
        else: internal_border_color = self.border_color

        # CHECK TEXT COLOR
        if text_font_size != None: internal_text_font_size = text_font_size
        else: internal_text_font_size = self.text_font_size

        self.setStyleSheet(Styles.bg_style.format(
            _bg_color = internal_bg_color,
            _border_radius = internal_border_radius,
            _border_size = internal_border_size,
            _border_color = internal_border_color,
            _text_color = internal_text_color,
            _text_font_size = internal_text_font_size
        ))

class Styles(object):
    bg_style = """
    #pod_bg_app {{
        background-color: {_bg_color};
        border-radius: {_border_radius};
        border: {_border_size}px solid {_border_color};
    }}
    QFrame {{ 
        color: {_text_color};
        font: {_text_font_size}px;
    }}
    """