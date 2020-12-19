import requests
import json
from fake_useragent import UserAgent
import time

#url_f='https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758546651144975!2y6093113884180453713!2m2!1i'
#url_b='8!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1s7E7YX57MDLGQr7wP7LaakAQ!7e81'

#url_f='https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758655143312777!2y14633634835676584921!2m2!1i'
#url_b='8!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1seV7YX8eZN4GwmAW47ZrgCQ!7e81'

#url_f='https://www.google.com.tw/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765758656371287665!2y738323575040338938!2m2!1i'
#url_b='8!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1sYn_YX6_TItKKr7wPsrOiyAE!7e81'

#url_f='https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765759062840895003!2y321026760390248241!2m2!1i'
#url_b='8!2i10!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1s_6PYX9j_N6LVmAXy1LLgBA!7e81'
ua=UserAgent()
with open('../data/reviews_ajax.txt','r',encoding='utf-8') as rf:
    rows=rf.read().split('\n')
for c in range(50):
    
    s=''
    url_f,url_b=rows[c].split(',')
    for i in range(1,100):
        print(c,i)
        text=requests.get(url_f+str(i)+url_b,headers={'user-agent':ua.random}).text
        text=text.replace(')]}\'','')
        soup=json.loads(text)
        l=soup[2]
        try:
            for i in l:
                s+=str(i[3])+'\n'
        except:
            pass
            #print(s)
        #time.sleep(5)
    with open('../reviews/'+str(c)+'.txt','w',encoding='utf-8') as f:
        f.write(s)

