import pandas as pd

class Function_exchangerate:
    url ='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%99%98%EC%9C%A8%EC%A1%B0%ED%9A%8C'
    tables = pd.read_html(url)[0]
    
    def USD_to_KRW():
        return Function_exchangerate.tables["매매기준율"][0]
    
    def JPY_to_KRW():
        return Function_exchangerate.tables["매매기준율"][1]
