# -*- coding: utf-8 -*-
import csv
l=['豚骨','麻辣','味噌','鹽味','醬油','雞白湯','沾麵','柑橘','蛤蠣','濃湯','叉燒','柚子','泡系']
d={}
for c in range(49):
    for i in l:
        d[i]=0
    with open('../breakwords/'+str(c)+'.txt','r',encoding='utf-8') as f:
        s=f.read().split('\n')
    for i in s:
        if i in d:
            d[i]+=1
    with open('../data/ramen_result.csv')
    #print(d)
