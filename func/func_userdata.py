from genericpath import isdir
import os
import pickle
import getpass

class Function_Login:
    username = getpass.getuser()
    user_data_dir_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist"))
    AppData_path = os.path.normpath(os.path.join(user_data_dir_path,"user_data.txt"))
    settings_data_dir_path = os.path.normpath(os.path.join(os.getcwd(), "data/settings_data"))
    settings_data_path = os.path.normpath(os.path.join(settings_data_dir_path, "settings.txt"))

    def __init__(self):
        if not os.path.isdir(self.user_data_dir_path):
            os.makedirs(self.user_data_dir_path)
        if not os.path.isfile(self.AppData_path):
            with open(self.AppData_path, "wb") as datawriter:
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
                    "apikey_save_ckbox": False,
                    "apikey_remember_warning_apear": True,
                }
                pickle.dump(data, datawriter)
    
    def save_AppData_decorator(func):
        def save_AppData(*args, **kwargs):
            with open(Function_Login.AppData_path, 'rb') as datareader:
                data = pickle.load(datareader)
            with open(Function_Login.AppData_path, "wb") as datawriter:
                func(data=data, *args, **kwargs)
                pickle.dump(data, datawriter)
        return save_AppData
    
    def load_AppData_decorator(func):
        def load_AppData(*args, **kwargs):
            with open(Function_Login.AppData_path, 'rb') as datareader:
                data = pickle.load(datareader)
                data = func(data=data, *args, **kwargs)
            return data
        return load_AppData
    
    def save_userdata_decorator(func):
        def save_userdata(*args, **kwargs):
            with open(Function_Login.settings_data_path, 'rb') as datareader:
                data = pickle.load(datareader)
            with open(Function_Login.settings_data_path, "wb") as datawriter:
                func(data=data, *args, **kwargs)
                pickle.dump(data, datawriter)
        return save_userdata
    
    def load_userdata_decorator(func):
        def load_userdata(*args, **kwargs):
            with open(Function_Login.settings_data_path, 'rb') as datareader:
                data = pickle.load(datareader)
                data = func(data=data, *args, **kwargs)
            return data
        return load_userdata

    @save_AppData_decorator
    def save_key(apikey, secretkey, data=None):
        data["apikey"] = apikey
        data["secretkey"] = secretkey
    
    @load_AppData_decorator
    def load_key(data=None):
        key = [data["apikey"], data["secretkey"]]
        return key

    @save_userdata_decorator
    def save_ckbox_remember_key(ckbox, data=None):
        data["apikey_save_ckbox"] = ckbox
        
    @load_userdata_decorator
    def load_ckbox_remember_key(data=None):
        ckbox = data["apikey_save_ckbox"]
        return ckbox

    @save_userdata_decorator
    def save_warning_label_appear(appear, data=None):
        data["apikey_remember_warning_apear"] = appear
    
    @load_userdata_decorator
    def load_warning_label_appear(data=None):
        ckbox = data["apikey_remember_warning_apear"]
        return ckbox