# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os

from .theme_switch import Theme_Switch

# APP Themes
# ///////////////////////////////////////////////////////////////
class Themes(object):
    # APP PATH
    # ///////////////////////////////////////////////////////////////
    cwd_path = os.path.abspath(os.getcwd())
    app_path = "gui/themes"
    switch = Theme_Switch().switch["switch_theme"]
    themes_json_file = "themes.json"
    
    
    themes_path = os.path.normpath(os.path.join(cwd_path,app_path,switch,themes_json_file))

    
    # INIT Themes
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(Themes, self).__init__()

        # DICTIONARY WITH Themes
        # Just to have objects references
        self.themes = {}
        
        # DESERIALIZE
        self.deserialize_themes()
        
    
    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize_themes(self):
        # WRITE JSON FILE
        with open(self.themes_path, "w", encoding='utf-8') as write:
            json.dump(self.themes, write, indent=4)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize_themes(self):
        # READ JSON FILE
        with open(self.themes_path, "r", encoding='utf-8') as reader:
            themes = json.loads(reader.read())
            self.themes = themes