import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
from collections import Counter
import numpy as np
import jieba

sp=[]
jieba.set_dictionary('../data/dict.txt.big')
flavor=[]
with open('../data/flavor.txt','r',encoding='utf-8') as f:
    flavor=f.read().split('\n')
for i in flavor:
    jieba.add_word(i)
with open('../data/stopword.txt','r',encoding='utf-8') as f:
        sp=f.read().split('\n')


mask=np.array(Image.open('../assets/ramen.png'))

for c in range(49):
    print(c)
    s=''
    l=[]
    dic=[]
    with open('../reviews/'+str(c)+'.txt','r',encoding='utf-8') as f:
        l=f.readlines()
    for i in l:
        s+=i
    breakword=jieba.cut(s)
    for word in breakword:
        if word not in sp:
            dic.append(word)
    #with open('../breakwords/'+str(c)+'.txt','r',encoding='utf-8') as f:
    #    dic=f.read().split('\n')
    dic=Counter(dic)
    wordcloud=WordCloud(background_color='white',mask=mask,font_path=r'C:\Windows\Fonts\mingliu.ttc')
    wordcloud.generate_from_frequencies(dic)
    image_colors=ImageColorGenerator(mask)
    wordcloud.recolor(color_func=image_colors)
    wordcloud.to_file('../wordclouds/'+str(c)+'.png')
