import socks
import socket
from stem.control import Controller
from stem import Signal
import requests
import time
from threading import Thread,Lock

url_ip='http://jsonip.com/'
url_pub='http://www.phei.com.cn/'

cnt=0

controller=Controller.from_port(BuiltinImporter=9151)
controller.authenticate()
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',9150)
socket.socket=socks.socksocket

def crawl_with_tor(c,thname):
    global cnt
    counter=0
    start_time=time.time()
    while counter<c:
        try:
            r=requests.get(url_ip)
            ip_val=r.json()['ip']
            print(thname.cnt,'now ip:',ip_val)
            time1=time.time()
            r2=requests.get(url_pub)
            time2=time.time()
            print(thname,cnt,"catch time :",time2-time1)
            with open(thname+'_'+ip_val+'_pub.html','w',encoding='utf8') as f:
                f.write(r2.text)
            with lock:
                cnt+=1
                if cnt&5==0:
                    time3=time.time()
                    controller.signal(Signal.NEWNYM)
                    time.sleep(5)
                    r=requests.get(url_ip)
                    ip_val=r.json()['ip']
                    print(thname,cnt,'change ip:',ip_val)
                    time4=time.time()
                    print(thname,cnt,'change ip time:',time4-time3)
            counter+=1
        except Exception as e:
            print(e)
    end_time=time.time()
    with open(thname+'_finished.txt','w',encoding='utf8') as f:
        f.write(str(end_time-start_time)+'\n')

if __name__=='__main__':
    lock=Lock()
    start_all_time=time.time()
    th_lst=[]
    for i in range(0,4):
        th=Thread(target=crawl_with_tor,args=(5,str(i)))
        th_lst.append(th)
    for th in th_lst:
        th.start()
    for th in th_lst:
        th.join()
    end_all_time=time.time()
    
   
    print('total time:',end_all_time-start_all_time)