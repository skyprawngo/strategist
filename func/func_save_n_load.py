import os
import pickle
import getpass

from module.CCXT_module_import import *


class Function_Login:
    username = getpass.getuser()
    file_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist/user_data.txt"))
    dir_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist"))
    if os.path.isdir(dir_path):
        os.makedirs(dir_path)
    
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as datareader:
            data = pickle.load(datareader)
            print(data)
    else:
        data = {
            "id": "",
        }
        
        with open(file_path, 'wb') as datawriter:
            pickle.dump(data, datawriter)
            
    def save_login_id(self, id=""):
        with open(self.file_path, 'wb') as datawriter:
            self.data["id"] = id
            pickle.dump(self.data, datawriter)
    
    def save_sign_in():
        pass
    

class Function_ccxt:
    pass