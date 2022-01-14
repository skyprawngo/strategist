from module.pyside6_module_import import *
from func.thread_ccxt import Thread_getChart
import pandas as pd
from datetime import datetime


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
        self._series = QCandlestickSeries()
        self._series.setIncreasingColor(Qt.red)
        self._series.setDecreasingColor(Qt.blue)
        
        self._layout.removeWidget(self.vol_chartview)
        self.vol_series = QCandlestickSeries()
        self.vol_series.setIncreasingColor(Qt.red)
        self.vol_series.setDecreasingColor(Qt.blue)
        interest = 0
        for row_num in range(len(df)):
            
            candlestick = QCandlestickSet(df.iloc[row_num][1], df.iloc[row_num][2], df.iloc[row_num][3], df.iloc[row_num][4], float(df.iloc[row_num][0]))
            self._series.append(candlestick)
            
            if df.iloc[row_num][1] < df.iloc[row_num][4]:
                vol_candlestick = QCandlestickSet(0, df.iloc[row_num][5], 0, df.iloc[row_num][5], float(df.iloc[row_num][0]))
            else:
                vol_candlestick = QCandlestickSet(df.iloc[row_num][5], df.iloc[row_num][5], 0, 0, float(df.iloc[row_num][0]))
            self.vol_series.append(vol_candlestick)
            
            vbscheck = df.iloc[row_num][1] + (df.iloc[row_num-1][2]-df.iloc[row_num-1][3])*0.5
            if df.iloc[row_num][4] > vbscheck :
                interest += df.iloc[row_num][4]-vbscheck
        
        print(interest)
            
        self.chart = QChart()
        self.chart.setTitle("BTC/USDT")
        self.chart.legend().hide() 
        self.chart.addSeries(self._series)

        self.vol_chart = QChart()
        self.vol_chart.legend().hide() 
        self.vol_chart.addSeries(self.vol_series)
        
        # self.vol_chart.legend().hide() 
        axis_x = QDateTimeAxis()
        axis_x.setFormat("yy/MM/dd")
        axis_x.setLabelsVisible(True)
        axis_x.setTitleVisible(False)
        self.chart.addAxis(axis_x, Qt.AlignBottom)
        self._series.attachAxis(axis_x)
        
        axis_y = QValueAxis()
        self.chart.addAxis(axis_y, Qt.AlignLeft)
        self._series.attachAxis(axis_y)
        
        vol_axis_x = QDateTimeAxis()
        vol_axis_x.setFormat("yy/MM/dd")
        vol_axis_x.setLabelsVisible(False)
        vol_axis_x.setTitleVisible(False)
        self.vol_chart.addAxis(vol_axis_x, Qt.AlignBottom)
        self.vol_series.attachAxis(vol_axis_x)
        
        vol_axis_y = QValueAxis()
        self.vol_chart.addAxis(vol_axis_y, Qt.AlignLeft)
        self.vol_series.attachAxis(vol_axis_y)
        
        self.chartview = QChartView(self.chart)
        
        self._layout.addWidget(self.chartview)
        
        self.vol_chartview = QChartView(self.vol_chart)
        self.vol_chartview.setFixedHeight(130)
        self._layout.addWidget(self.vol_chartview)
    
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
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        
        self.chart = QChart()
        self.chart.legend().hide()
        self._series = QCandlestickSeries()
        self.chartview = QChartView(self.chart)
        self._layout.addWidget(self.chartview)
        
        self.vol_chart = QChart()
        self.vol_chart.legend().hide()
        self.vol_series = QCandlestickSeries()
        self.vol_chartview = QChartView(self.vol_chart)
        self._layout.addWidget(self.vol_chartview)
        pass