import pickle
import time

from .func_userdata import Function_Login
from .func_ccxt import Function_ccxt

class Func_Work:
    def my_balance_trend_data():
        old_data = Function_Login.load_AppData_record()
        datum_time = None
        if not old_data:
            pass
        else:
            datum_time = old_data.pop()["timestamp"]
        
        binance = Function_ccxt.binance
        markets = Function_Login.load_local_markets()
        my_trades = {}
        for market in markets:
            my_trade = binance.fetch_my_trades(symbol=market, since=datum_time, limit=None)
            my_trades[f"{market['timestamp']}"] = my_trade
        my_trades = my_trades.sort(key=my_trades.keys())
        Function_Login.save_AppData_record(my_trades)

        