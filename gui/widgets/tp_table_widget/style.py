# STYLE
style = '''
/* QTableWidget */

QTableWidget {{	
	background-color: {_bg_two};
	padding: 5px;
	border-radius: {_border_radius}px;
	gridline-color: {_bg_two};
    color: {_bg_two};
}}
QTableWidget::item{{
	border-color: none;
	padding-left: 5px;
	padding-right: 5px;
    border-bottom: 1px solid {_color_one};
    color: #000;
}}
QTableWidget::item:selected{{
    color: #000;
	background-color: {_color_one};
	border-radius: {_border_radius}px;
 
}}
QHeaderView::section{{
	background-color: {_bg_two};
	max-width: 30px;
	border: 1px solid {_bg_two};
	border-style: none;
    border-bottom: 1px solid {_bg_two};
    border-right: 1px solid {_bg_two};
}}
QTableWidget::horizontalHeader {{	
	background-color: {_bg_two};
}}
QTableWidget QTableCornerButton::section {{
    border: none;
	background-color: {_bg_three};
	padding: 3px;
    border-top-left-radius: {_border_radius}px;
}}
QHeaderView::section:horizontal
{{
    border: none;
	background-color: {_bg_two};
	padding: 3px;
}}
QHeaderView::section:vertical
{{
    border: none;
	background-color: {_bg_three};
	padding-left: 5px;
    padding-right: 5px;
    border-bottom: 1px solid {_bg_three};
    margin-bottom: 1px;
}}
QHeaderView::section:vertical:selected
{{
    border: none;
	background-color: {_color_one};
	padding-left: 5px;
    padding-right: 5px;
    border-bottom: 1px solid {_bg_three};
    margin-bottom: 1px;
}}


/* /////////////////////////////////////////////////////////////////////////////////////////////////
ScrollBars */
QScrollBar:horizontal {{
    border: none;
    background: {_bg_three};
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: {_color_one};
    min-width: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background: {_bg_three};
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background: {_bg_three};
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
     background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
     background: none;
}}
QScrollBar:vertical {{
	border: none;
    background: {_bg_three};
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
}}
QScrollBar::handle:vertical {{	
	background: {_bg_three};
    min-height: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:vertical {{
     border: none;
    background: {_bg_three};
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	border: none;
    background: {_bg_three};
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     background: none;
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     background: none;
}}
'''