import requests
import json
from fake_useragent import UserAgent
import time

ua = UserAgent()  # 僞造header

# google map reviews網址
with open('../data/reviews_ajax.txt', 'r', encoding='utf-8') as rf:
    rows = rf.read().split('\n')

for c in range(50):
    s = ''
    url_f, url_b = rows[c].split(',')
    for i in range(1, 100):
        print(c, i)
        text = requests.get(url_f+str(i)+url_b,
                            headers={'user-agent': ua.random}).text
        text = text.replace(')]}\'', '')
        soup = json.loads(text)
        l = soup[2]  # l是一個json取其index[3]會得到評論
        try:
            for i in l:
                s += str(i[3])+'\n'
        except:  # 評論數太少QQ
            pass
    with open('../reviews/'+str(c)+'.txt', 'w', encoding='utf-8') as f:
        f.write(s)
