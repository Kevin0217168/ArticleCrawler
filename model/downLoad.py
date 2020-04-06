import requests
import bs4
import hashlib
import os

class Download:
    def __init__(self, outPath):
        self.outPath = outPath
        
    def dwonLoad(self, url):
        print("正在连接 ->", url)
        res = requests.get(url = url)
        soup = bs4.BeautifulSoup(res.text, "lxml")
        title = soup.find(class_ = "core_title_txt")
        print("[已连接]", title.text)
        
        echo = soup.find_all(class_ = "d_post_content")
        content = list(echo)
        for n in range(len(content)):
            print("正在下载文本[第", n+1, "条]...", end="")
            # 将url进行哈希运算，防止重名
            with open(self.outPath + "/" + str(hash(url)) + ".txt", "a", encoding="utf-8") as f:
                f.write(content[n].text + "\n--------------\n")
            print("下载完成")
            
            print("扫描图片中...", end="")
            soup2 = bs4.BeautifulSoup(str(echo[n]), "lxml")
            images = list(soup2.find_all("img"))
            print("[共有图片" + str(len(images)) + "张]")
            if len(images) != 0:
                dirstr = self.outPath + "\\Images -- " + str(hash(url))
                try:
                    os.mkdir(dirstr)
                except Exception:
                    print("文件夹重复--合并")
                print("创建文件存放目录：" + dirstr)
                for i in range(len(images)):
                    print("图片下载中[第", i+1, "张]...", end="")
                    res = requests.get(url = images[i]["src"])
                    # 处理拓展名
                    tuozhan = images[i]["src"][images[i]["src"].rfind("."):]
                    t = tuozhan.rfind("?")
                    if t != -1:
                        tuozhan = tuozhan[:t]
                        
                    with open(dirstr + "/" + str(hash(images[i]["src"])) + tuozhan, "wb") as f:
                        f.write(res.content)
                    print("[下载完成]")
            
        