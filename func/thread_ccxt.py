from module.pyside6_module_import import *
from func.func_ccxt import Function_ccxt
from func.func_userdata import Function_Login
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
        try:
            old_data = Function_Login.load_AppData_record()
        except:
            old_data = pd.DataFrame()
        print(old_data)
        datum_time = None
        if old_data.empty:
            pass
        else:
            old_timestamp = old_data.iloc[old_data.shape[0]-1]["timestamp"]
            if binance.milliseconds()-old_timestamp <= 70000000:
                self.runtime +=1
                return old_data
            pass
            datum_time = old_timestamp

        markets = Function_Login.load_local_markets()
        df_my_trades = pd.DataFrame()
        markets = ["BNB/ETH", "SOL/BUSD", "SOL/USDT", "BNB/BUSD", "BNB/USDT", "BTT/USDT", "BTT/BUSD" ]
        for market in markets:
            if self.runtime >= 1:
                break
            while self.pause:
                time.sleep(1)
            df = pd.DataFrame(binance.fetch_my_trades(symbol=market, since=datum_time, limit=None))
            df_my_trades = df.append(df_my_trades)
            print(df)
            print(df_my_trades.shape[0])
        df_sort_my_trades = df_my_trades.sort_values("timestamp")
        
        Function_Login.save_AppData_record(df_sort_my_trades)
        Function_Login.save_history_timestamp_check(binance.milliseconds())
        self.runtime +=1
        return df_sort_my_trades
        