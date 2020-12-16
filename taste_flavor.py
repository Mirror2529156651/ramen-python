# -*- coding: utf-8 -*-
d={'味噌':0,'麻辣':0,'豚骨':0,'雞白湯':0}
with open('tmp.txt','r',encoding='utf-8') as f:
    s=f.read().split('\n')
for i in s:
    if i in d:
        d[i]+=1
print(d)
