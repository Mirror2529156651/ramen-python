import jieba

sp = []  # stopword list
jieba.set_dictionary('../data/dict.txt.big')  # 讀中文字典
flavor = []  # 口味

# 讀取事先準備的口味分類
with open('../data/flavor.txt', 'r', encoding='utf-8') as f:
    flavor = f.read().split('\n')

# 把口味加入字典中
for i in flavor:
    jieba.add_word(i)

# 讀取文字雲中不要的文字
with open('../data/stopword.txt', 'r', encoding='utf-8') as f:
    sp = f.read().split('\n')

for c in range(49):  # 共49間店
    print(c)
    s = ''
    l = []
    dic = []

    # 讀入Google map留言並按照字典切開
    with open('../reviews/'+str(c)+'.txt', 'r', encoding='utf-8') as f:
        l = f.readlines()
    for i in l:
        s += i
    breakword = jieba.cut(s)

    # 把不要的文字去掉
    for word in breakword:
        if word not in sp:
            dic.append(word)

    # 把切割好的文字存起來
    with open('../breakwords/'+str(c)+'.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(dic))
