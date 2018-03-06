# coding=gbk

import urllib.request
from bs4 import BeautifulSoup
import csv
import time
import random
import re

# 处理页面标签类
from urllib.error import URLError
from Tools.scripts.treesync import raw_input

class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


# 百度贴吧爬虫类
class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ, floorTag):
        # base链接地址
        self.baseURL = baseUrl
        # 是否只看楼主
        self.seeLZ = '?see_lz=' + str(seeLZ)
        # HTML标签剔除工具类对象
        self.tool = Tool()
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层标号，初始为1
        self.floor = 1
        # 默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"百度贴吧"
        # 是否写入楼分隔符的标记
        self.floorTag = floorTag

    # 传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            # 构建URL
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            # 返回UTF-8格式编码内容
            return response.read().decode('utf-8')
        # 无法连接，报错
        except URLError as e:
            if hasattr(e, "reason"):
                print
                u"连接百度贴吧失败,错误原因", e.reason
                return None

    # 获取帖子标题
    def getTitle(self, page):
        # 得到标题的正则表达式
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            # 如果存在，则返回标题
            return result.group(1).strip()
        else:
            return None

    # 获取帖子一共有多少页
    def getPageNum(self, page):
        # 获取帖子页数的正则表达式
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # 获取每一层楼的内容,传入页面内容
    def getContent(self, page):
        # 匹配所有楼层的内容
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            # 将文本进行去除标签处理，同时在前后加入换行符
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self, title):
        # 如果标题不是为None，即成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "wb+")
        else:
            self.file = open(self.defaultTitle + ".txt", "wb+")

    def writeData(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == '1':
                # 楼之间的分隔符
                floorLine = "\n" + str(
                    self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(str.encode(floorLine,"utf-8"))
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print ("URL已失效，请重试")
            return
        try:
            print
            "该帖子共有" + str(pageNum) + "页"
            for i in range(1, int(pageNum) + 1):
                print
                "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        # 出现写入异常
        except IOError as e:
            print
            "写入异常，原因" + e.message
        finally:
            print
            "写入任务完成"


#计算运行时间
start_time = time.time()

#保存到csv中
csvFile = open(r"test.csv",'a+',newline='')
writer =  csv.writer(csvFile)
writer.writerow(('posting_num','posting_title','posting_coments_num','posting_user_link','posting_user_name'))

#每页加50,共6940页
base_url = 'http://tieba.baidu.com/f?kw=%E5%B9%BF%E4%B8%9C%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
posting_num = 1  #计数爬取到第几个帖子
for page in range(0,2172):  #一共2172页   
    time_delay = random.randint(1, 3)  # 设置随机延迟时间，防止频繁的爬取导致百度封锁ID    
    url = base_url + str(page * 50)    
    html = urllib.request.urlopen(url)    
    bsObj = BeautifulSoup(html,'lxml')    
    posting_list = bsObj.find_all('div',{'class':'t_con cleafix'})    #查找标题块内各个信息， 标题、回复数、发帖人       

    print('============================')        
    print('正在抓取贴吧第%d页' % page)    
    now_time = time.time()      
    has_spent_seconds = now_time - start_time    
    has_spent_time_int = int((now_time - start_time) / 60)    
    print('小爬虫已耗时%d分钟' % has_spent_time_int)    
    if page > 1:        
        will_need_time = ((6940 * has_spent_seconds) / page)/60        
        will_need_time = int(will_need_time)        
        print('小爬虫还要爬%d分钟'%will_need_time)    
    #页面查找posting_coments_num，
    for posting in posting_list:
        try:
            # posting_coments_num
            posting_coments_num = posting.contents[1].span.contents[0]

            #posting_user_name
            posting_user_name =  posting.contents[3].span.contents[1].a.contents[0]

            #posting_user_link
            posting_user_link = 'http://tieba.baidu.com' + posting.contents[3].span.contents[1].a.attrs['href']

            #posting_title
            posting_title = posting.contents[3].contents[1].contents[1].a.attrs['title']

            #帖子数加1
            posting_num = posting_num + 1

            #数据保存
            writer.writerow((posting_num, posting_title, posting_coments_num, posting_user_link, posting_user_name))

        except:
            continue

    #抓数据每翻一页休息时间
    time.sleep(time_delay)
    #抓取了十页就休息3秒
    if page in list(range(1,6940,10)):
        time.sleep(3)


# 遍历完网站关闭csvFile
csvFile.close()

end_time = time.time()
duration_time = int((end_time - start_time)/60)
print('程序运行了%d分钟'%duration_time)