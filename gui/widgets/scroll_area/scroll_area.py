from module.pyside6_module_import import *

class Scroll_Area(QScrollArea):
    def __init__(
            self,
            parent,
            bg_one = "#e0e3ea",
            bg_two = "#f5f6fa",
            bg_three = "#fff",
            
            color_one = "#b9cefe",
            color_two = "#8aadff",
            color_three = "#6c98fe"
        ):
        super().__init__()
        self.bg_one = bg_one
        self.bg_two = bg_two
        self.bg_three = bg_three
        
        self.color_one = color_one
        self.color_two = color_two
        self.color_three = color_three
        
        self._style = None
        _style = self.set_style()
        self.setStyleSheet(_style)
    
    def set_style(self):
        transparent_color = '''background: transparent;'''
        bar_handle_vertical = f'''
            background-color: {self.color_one};
            min-height: 30px;
            border-radius: 7px;
        '''
        Bar_handle_vertical_hover = f'''
            background-color: {self.color_two};
        '''
        Bar_handle_vertical_pressed = f'''
            background-color: {self.color_three};
        '''
        bar_sub_line_vertical = f'''
            border: none;
            background:none;
            height: 0px;
            
        '''
        bar_add_line_vertical = f'''
            border: none;
            background:none;
            height: 0px;
        '''
        arrow = '''
        /* RESET ARROW */
        QScrollBar::up-arrow:vertical, QScrollbar::down-arrow:vertical {
            border: none;
            background: none;
        }
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
            border: none;
            background: none;
        }
        '''
        transparent_color = "{"+transparent_color+"}"
        bar_handle_vertical = "{"+bar_handle_vertical+"}"
        Bar_handle_vertical_hover = "{"+Bar_handle_vertical_hover+"}"
        Bar_handle_vertical_pressed = "{"+Bar_handle_vertical_pressed+"}"
        
        bar_sub_line_vertical = "{"+bar_sub_line_vertical+"}"
        bar_add_line_vertical = "{"+bar_add_line_vertical+"}"

        _style = f'''
            QScrollArea {transparent_color}
            /* VERTICAL SCROLLBAR */

            /* HANDLE BAR VERTICAL */
            QScrollBar {transparent_color}
            QScrollBar::handle:vertical {bar_handle_vertical}
            QScrollBar::handle:vertical:hover {Bar_handle_vertical_hover}
            QScrollBar::handle:vertical:pressed {Bar_handle_vertical_pressed}

            /* BTN TOP - SCHROLLBAR */
            QScrollBar::sub-line:vertical {bar_sub_line_vertical}
            QScrollBar::sub-page:vertical {bar_sub_line_vertical}
            

            /* BTN BOTTOM - SCHROLLBAR */
            QScrollBar::add-line:vertical {bar_add_line_vertical}
            QScrollBar::add-page:vertical {bar_add_line_vertical}
            
            {arrow}
        '''
        return _style