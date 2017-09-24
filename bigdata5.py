import requests

url_dict={
    
    '1':'http://www.phei.com.cn/module/goods/wssd_index.jsp',
    '2':'http://www.baidu.com'

    
    }

url_lst=[
    
    ('1','http://www.phei.com.cn/module/goods/wssd_index.jsp'),
    ('2','http://www.baidu.com')

    
    ]

print(type(url_dict))
print(type(url_lst))

cufd=set()
for ind,name in enumerate(url_dict.keys()):
    name_url=url_dict[name]
    if name_url in cufd:
        print(ind,name,"have load")
    else:
        try:
            resp=requests.get(name_url)
        except Exception as e:
            print(ind,name,':',str(e)[0:50])
            continue

        content=resp.text
        cufd.add(name_url)
        with open('bydict_'+name+'.html','w',encoding='utf8') as f:
            f.write(content)
            print('load competele:{}   {},length:{}'.format(ind,name,len(content)))
for u in cufd:
    print(u)

print('-'*60)

cufl=set()
for ind,tup in enumerate(url_lst):
    name=tup[0]
    name_url=tup[1]
    if name_url in cufl: 
        print(ind,name,'have load')
    else:
        try:
            resp=requests.get(name_url)
        except Exception as e:
            print(ind,name,':',str(e)[0:50])
            continue
        content=resp.text
        cufl.add(name_url)
        with open('bylist_'+name+'.html','w',encoding='utf8') as f:
            f.write(content)
            print("load competele:{}   {},length:{}".format(ind,name,len(content)))
for u in cufl:
    print(u)