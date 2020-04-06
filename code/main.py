import requests
import bs4

for page in range(1, 11):
    url = "http://tieba.baidu.com/f/search/res?ie=utf-8&qw=aj1&pn=" + str(page)

    res = requests.get(url = url)
    html = res.text

    soup = bs4.BeautifulSoup(html, "lxml")
    echo = soup.find_all(class_ = "p_title")
    soup2 = bs4.BeautifulSoup(str(echo), "lxml")
    echo2 = soup2.find_all(class_ = "bluelink")
    for i in echo2:
        print(i["href"])
        print(i.text)
        print()