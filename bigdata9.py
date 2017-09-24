# coding=gbk
import time
import requests
from bs4 import BeautifulSoup
import threading
import io
import sys
import multiprocessing
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
#reload(sys)
#sys.setdefaultencoding('utf-8')

def format_str(s):
    return s.replace("\n","").replace(" ","").replace("\t","")

def get_urls_in_pages(from_page_num,to_page_num):
    urls=[]
    search_word='计算机'
     

    url_part_1='http://www.phei.com.cn/module/goods/searchkey.jsp?Page='
    url_part_2='&Page=2&searchKey='
    for i in range(from_page_num,to_page_num+1):
        urls.append(url_part_1+str(i)+url_part_2+search_word)
    all_href_list=[]
    for url in urls:
        print(url)
        resp=requests.get(url)
        bs=BeautifulSoup(resp.text,'lxml')
        a_list=bs.find_all('a')
        needed_list=[]
        for a in a_list:
            if 'href' in a.attrs:
                href_val=a['href']
                title=a.text
                if 'bookid' in href_val and 'shopcar0.jsp' not in href_val and title !="":
                    if[title,href_val] not in needed_list:
                        needed_list.append([format_str(title),format_str(href_val)])
        all_href_list+=needed_list
    all_href_file=open(str(from_page_num)+'_'+str(to_page_num)+'_'+'all_hrefs.txt','w')
    for href in all_href_list:
        all_href_file.write('\t'.join(href)+'\n')
    all_href_file.close()
    print(from_page_num,to_page_num,len(all_href_list))


def multiple_threads_test():
    t1=time.time()
    page_ranges_lst=[(1,10),
                     (11,20),
                     (21,30),
                     (31,40),
                     ]
    th_lst=[]
    for page_range in page_ranges_lst:
        th=threading.Thread(target=get_urls_in_pages,args=(page_range[0],page_range[1]))
        th_lst.append(th)
    for th in th_lst:
        th.start()
    for th in th_lst:
        th.join()
    t2=time.time()
    print("use time :",t2-t1)
    return t2-t1

def single_test():
    t1=time.time()
    get_urls_in_pages(1,40)
    t2=time.time()
    print('use time:',t2-t1)
    return t2-t1


def multiple_processes_test():
    t1=time.time()
    page_ranges_lst=[(1,10),
                     (11,20),
                     (21,30),
                     (31,40),
                     ]
    pool=multiprocessing.Pool(processes=4)
    for page_range in page_ranges_lst:
        pool.apply_async(get_urls_in_pages,(page_range[0],page_range[1]))
    pool.close()
    pool.join()
    t2=time.time()
    print('time use:',t2-t1)
    return t2-t1


if __name__=='__main__':
    #mt=multiple_threads_test()
    #st=single_test()
    mpt=multiple_processes_test()
    print('mpt',mpt)