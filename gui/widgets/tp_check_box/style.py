# Style
style = '''
QCheckBox::indicator{{
    background-color: qlineargradient(...);
    border: 1px solid #a2a5a9;
    width: {_width};
    height: {_height};
    border-radius: {_border_radius};
    left: 1px;
}}
QCheckBox::indicator:hover {{
    background-color: {_color_one};
    border: 1px solid {_color_one};
    width: {_width};
    height: {_height};
    border-radius: {_border_radius};
}}
QCheckBox::indicator:checked {{
    background-color: {_color_three};
    border: 1px solid {_color_three};
    width: {_width};
    height: {_height};
    border-radius: {_border_radius};
}}

'''