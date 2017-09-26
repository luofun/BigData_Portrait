import socks
import socket
from stem.control import Controller
from stem import Signal
import requests
import time

counter=0
controller=Controller.from_port(port=9151)
controller.authenticate()
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',9150)
socket.socket=socks.socksocket
url_ip='http://jsonip.com/'
url_pub='http://www.phei.com.cn/'
while counter<5:
    try:
        r=requests.get(url_ip)
        ip_val=r.json()['ip']
        print(counter,'now ip:',ip_val)
        time1=time.time()
        r2=requests.get(url_pub)
        time2=time.time()
        print(counter,'catch time:',time2-time1)
        with open(ip_val+'_pub.html','w',encoding="utf8") as f:
            f.write(r2.text)
        time3=time.time()
        controller.signal(Signal.NEWNYM)
        time.sleep(controller.get_newnym_wait())
        time4=time.time()
        print(counter,'change ip time:',time4-time3)
        counter=counter+1
    except Exception  as e:
        print(e)