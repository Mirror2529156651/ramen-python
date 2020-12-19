import requests
from fake_useragent import UserAgent
import csv
from urllib import request

ua=UserAgent()
rows=[]
with open('../data/ramen_new.csv','r',encoding='utf-8') as f:
    rows=csv.reader(f)
    c=41
    for row in rows:
        url=row[3]
        print(c)
        text=requests.get(url,headers={'user-agent':ua.random}).text
        pic_url=text.split('<')[14].split('"')[1]
        request.urlretrieve(pic_url,'../assets/'+str(c)+'.png')        
        c+=1
