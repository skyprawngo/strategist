import time
from ccxt.base.exchange import Exchange
import pandas as pd
from module.pyside6_module_import import *
from module.ccxt_module_import import *
from func.func_userdata import Function_DataIO
from func.func_exchangerate import Function_Exchangerate

binance = ccxt.binance()
df_balance = pd.DataFrame()

class Thread_setKey(QThread):
    setkey_donesig = Signal(str)
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
        global binance
        self.exiting = True
        
        apikey = self._parent.lineedit_apikey.text()
        secretkey = self._parent.lineedit_secretkey.text()
        binance = ccxt.binance(config={  
            'apiKey': apikey,
            'secret': secretkey
        })
        self.setkey_donesig.emit(self.__class__.__name__)
        self.exiting = False
        

class Thread_getBalance(QThread):
    getbalance_donesig = Signal()
    
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
        global binance
        global df_balance
        self.exiting = True
        
        balance = binance.fetch_balance()
        balance_total = balance["total"]
        del_parameters = ["info", "free", "used", "total"]
        
        for del_parameter in del_parameters:
            del balance[del_parameter]
            
        for coin in balance_total.keys():
            if balance_total[coin] == 0:
                del balance[coin]
        
        df_balance = pd.DataFrame(balance)
        df_balance = df_balance.transpose()
        df_balance = df_balance.drop(["free", "used"], axis=1)
        self.datetime = df_balance.loc["datetime"]["total"]
        df_balance = df_balance.drop("datetime")
        df_balance = df_balance.drop("timestamp")
        df_balance = df_balance.reset_index()
        df_balance = df_balance.rename(columns={"index":"Coin"})
        df_balance = df_balance.rename(columns={"total":"Amount"})
        
        coin_names = list(df_balance["Coin"])
        prices=[]
        for coin_name in  coin_names:
            symbol = coin_name+"/USDT"
            price = binance.fetch_ticker(symbol=symbol)
            prices.append(price["close"])
        df_balance["Price(USD)"] = prices
        df_balance["Value(USD)"] = df_balance["Price(USD)"] * df_balance["Amount"]
        exchange_rate = Function_Exchangerate.USD_to_KRW()
        df_balance["Value(KRW)"] = df_balance["Value(USD)"] * exchange_rate
        hheaders = ["Coin", "Price(USD)", "Amount", "Value(USD)", "Value(KRW)"]
        self.df_balance = df_balance.reindex(columns=hheaders)

        self.getbalance_donesig.emit()
        self.exiting = False

class Thread_getHistory(QThread):
    gethistory_donesig = Signal()
    
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
        global binance
        global df_balance
        
        df_old = Function_DataIO.load_AppData_record()
        df_bundle = pd.DataFrame()
        df_new = pd.DataFrame()
        

        if df_old.empty:
            datum_time = None
        else:
            datum_time = df_old.iloc[-1]["timestamp"]
            print(datum_time)
            if binance.milliseconds()-datum_time <= 70000000:
                self.runtime +=1
            pass

        markets = ["BNB/ETH", "SOL/BUSD", "SOL/USDT", "BNB/BUSD", "BNB/USDT", "BTT/USDT", "BTT/BUSD" ]
        for market in markets:
            if self.runtime >= 1:
                break
            df = pd.DataFrame(binance.fetch_my_trades(symbol=market, since=datum_time, limit=None))
            df_bundle = df.append(df_bundle)
        df_bundle = df_bundle.drop(index=0)
        df_new = df_bundle.append(df_old)
        df_new = df_new.sort_values("timestamp")
        df_new = df_new.reset_index(drop=True)
        
        Function_DataIO.save_AppData_record(df_new)
        Function_DataIO.save_history_timestamp_check(binance.milliseconds())
        self.gethistory_donesig.emit()
        self.runtime +=1
        