import jieba
import matplotlib.pyplot as plt
#from wordcloud import WordCloud
from collections import Counter
import stylecloud

jieba.set_dictionary('dict.txt.big')
s=''
l=[]
sp=[]
dic=[]
with open('comment.txt','r',encoding='utf-8') as f:
    l=f.readlines()
with open('stopword.txt','r',encoding='utf-8') as f:
    sp=f.read().split('\n')
for i in l:
    s+=i
breakword=jieba.cut(s)
with open('tmp.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(breakword))
stylecloud.gen_stylecloud(file_path='tmp.txt',
                          icon_name='fas fa-cookie',
                          background_color='white',
                          output_name='t.png',
                          font_path=r'C:\Windows\Fonts\mingliu.ttc',
                          custom_stopwords=sp)
