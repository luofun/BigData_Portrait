import requests
import json
from pymongo import MongoClient
#from pymongo import mongo_client

ip='127.0.0.1'
port=10001
db_name='gd_map'
collection_name='pos_info'
url_1='http://ditu.amap.com/service/poiInfo?id=B0FFD62VDM&query_type=IDQ'
url_2='http://ditu.amap.com/service/poiInfo?id=B01C30003A&query_type=IDQ'
urls=[url_1,url_2]
mongo_conn=MongoClient(ip,port)

db=mongo_conn[db_name]

collection=db[collection_name]

for url in urls:
    try:
        print(url)
        resp=requests.get(url)
        json_dict=json.loads(resp.text)
        collection.save(json_dict)
    except Exception as e:
        print(e)