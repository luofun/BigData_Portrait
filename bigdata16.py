
from celery import Celery
from threading import Thread
import time

redit_ips={
    0:'redis://xxx.xxx.xxx.167:6379/0',
    1:'redis://xxx.xxx.xxx.193:6379/0',
    2:'redis://xxx.xxx.xxx.139:6379/0',
    3:'redis://xxx.xxx.xxx.7:6379/0',
    }

def send_task_and_get_results(ind,from_page,to_page):
    print('redis:',redit_ips[ind])
    app=Celery('tasks',broker=redit_ips[ind])
    app.conf.CELERY_RESULT_BACKED=redit_ips[ind]
    result=app.send_task('task.get_urls_in_pages',args=(from_page,to_page))
    print(redit_ips[ind],result.get())

if __name__=='__main__':
    t1=time.time()
    page_ranges_lst=[(1,10),
                     (11,20),
                     (21,30),
                     (31,40),
                     ]
    th_lst=[]
    for ind,page_range in enumerate(page_ranges_lst):
        th=Thread(target=send_task_and_get_results,args=(ind,page_range[0],page_range[1]))
        th_lst.append(th)
    for th in th_lst:
        th.start()
    for th in th_lst:
        th.join()
    t2=time.time()
    print('use time:',t2-t1)