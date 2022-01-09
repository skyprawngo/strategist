from module.ccxt_module_import import *
import pandas as pd
import time

class Function_ccxt:
    binance = ccxt.binance()
    apikey = None
    secretkey = None
    df_balance = pd.DataFrame()
    
    def set_account(apikey, secretkey):
        Function_ccxt.apikey = apikey
        Function_ccxt.secretkey = secretkey
        Function_ccxt.binance = ccxt.binance(config={
            'apiKey': apikey,
            'secret': secretkey
        })
    
    def get_balance():
        balance = Function_ccxt.binance.fetch_balance()
        balance_total = balance["total"]
        del_parameters = ["info", "free", "used", "total"]
        for del_parameter in del_parameters:
            del balance[del_parameter]
            
        for coin in balance_total.keys():
            if balance_total[coin] == 0:
                del balance[coin]
                
        Function_ccxt.df_balance = pd.DataFrame(balance)
        
        return Function_ccxt.df_balance
    
    def get_price_USD(coin_name):
        coin_name = coin_name + "/USDT"
        price = Function_ccxt.binance.fetch_ticker(coin_name)
        price = price["close"]
        return price
    