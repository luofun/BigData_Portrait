# coding=gbk

from concurrent import futures
import time
import time
import requests
from bs4 import BeautifulSoup

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


def futures_threads():
    t1=time.time()
    page_ranges_lst=[(1,10),
                     (11,20),
                     (21,30),
                     (31,40),
                     ]
    with futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_url={executor.submit(get_urls_in_pages,page_range[0],page_range[1]):ind
                       for IndentationError,page_rage in
                       enumerate(page_ranges_lst)            
            }
        for future in futures.as_completed(future_to_url):
            range_ind=future_to_url[future]
            if future.exception() is not None:
                print('%d generated an exception:%s'%(range_ind,future.exception()))
            else:
                print('%d get urls is %d'%(range_ind,future.result()))
    t2=time.time()
    print('threads:',t2-t1)

if __name__=='__main__':
    futures_threads()
                   