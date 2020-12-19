# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import csv

day=['一','二','三','四','五','六','日']

rep=['\\','"','[','n']

ua=UserAgent()
rows=[]
with open('ramen_bak_new.csv','r',encoding='utf-8') as f:
    with open('ramen_result1.csv','w',encoding='utf-8')as wf:
        rows=csv.reader(f)
        writer=csv.writer(wf)
        c=0
        for row in rows:
            #input()
            #url='https://g.page/ichiran-tw?share'
            url=row[3]
            c+=1
            print(c)
            #input()
            text=requests.get(url,headers={'user-agent':ua.random}).text
            #print(text)
            store_tmp=text.split('評論')[1].split('[')[3].split(']')[1].split(',')
            store=''
            for word in store_tmp:
                if word!='null' and word!='\\n':
                    store+=word+','
            store=store[:len(store)-2]
            for i in rep:
                store=store.replace(i,'')
            '''for i in range(len(store)):
                if '114台北市內湖區環山路一段33號' in store[i]:
                    print(i)'''
            score=text.split('評論')[1].split(',')[6]
            reviews=text.split('評論')[1].split(',')[7].split(']')[0]
            open_time=[]
            print(score,reviews,store)
            for i in day:
                day_pos=text.find(r'\"星期'+i+r'\"')
                f_pos=text.find('[',day_pos)
                s_pos=text.find(']',day_pos)
                open_day=text[f_pos:s_pos]
                for j in rep:
                    open_day=open_day.replace(j,'')
                #print(open_day)
                open_time.append(open_day)
                
                
            writer.writerow([row[0],
                                 row[1],
                                 row[2],
                                 row[3],
                                 score,
                                 reviews,
                                 store,
                                 open_time[0],
                                 open_time[1],
                                 open_time[2],
                                 open_time[3],
                                 open_time[4],
                                 open_time[5],
                                 open_time[6]])

