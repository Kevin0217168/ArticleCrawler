import sys
# 添加自制模块导入目录
sys.path.append("model")
# 系统模块导入目录
sys.path.append(r"C:\Users\18037802106\AppData\Local\Programs\Python\Python37")
sys.path.append(r"C:\Users\18037802106\AppData\Local\Programs\Python\Python37\Scripts")
sys.path.append(r"C:\Users\18037802106\AppData\Local\Programs\Python\Python37\Lib")
sys.path.append(r"C:\Users\18037802106\AppData\Local\Programs\Python\Python37\Lib\site-packages")

import title

import os

ba = input("请输入要搜索的吧名(不填则为全吧搜索)：")
word = input("请输入要搜索的关键词(必填)：")

# 实例化标题请求
Req = title.Requests(ba, word)
# 默认请求第一页
page = 1
com = ''
while True:
    # 请求页面
    res = Req.request_Page(str(page))
    # 打印候选列表
    for n in range(len(res[0])):
        print("（", n+1, "）", res[0][n], "\n")
        
    print("您所在的位置是第", page, "页，共", Req.tail_page, "页，请选择需要的指令：")
    print("向上翻页：j，向下翻页：k，跳转到页面：goto {page}，退出：q")
    print("输入文章序号来下载内容(可多个下载)：get {paperNum} [paper2Num] [paper3Num]...")
    
    while True:
        # 请求输入并去除左右空格
        ch = input(">>> ").strip()
        
        # 向上翻页
        if ch == "j":
            if page != 1:
                page -= 1
                break
            else:
                print("已经是第一页啦！")
            
        # 向下翻页
        elif ch == "k":
            if page != Req.tail_page: 
                page += 1
                break
            else:
                print("已经是最后一页啦！")
        
        # 跳转到页面
        elif "goto" in ch:
            p = int(ch[4:])
            if p > 0 and p <= Req.tail_page:
                page = p
                break
            else:
                print("不匹配!")
        
        # 下载页面
        elif "get" in ch:
            num_list = ch[4:-1].split(" ")
            print("注意！将要下载这些页面：", num_list)
            if input("按'y'确认：") != 'y':
                print("您取消了下载！")
                continue
            print("准备下载...")
            
        # 退出
        elif ch == "q":
            print("您退出了选择")
            com = "home"
            break
        
        else:
            print("看不懂哦，再检查一下吧!")
            print("您所在的位置是第", page, "页，请选择需要的指令：")
            print("向上翻页：j，向下翻页：k，跳转到页面：goto page，退出：q")
            print("输入文章序号来下载内容(可多个下载)：get {paperNum} [paper2Num] [paper3Num]...")
        
        print()
    
    if com == "home":
        break
