from module.pyside6_module_import import *
from func.func_ccxt import Function_ccxt
from func.func_userdata import Function_DataIO
import time
import pandas as pd

class Thread_getbalance(QThread):
    done_signal = Signal()
    
    def __init__(
        self, 
        parent,
        app_parent
    ):
        QThread.__init__(self, app_parent)
        self._parent = parent
        self._app_parent = app_parent
        self.exiting = False
    
    def run(self):
        self.exiting = True
        apikey = self._parent.lineedit_apikey.text()
        secretkey = self._parent.lineedit_secretkey.text()
        Function_ccxt.set_account(
            apikey = apikey,
            secretkey = secretkey
        )       
        Function_ccxt.get_balance()
        self.done_signal.emit()
        self.exiting = False

class Thread_get_history(QThread):
    done_signal = Signal()
    
    def __init__(
        self, 
        parent,
        app_parent
    ):
        QThread.__init__(self, app_parent)
        self._parent = parent
        self._app_parent = app_parent
        self.runtime = 0
        self.pause = True
        
    def run(self):
        binance = Function_ccxt.binance
        markets = Function_DataIO.load_local_markets()
        old_data = Function_DataIO.load_AppData_record()
        df_trades = pd.DataFrame()
        df_new = pd.DataFrame()
        datum_time = None

        if old_data.empty:
            pass
        else:
            datum_time = old_data.iloc[old_data.shape[0]-1]["timestamp"]
            if binance.milliseconds()-datum_time <= 70000000:
                self.runtime +=1
            pass

        markets = ["BNB/ETH", "SOL/BUSD", "SOL/USDT", "BNB/BUSD", "BNB/USDT", "BTT/USDT", "BTT/BUSD" ]
        for market in markets:
            if self.runtime >= 1:
                break
            df = pd.DataFrame(binance.fetch_my_trades(symbol=market, since=datum_time, limit=None))
            df_trades = df.append(df_trades)
        df_trades.drop(index=0)
        df_new = df_trades.append(old_data)
        df_new = df_new.sort_values("timestamp")
        print(df_new)
        df_new.reset_index(drop=True)
        print(df_new)
        
        Function_DataIO.save_AppData_record(df_new)
        Function_DataIO.save_history_timestamp_check(binance.milliseconds())
        self.runtime +=1
        return df_new
        