from module.ccxt_module_import import *
import time

class Function_ccxt:
    binance = ccxt.binance()
    apikey = None
    secretkey = None
    wallet_balance = {}
    
    def set_account(apikey, secretkey):
        Function_ccxt.apikey = apikey
        Function_ccxt.secretkey = secretkey
        Function_ccxt.binance = ccxt.binance(config={
            'apiKey': apikey,
            'secret': secretkey
        })
    
    def get_balance():
        try:
            balance = Function_ccxt.binance.fetch_balance()
            balance_total = balance["total"]
            for coin in balance_total:
                if balance_total[coin] == 0:
                    pass
                else :
                    Function_ccxt.wallet_balance.setdefault(coin, balance[coin])
        except:
            Function_ccxt.wallet_balance = {}
        return Function_ccxt.wallet_balance
    
    def get_price_USD(coin_name):
        coin_name = coin_name + "/USDT"
        price = Function_ccxt.binance.fetch_ticker(coin_name)
        price = price["close"]
        return price