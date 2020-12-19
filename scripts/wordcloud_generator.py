import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
from collections import Counter
import numpy as np

mask=np.array(Image.open('../assets/ramen.png'))

for c in range(49):
    print(c)
    dic=[]
    with open('../breakwords/'+str(c)+'.txt','r',encoding='utf-8') as f:
        dic=f.read().split('\n')
    dic=Counter(dic)
    wordcloud=WordCloud(background_color='white',mask=mask,font_path=r'C:\Windows\Fonts\mingliu.ttc')
    wordcloud.generate_from_frequencies(dic)
    #image_colors=ImageColorGenerator(mask)
    #wordcloud.recolor(color_func=image_colors)
    wordcloud.to_file('../wordclouds/'+str(c)+'.png')