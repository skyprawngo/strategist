from module.ccxt_module_import import *

class Function_ccxt:
    binance = ccxt.binance()
    apikey = None
    secretkey = None
    
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
        except:
            balance = None
            print("balance error!")
        return balance