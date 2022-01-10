from genericpath import isdir
import os
import csv
import pandas as pd
import pickle
import getpass
import platform
import ccxt

class Function_DataIO:
    if platform.system() == "Windows":
        username = getpass.getuser()
        appdata_dir_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist"))
    elif platform.system() == "Darwin":
        username = getpass.getuser()
        appdata_dir_path = os.path.abspath("/library/Caches/Stretegist")  
        
    appdata_path = os.path.abspath(os.path.join(appdata_dir_path,"user_data.txt"))
    appdata_history_path = os.path.normpath(os.path.join(appdata_dir_path, "history.csv"))
    parameter_dir_path = os.path.abspath(os.path.join(os.getcwd(), "data/parameter"))
    parameter_path = os.path.normpath(os.path.join(parameter_dir_path, "parameters.txt"))
    local_dir_path = os.path.abspath(os.path.join(os.getcwd(), "data/local"))
    local_markets_path = os.path.normpath(os.path.join(local_dir_path, "markets.csv"))
    
    def __init__(self):
        
        self.isfile_check()
        self.renewal_markets()
    
    def isfile_check(self):
        if not os.path.isdir(Function_DataIO.appdata_dir_path):
            os.makedirs(Function_DataIO.appdata_dir_path)
        if not os.path.isfile(Function_DataIO.appdata_path):
            with open(Function_DataIO.appdata_path, "wb") as datawriter:
                data = {
                    "apikey": None,
                    "secret": None
                }
                pickle.dump(data, datawriter)
        if not os.path.isfile(Function_DataIO.appdata_history_path):
            with open(Function_DataIO.appdata_history_path, "w") as datawriter:
                pass
        if not os.path.isdir(Function_DataIO.parameter_dir_path):
            os.makedirs(Function_DataIO.parameter_dir_path)
        if not os.path.isfile(Function_DataIO.parameter_path):
            with open(Function_DataIO.parameter_path, "wb") as datawriter:
                data = {
                    "key_save_ckbox": False,
                    "history_timestamp": None,
                    "market_timestamp": None,
                }
                pickle.dump(data, datawriter)
        if not os.path.isdir(Function_DataIO.local_dir_path):
            os.makedirs(Function_DataIO.local_dir_path)
        if not os.path.isfile(Function_DataIO.local_markets_path):
            with open(Function_DataIO.local_markets_path, "w") as datawriter:
                pass
        
    def renewal_markets(self):
        binance = ccxt.binance()
        
        markets = binance.load_markets()
        markets = pd.DataFrame(markets)
        try:
            local_markets = Function_DataIO.load_local_markets()
        except:
            local_markets = pd.DataFrame()
        
        if len(markets) != len(local_markets):
            
            Function_DataIO.save_local_markets(markets)
    
    def save_AppData_decorator(func):
        def save_AppData(*args, **kwargs):
            with open(Function_DataIO.appdata_path, 'rb') as datareader:
                data = pickle.load(datareader)
            with open(Function_DataIO.appdata_path, "wb") as datawriter:
                func(data=data, *args, **kwargs)
                pickle.dump(data, datawriter)
        return save_AppData
    
    def load_AppData_decorator(func):
        def load_AppData(*args, **kwargs):
            with open(Function_DataIO.appdata_path, 'rb') as datareader:
                data = pickle.load(datareader)
                data = func(data=data, *args, **kwargs)
            return data
        return load_AppData
    
    def save_local_decorator(func):
        def save_userdata(*args, **kwargs):
            with open(Function_DataIO.parameter_path, 'rb') as datareader:
                data = pickle.load(datareader)
            with open(Function_DataIO.parameter_path, "wb") as datawriter:
                func(data=data, *args, **kwargs)
                pickle.dump(data, datawriter)
        return save_userdata
    
    def load_local_decorator(func):
        def load_userdata(*args, **kwargs):
            with open(Function_DataIO.parameter_path, 'rb') as datareader:
                data = pickle.load(datareader)
                data = func(data=data, *args, **kwargs)
            return data
        return load_userdata

    @save_AppData_decorator
    def save_AppData(key, value, data=None):
        data[key] = value
    
    @load_AppData_decorator
    def load_AppData(data=None):
        return data
    
    @save_local_decorator
    def save_local_parameter(key, value, data=None):
        data[key] = value
        
    @load_local_decorator
    def load_local_parameter(data=None):
        return data

    def save_AppData_wallethistory(history):
        history.to_csv(Function_DataIO.appdata_history_path, index=None)
        
    def load_AppData_wallethistory():
        try:
            record = pd.read_csv(Function_DataIO.appdata_history_path)
        except:
            record = pd.DataFrame()
        return record
    
    def save_local_markets(markets, data=None):
        markets.to_csv(Function_DataIO.local_markets_path, index=None)
    
    def load_local_markets():
        try:
            markets = pd.read_csv(Function_DataIO.local_markets_path)
        except:
            markets = pd.DataFrame()
        return markets
    
    


