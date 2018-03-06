# coding=gbk

import urllib.request
from bs4 import BeautifulSoup
import csv
import time
import random
import re

# ����ҳ���ǩ��
from urllib.error import URLError
from Tools.scripts.treesync import raw_input

class Tool:
    # ȥ��img��ǩ,7λ���ո�
    removeImg = re.compile('<img.*?>| {7}|')
    # ɾ�������ӱ�ǩ
    removeAddr = re.compile('<a.*?>|</a>')
    # �ѻ��еı�ǩ��Ϊ\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # ������Ʊ�<td>�滻Ϊ\t
    replaceTD = re.compile('<td>')
    # �Ѷ��俪ͷ��Ϊ\n�ӿ�����
    replacePara = re.compile('<p.*?>')
    # �����з���˫���з��滻Ϊ\n
    replaceBR = re.compile('<br><br>|<br>')
    # �������ǩ�޳�
    removeExtraTag = re.compile('<.*?>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()��ǰ���������ɾ��
        return x.strip()


# �ٶ�����������
class BDTB:
    # ��ʼ�����������ַ���Ƿ�ֻ��¥���Ĳ���
    def __init__(self, baseUrl, seeLZ, floorTag):
        # base���ӵ�ַ
        self.baseURL = baseUrl
        # �Ƿ�ֻ��¥��
        self.seeLZ = '?see_lz=' + str(seeLZ)
        # HTML��ǩ�޳����������
        self.tool = Tool()
        # ȫ��file�������ļ�д���������
        self.file = None
        # ¥���ţ���ʼΪ1
        self.floor = 1
        # Ĭ�ϵı��⣬���û�гɹ���ȡ������Ļ�������������
        self.defaultTitle = u"�ٶ�����"
        # �Ƿ�д��¥�ָ����ı��
        self.floorTag = floorTag

    # ����ҳ�룬��ȡ��ҳ���ӵĴ���
    def getPage(self, pageNum):
        try:
            # ����URL
            url = self.baseURL + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            # ����UTF-8��ʽ��������
            return response.read().decode('utf-8')
        # �޷����ӣ�����
        except URLError as e:
            if hasattr(e, "reason"):
                print
                u"���Ӱٶ�����ʧ��,����ԭ��", e.reason
                return None

    # ��ȡ���ӱ���
    def getTitle(self, page):
        # �õ������������ʽ
        pattern = re.compile('<h1 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            # ������ڣ��򷵻ر���
            return result.group(1).strip()
        else:
            return None

    # ��ȡ����һ���ж���ҳ
    def getPageNum(self, page):
        # ��ȡ����ҳ����������ʽ
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        if result:
            return result.group(1).strip()
        else:
            return None

    # ��ȡÿһ��¥������,����ҳ������
    def getContent(self, page):
        # ƥ������¥�������
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            # ���ı�����ȥ����ǩ����ͬʱ��ǰ����뻻�з�
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content.encode('utf-8'))
        return contents

    def setFileTitle(self, title):
        # ������ⲻ��ΪNone�����ɹ���ȡ������
        if title is not None:
            self.file = open(title + ".txt", "wb+")
        else:
            self.file = open(self.defaultTitle + ".txt", "wb+")

    def writeData(self, contents):
        # ���ļ�д��ÿһ¥����Ϣ
        for item in contents:
            if self.floorTag == '1':
                # ¥֮��ķָ���
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
            print ("URL��ʧЧ��������")
            return
        try:
            print
            "�����ӹ���" + str(pageNum) + "ҳ"
            for i in range(1, int(pageNum) + 1):
                print
                "����д���" + str(i) + "ҳ����"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
        # ����д���쳣
        except IOError as e:
            print
            "д���쳣��ԭ��" + e.message
        finally:
            print
            "д���������"


#��������ʱ��
start_time = time.time()

#���浽csv��
csvFile = open(r"test.csv",'a+',newline='')
writer =  csv.writer(csvFile)
writer.writerow(('posting_num','posting_title','posting_coments_num','posting_user_link','posting_user_name'))

#ÿҳ��50,��6940ҳ
base_url = 'http://tieba.baidu.com/f?kw=%E5%B9%BF%E4%B8%9C%E5%B7%A5%E4%B8%9A%E5%A4%A7%E5%AD%A6&ie=utf-8&pn='
posting_num = 1  #������ȡ���ڼ�������
for page in range(0,2172):  #һ��2172ҳ   
    time_delay = random.randint(1, 3)  # ��������ӳ�ʱ�䣬��ֹƵ������ȡ���°ٶȷ���ID    
    url = base_url + str(page * 50)    
    html = urllib.request.urlopen(url)    
    bsObj = BeautifulSoup(html,'lxml')    
    posting_list = bsObj.find_all('div',{'class':'t_con cleafix'})    #���ұ�����ڸ�����Ϣ�� ���⡢�ظ�����������       

    print('============================')        
    print('����ץȡ���ɵ�%dҳ' % page)    
    now_time = time.time()      
    has_spent_seconds = now_time - start_time    
    has_spent_time_int = int((now_time - start_time) / 60)    
    print('С�����Ѻ�ʱ%d����' % has_spent_time_int)    
    if page > 1:        
        will_need_time = ((6940 * has_spent_seconds) / page)/60        
        will_need_time = int(will_need_time)        
        print('С���滹Ҫ��%d����'%will_need_time)    
    #ҳ�����posting_coments_num��
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

            #��������1
            posting_num = posting_num + 1

            #���ݱ���
            writer.writerow((posting_num, posting_title, posting_coments_num, posting_user_link, posting_user_name))

        except:
            continue

    #ץ����ÿ��һҳ��Ϣʱ��
    time.sleep(time_delay)
    #ץȡ��ʮҳ����Ϣ3��
    if page in list(range(1,6940,10)):
        time.sleep(3)


# ��������վ�ر�csvFile
csvFile.close()

end_time = time.time()
duration_time = int((end_time - start_time)/60)
print('����������%d����'%duration_time)