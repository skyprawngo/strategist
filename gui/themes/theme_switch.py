# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import json
import os

# APP SETTINGS
# ///////////////////////////////////////////////////////////////
class Theme_Switch(object):
    # APP PATH
    # ///////////////////////////////////////////////////////////////
    cwd_path = os.path.abspath(os.getcwd())
    app_path = "gui/themes"
    json_switch_path = os.path.normpath(os.path.join(cwd_path, app_path, "switch.json"))

    # INIT SETTINGS
    # ///////////////////////////////////////////////////////////////
    def __init__(self):
        super(Theme_Switch, self).__init__()
        self.switch = {}
        self.deserialize_switch()

    # SERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def serialize_switch(self):
        # WRITE JSON FILE
        with open(self.json_switch_path, "w", encoding='utf-8') as write:
            json.dump(self.switch, write, indent=4)

    # DESERIALIZE JSON
    # ///////////////////////////////////////////////////////////////
    def deserialize_switch(self):
        # WRITE JSON FILE
        with open(self.json_switch_path, "r", encoding='utf-8') as reader:
            switch = json.loads(reader.read())
            self.switch = switch
    # ///////////////////////////////////////////////////////////////