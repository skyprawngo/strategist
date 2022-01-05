# tyle
style = '''
/*QScrollArea*/
QScrollArea {{
    background: transparent;
}}
QScrollBar {{
    background: transparent;
}}
/* Vertical Scrollbar */

/* Vertical Handle bar  */

QScrollBar::handle:vertical {{
    background-color: {_color_one};
    min-height: 30px;
    border-radius: {_bar_radius};
}}
QScrollBar::handle:vertical:hover {{
    background-color: {_color_two};
}}
QScrollBar::handle:vertical:pressed {{
    background-color: {_color_three};
}}

/* BTN TOP - SCHROLLBAR */
QScrollBar::sub-line:vertical {{
    border: none;
    background:none;
    height: 0px;
}}
QScrollBar::sub-page:vertical {{
    border: none;
    background: none;
}}
QScrollBar::up-arrow:vertical{{
    border: none;
    background: none;
}}

/* BTN BOTTOM - SCHROLLBAR */
QScrollBar::add-line:vertical {{
    border: none;
    background:none;
    height: 0px;
}}
QScrollBar::add-page:vertical {{
    border: none;
    background: none;
}}
QScrollbar::down-arrow:vertical {{
    border: none;
    background: none;
}}



/* Horizontal Scrollbar */

/* Horizontal Handle bar  */
QScrollBar::handle:Horizontal {{
    background-color: {_color_one};
    min-width: 30px;
    border-radius: {_bar_radius};
}}
QScrollBar::handle:Horizontal:hover {{
    background-color: {_color_two};
}}
QScrollBar::handle:Horizontal:pressed {{
    background-color: {_color_three};
}}

/* BTN LEFT - SCHROLLBAR */
QScrollBar::sub-line:Horizontal {{
    border: none;
    background:none;
    height: 0px;
}}
QScrollBar::sub-page:Horizontal {{
    border: none;
    background: none;
}}
QScrollBar::left-arrow:Horizontal{{
    border: none;
    background: none;
}}

/* BTN RIGHT - SCHROLLBAR */
QScrollBar::add-line:Horizontal {{
    border: none;
    background:none;
    height: 0px;
}}
QScrollBar::add-page:Horizontal {{
    border: none;
    background: none;
}}
QScrollbar::right-arrow:Horizontal {{
    border: none;
    background: none;
}}
'''