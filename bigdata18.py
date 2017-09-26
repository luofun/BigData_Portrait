import requests
url='https://t1.onvshen.com:85/gallery/22162/23839/026.jpg'
r=requests.get(url)
with open('test.jpg','wb') as f:
    f.write(r.content)
