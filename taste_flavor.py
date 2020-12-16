# -*- coding: utf-8 -*-
l=['豚骨','麻辣','味噌','鹽味','醬油','雞白湯','沾麵','柑橘','蛤蠣','濃湯','叉燒','柚子','泡系']
d={}
for i in l:
    d[i]=0
with open('tmp.txt','r',encoding='utf-8') as f:
    s=f.read().split('\n')
for i in s:
    if i in d:
        d[i]+=1
print(d)
