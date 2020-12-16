# -*- coding: utf-8 -*-
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

day=['一','二','三','四','五','六','日']

ua=UserAgent()
url='https://www.google.com/maps/place/%E9%9B%9E%E5%90%89%E5%90%9B%E6%8B%89%E9%BA%B5/@25.0861865,121.5648063,17z/data=!4m5!3m4!1s0x0:0x2287b1e0c714de1b!8m2!3d25.0861865!4d121.5670003'
text=requests.get(url,headers={'user-agent':ua.random}).text
score=text.split('評論')[1].split(',')[6]
print(score)
for i in day:
    day_pos=text.find(r'\"星期'+i+r'\"')
    f_pos=text.find('[',day_pos)
    s_pos=text.find(']',day_pos)
    print(text[f_pos:s_pos])
