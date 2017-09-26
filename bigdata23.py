import socks
import socket
from stem.control import Controller
from stem import Signal
import requests
import time
from bs4 import BeautifulSoup

controller=Controller.from_port(port=9151)
controller.authenticate()
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,'127.0.0.1',9150)
socket.socket=socks.socksocket

counter=0
url_ip='http://jsonip.com'
while counter < 500000:
    try:
        r=requests.get(url_ip)
        soup=BeautifulSoup(r.text)
        ip_val=r.json()['ip']
        print(counter,'now ip:',ip_val)
        time1=time.time()
        controller.signal(Signal.NEWNYM)
        time.sleep(5)
        time2=time.time()
        print(counter,'change ip time :',time2-time1)
        counter+=1
    except Exception as e:
        print(e)