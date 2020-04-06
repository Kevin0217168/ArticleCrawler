#from lxml import etree
from urllib import parse
import requests
import bs4

class Requests:
    def __init__(self, ba, word):
        self.ba = ba
        self.word = word
        self.url = "http://tieba.baidu.com/f/search/res?ie=utf-8&kw=" + parse.quote(ba) + "&qw=" + parse.quote(word) + "&pn="
        self.last_page = 0
        self.first = True
    
    def request_Page(self, page):
        # 请求网页
        res = requests.get(url = self.url + page)
        # 网页文本
        html = res.text

        # bs4二次搜索找出文章标题及链接
        soup = bs4.BeautifulSoup(html, "lxml")
        # 如果是第一次，则查找最大页数
        if self.first:
            herf = soup.find(class_ = "last")["href"]
            self.tail_page = int(herf[herf.rfind("=")+1:])
            self.first = False
            
        echo = soup.find_all(class_ = "p_title")
        soup2 = bs4.BeautifulSoup(str(echo), "lxml")
        echo2 = soup2.find_all(class_ = "bluelink")
        
        content = {}
        title = []
        for i in echo2:
            content[i.text] = i["href"]
            title.append(i.text)
            
        self.last_page = page
        return title, content