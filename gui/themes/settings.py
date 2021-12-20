# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os

from .theme_switch import ThemeSwitch

# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Settings(object):
    # APP PATH
    # ///////////////////////////////////////////////////////////////
    cwd_path = os.path.abspath(os.getcwd())
    app_path = "gui/themes"
    switch = ThemeSwitch().switch["switch_theme"]
    settings_json_file = "settings.json"
    
    
    settings_path = os.path.normpath(os.path.join(cwd_path,app_path,switch,settings_json_file))

    
    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(Settings, self).__init__()

        # DICTIONARY WITH SETTINGS
        # Just to have objects references
        self.settings = {}
        
        # DESERIALIZE
        self.deserialize_settings()
    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize_settings(self):
        # WRITE JSON FILE
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(self.settings, write, indent=4)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize_settings(self):
        # READ JSON FILE
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            self.settings = settings