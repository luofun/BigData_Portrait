﻿import io
import sys
import urllib.request
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
res=urllib.request.urlopen('http://www.baidu.com')
htmlBytes=res.read()
print(htmlBytes.decode('utf-8'))
f = open("out.html","w",encoding='utf-8')  
f.write(htmlBytes.decode('utf-8'))