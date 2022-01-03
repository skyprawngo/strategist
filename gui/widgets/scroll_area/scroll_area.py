from module.pyside6_module_import import *

class Scroll_Area(QScrollArea):
    def __init__(
            self,
            bg_color = "#fff",
            
            bar_bg_color = "#eaebec",
            bar_bg_color_hover = "#e3dbd7",
            bar_bg_color_pressed = "#d0a99a",
            add_sub_color = "#d8d9da",
        ):
        super().__init__()
        self.bg_color = bg_color
        
        self.bar_bg_color = bar_bg_color
        self.bar_bg_color_hover = bar_bg_color_hover
        self.bar_bg_color_pressed = bar_bg_color_pressed
        self.add_sub_color = add_sub_color
        
        self._style = None
        _style = self.set_style()
        self.setStyleSheet(_style)
    
    def set_style(self):
        bar_handle_vertical = f'''
            background-color: {self.bar_bg_color};
            min-height: 30px;
            border-radius: 7px;
        '''
        Bar_handle_vertical_hover = f'''
            background-color: {self.bar_bg_color_hover};
        '''
        Bar_handle_vertical_pressed = f'''
            background-color: {self.bar_bg_color_pressed};
        '''
        
        bar_sub_line_vertical = f'''
            border: none;
            background:none;
            height: 0px;
            
        '''
        bar_sub_line_vertical_hover = f'''
            background-color: {self.bar_bg_color_hover};
        '''
        bar_sub_line_vertical_pressed = f'''
            background-color: {self.bar_bg_color_pressed};
        '''
        
        bar_add_line_vertical = f'''
            border: none;
            background:none;
            height: 0px;
        '''
        bar_add_line_vertical_hover = f'''
            background-color: {self.bar_bg_color_hover};
        '''
        bar_add_line_vertical_pressed = f'''
            background-color: {self.bar_bg_color_pressed};
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
        
        bar_handle_vertical = "{"+bar_handle_vertical+"}"
        Bar_handle_vertical_hover = "{"+Bar_handle_vertical_hover+"}"
        Bar_handle_vertical_pressed = "{"+Bar_handle_vertical_pressed+"}"
        
        bar_sub_line_vertical = "{"+bar_sub_line_vertical+"}"
        bar_sub_line_vertical_hover = "{"+bar_sub_line_vertical_hover+"}"
        bar_sub_line_vertical_pressed = "{"+bar_sub_line_vertical_pressed+"}"
        
        bar_add_line_vertical = "{"+bar_add_line_vertical+"}"
        bar_add_line_vertical_hover = "{"+bar_add_line_vertical_hover+"}"
        bar_add_line_vertical_pressed = "{"+bar_add_line_vertical_pressed+"}"
        
        
        _style = f'''
        /* VERTICAL SCROLLBAR */

            /* HANDLE BAR VERTICAL */
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