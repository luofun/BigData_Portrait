#coding=gbk
import requests
import chardet

htmlCharsetGuess = chardet.detect(pageCode)
htmlCharsetEncoding = htmlCharsetGuess["encoding"]
htmlCode_decode = pageCode.decode(htmlCharsetEncoding)
type = sys.getfilesystemencoding()
htmlCode_encode = htmlCode_decode.encode(type)
print( htmlCode_encode) 

import zlib
def Get(self, url, refer=None):
     try:
       req = urllib2.Request(url)
       req.add_header('Accept-encoding', 'gzip')#默认以gzip压缩的方式得到网页内容
       if not (refer is None):
         req.add_header('Referer', refer)
       response = urllib2.urlopen(req, timeout=120)
       html = response.read()
       gzipped = response.headers.get('Content-Encoding')#查看是否服务器是否支持gzip
       if gzipped:
           html = zlib.decompress(html, 16+zlib.MAX_WBITS)#解压缩，得到网页源码
       return html
     except urllib2.HTTPError as e:
       return e.read()
     except socket.timeout as e:
       return ''
     except socket.error as e:
       return ''