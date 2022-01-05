from module.pyside6_module_import import *
from module.ccxt_module_import import *
import time

class Thread_getbalance(QThread):
    signal = Signal()
    binance = ccxt.binance()
    apikey = None
    secretkey = None
    wallet_balance = {}
    
    def __init__(
        self, 
        app_parent = None
    ):
        QThread.__init__(self, app_parent)
        self. exiting = None
        
    def set_account(self, apikey, secretkey):
        self.apikey = apikey
        self.secretkey = secretkey
        self.binance = ccxt.binance(config={
            'apiKey': apikey,
            'secret': secretkey
        })
    
    def run(self):
        try:
            balance = self.binance.fetch_balance()
            balance_total = balance["total"]
            for coin in balance_total:
                if balance_total[coin] == 0:
                    pass
                else :
                    self.wallet_balance.setdefault(coin, balance[coin])
        except:
            balance = None
            print("balance error!")
        
        time.sleep(3)
        print(self.wallet_balance)
        return balance