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
    with open('../breakwords/'+str(c)+'.txt','w',encoding='utf-8') as f:
        f.write('\n'.join(dic))

