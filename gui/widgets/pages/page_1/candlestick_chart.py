from module.pyside6_module_import import *
from func.thread_ccxt import Thread_getChart
import pandas as pd


class Candlestick_Chart(QWidget):
    def __init__(
        self,
        parent,
        app_parent,
        ):
        super().__init__()
        self._parent = parent
        self._app_parent = app_parent
        
        self.setup_Ui()
        self.setup_thread()
        self.sig_n_slot()
        
    def set_chart(self, df):
        df = pd.DataFrame(df)
        self._layout.removeWidget(self.chartview)
        self.chart = QChart()
        self._series = QCandlestickSeries()
        self._series.setIncreasingColor(Qt.red)
        self._series.setDecreasingColor(Qt.blue)
        timestamp = []
        for row_num in range(len(df)):
            candlestick = QCandlestickSet(df.iloc[row_num][1], df.iloc[row_num][2], df.iloc[row_num][3], df.iloc[row_num][4])
            self._series.append(candlestick)
            timestamp.append(str(df.iloc[row_num][0]))
        
        print(type(str(list(df.iloc[:][0]))))
        self.chart.addSeries(self._series)  

        self.chart.createDefaultAxes()
        self.chart.axisX(self._series).setCategories(timestamp)
        self.chart.legend().hide() 
             
        self.chartview = QChartView(self.chart)
        self._layout.addWidget(self.chartview)
    
    def sig_received(self, tooltip_text):
        self.symbol = tooltip_text
        if not self.thread_getchart.isRunning():
            self.thread_getchart.start()
            
    def sig_n_slot(self):
        self.thread_getchart.getchart_donesig.connect(self.set_chart)
    
    def setup_thread(self):
        self.thread_getchart = Thread_getChart(
            parent = self,
            app_parent = self._app_parent
        )
        
    def setup_Ui(self):
        self._layout = QVBoxLayout(self) 

        self.chart = QChart()
        self._series = QCandlestickSeries()
        self._series.setIncreasingColor(Qt.red)
        self._series.setDecreasingColor(Qt.blue)
        candlestick = QCandlestickSet()
        self._series.append(candlestick)
        
        self.chart.addSeries(self._series)
        self.chart.createDefaultAxes()
        self.chart.legend().hide()
        self.chartview = QChartView(self.chart)
        self._layout.addWidget(self.chartview)
        pass