from module.pyside6_module_import import *
from func.func_ccxt import Function_ccxt
import time

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