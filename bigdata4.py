import requests

def get_content(url):
    resp=requests.get(url)
    return resp.text

if __name__=='__main__':
    url="http://www.phei.com.cn"

    content=get_content(url)
    print("first 50:",content[0:50])

    content_len=len(content)

    print("length:",content_len)

    if content_len>=40*1024:
        print("bigger than 40KB(Byte)")
    else:
        print("smaller than 40KB(Byte)")
    
    print("-"*20)
    f1=open('1.html','w',encoding='utf8')
    f1.write(content)
    f1.close()

    print("read file")
    f2=open('1.html','r',encoding='utf8')
    content_read=f2.read()
    print("read 50:",content_read[0:50])
    f2.close()

    print('-'*20)
    
    with open('2.html','w',encoding='utf8') as f3:
        f3.write(content)
        #without close file by using the 'with'
    print('read2 50:')
    with open('2.html','r',encoding='utf8') as f4:
        content_read_2=f4.read()
        print(content_read_2[0:50])