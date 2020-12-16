import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
from collections import Counter
import numpy as np
#import stylecloud

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
'''with open('tmp.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(breakword))
stylecloud.gen_stylecloud(file_path='tmp.txt',
                          icon_name='fas fa-cookie',
                          background_color='white',
                          output_name='t.png',
                          font_path=r'C:\Windows\Fonts\mingliu.ttc',
                          custom_stopwords=sp)'''
for word in breakword:
    if word not in sp:
        dic.append(word)
dic=Counter(dic)
mask=np.array(Image.open('ramen.png'))
wordcloud=WordCloud(background_color='white',mask=mask,font_path=r'C:\Windows\Fonts\mingliu.ttc')
wordcloud.generate_from_frequencies(dic)
image_colors=ImageColorGenerator(mask)
wordcloud.recolor(color_func=image_colors)
wordcloud.to_file('t.png')
