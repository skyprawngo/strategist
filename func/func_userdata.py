from genericpath import isdir
import os
import csv
import pandas as pd
import pickle
import getpass
import platform
from .func_ccxt import Function_ccxt

class Function_DataIO:
    if platform.system() == "Windows":
        username = getpass.getuser()
        appdata_dir_path = os.path.normpath(os.path.join("C:/Users",username,"AppData/Local/Stretegist"))
    elif platform.system() == "Darwin":
        username = getpass.getuser()
        appdata_dir_path = os.path.abspath("/library/Caches/Stretegist")  
    appdata_path = os.path.abspath(os.path.join(appdata_dir_path,"user_data.txt"))
    appdata_record_path = os.path.normpath(os.path.join(appdata_dir_path, "record.csv"))
    settings_data_dir_path = os.path.normpath(os.path.join(os.getcwd(), "data/settings_data"))
    settings_data_path = os.path.normpath(os.path.join(settings_data_dir_path, "settings.txt"))
    settings_data_dir_path = os.path.normpath(os.path.join(os.getcwd(), "data/local"))
    local_data_path = os.path.normpath(os.path.join(settings_data_dir_path, "recordmarket.txt"))
    
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
                    "secretkey": None
                }
                pickle.dump(data, datawriter)
                
        if not os.path.isfile(Function_DataIO.appdata_record_path):
            with open(Function_DataIO.appdata_record_path, "w") as datawriter:
                pass
        
        if not os.path.isdir(Function_DataIO.settings_data_dir_path):
            os.makedirs(Function_DataIO.settings_data_dir_path)
        if not os.path.isfile(Function_DataIO.settings_data_path):
            with open(Function_DataIO.settings_data_path, "wb") as datawriter:
                data = {
                    "apikey_save_ckbox": False,
                    "history_timestamp": None
                }
                pickle.dump(data, datawriter)
        if not os.path.isfile(Function_DataIO.local_data_path):
            with open(Function_DataIO.local_data_path, "wb") as datawriter:
                data = {
                    "markets" : ""
                }
                pickle.dump(data, datawriter)
        
    
    def renewal_markets(self):
        binance = Function_ccxt.binance
        
        markets = binance.load_markets()
        local_markets = Function_DataIO.load_local_markets()
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
            with open(Function_DataIO.settings_data_path, 'rb') as datareader:
                data = pickle.load(datareader)
            with open(Function_DataIO.settings_data_path, "wb") as datawriter:
                func(data=data, *args, **kwargs)
                pickle.dump(data, datawriter)
        return save_userdata
    
    def load_local_decorator(func):
        def load_userdata(*args, **kwargs):
            with open(Function_DataIO.settings_data_path, 'rb') as datareader:
                data = pickle.load(datareader)
                data = func(data=data, *args, **kwargs)
            return data
        return load_userdata
    
    def save_local_record_decorator(func):
        def save_recorddata(*args, **kwargs):
            with open(Function_DataIO.local_data_path, 'rb') as datareader:
                data = pickle.load(datareader)
            with open(Function_DataIO.local_data_path, "wb") as datawriter:
                func(data=data, *args, **kwargs)
                pickle.dump(data, datawriter)
        return save_recorddata
    
    def load_local_record_decorator(func):
        def load_recorddata(*args, **kwargs):
            with open(Function_DataIO.local_data_path, 'rb') as datareader:
                data = pickle.load(datareader)
                data = func(data=data, *args, **kwargs)
            return data
        return load_recorddata

    @save_AppData_decorator
    def save_key(apikey, secretkey, data=None):
        data["apikey"] = apikey
        data["secretkey"] = secretkey
    
    @load_AppData_decorator
    def load_key(data=None):
        key = [data["apikey"], data["secretkey"]]
        return key
    
    def save_AppData_record(record):
        record.to_csv(Function_DataIO.appdata_record_path)
        
    def load_AppData_record():
        try:
            record = pd.read_csv(Function_DataIO.appdata_record_path)
        except:
            record = pd.DataFrame()
        return record

    @save_local_decorator
    def save_ckbox_remember_key(ckbox, data=None):
        data["apikey_save_ckbox"] = ckbox
        
    @load_local_decorator
    def load_ckbox_remember_key(data=None):
        ckbox = data["apikey_save_ckbox"]
        return ckbox

    @save_local_decorator
    def save_history_timestamp_check(timestamp, data=None):
        data["history_timestamp"] = timestamp
        
    @load_local_decorator
    def load_history_timestamp_check(data=None):
        timestamp = data["history_timestamp"]
        return timestamp
    
    @save_local_record_decorator
    def save_local_markets(markets, data=None):
        data["markets"] = markets
    
    @load_local_record_decorator
    def load_local_markets(data=None):
        markets = data["markets"]
        return markets
    
    


