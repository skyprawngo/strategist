import os
import pickle
import getpass

from module.ccxt_module_import import *

class Function_ccxt:
    binance = ccxt.binance()
    apikey = None
    secretkey = None
    
    def set_account(self, apikey, secretkey):
        self.apikey = apikey
        self.secretkey = secretkey
        self.binance = ccxt.binance(config={
            'apiKey': self.apikey,
            'secret': self.secretkey
        })
    
    def get_balance(self):
        balance = self.binance.fetch_balance()
        return balance
    
class Function_Login:
    username = getpass.getuser()
    file_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist/user_data.txt"))
    dir_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist"))
    
    

