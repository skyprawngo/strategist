from genericpath import isdir
import os
import pickle
import getpass

class Function_Login:
    username = getpass.getuser()
    user_data_dir_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist"))
    user_data_path = os.path.normpath(os.path.join(user_data_dir_path,"user_data.txt"))
    settings_data_dir_path = os.path.normpath(os.path.join(os.getcwd(), "data/settings_data"))
    settings_data_path = os.path.normpath(os.path.join(settings_data_dir_path, "settings.txt"))

    def __init__(self):
        if not os.path.isdir(self.user_data_dir_path):
            os.makedirs(self.user_data_dir_path)
        if not os.path.isfile(self.user_data_path):
            with open(self.user_data_path, "wb") as datawriter:
                data = {
                    "id": None,
                    "apikey": None,
                    "secretkey": None
                }
                pickle.dump(data, datawriter)
        
        if not os.path.isdir(self.settings_data_dir_path):
            os.makedirs(self.settings_data_dir_path)
        if not os.path.isfile(self.settings_data_path):
            with open(self.settings_data_path, "wb") as datawriter:
                data = {
                    "apikey_save": False,
                    "apikey_remember_warning_apear": True,
                }
                pickle.dump(data, datawriter)
            
    def save_key(apikey=None, secretkey=None):
        with open(Function_Login.user_data_path, 'rb') as datareader:
            data = pickle.load(datareader)
        with open(Function_Login.user_data_path, "wb") as datawriter:
                data["apikey"] = apikey
                data["secretkey"] = secretkey
                pickle.dump(data, datawriter)
    
    def load_key():
        with open(Function_Login.user_data_path, 'rb') as datareader:
            data = pickle.load(datareader)
            key = [data["apikey"], data["secretkey"]]
        return key

