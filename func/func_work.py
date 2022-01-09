import pickle
import pprint

from .func_userdata import Function_DataIO
from .func_ccxt import Function_ccxt
from module.pyside6_module_import import *
from func.func_ccxt import Function_ccxt
import time

class Function_Work:
    # DO NOT USED!
    def my_balance_trend_data():
        old_data = Function_DataIO.load_AppData_record()
        datum_time = Function_DataIO.load_history_timestamp_check()
        if not old_data:
            pass
        else:
            try:
                datum_time = old_data.index(-1)["timestamp"]
            except:
                pass
        binance = Function_ccxt.binance
        markets = Function_DataIO.load_local_markets()
        my_trades = []
        for market in markets:
            my_trades.append(binance.fetch_my_trades(symbol=market, since=datum_time, limit=None))
            if my_trades[-1] == []:
                my_trades.remove([])
            time.sleep(1)
        sorted_my_trades = my_trades.sort(key=lambda x: x["timestamp"])
        Function_DataIO.save_history_timestamp_check(binance.milliseconds())
        return sorted_my_trades
        

        