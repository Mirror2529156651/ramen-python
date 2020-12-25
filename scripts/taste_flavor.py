# -*- coding: utf-8 -*-
import csv
l = ['豚骨', '麻辣', '味噌', '鹽味', '醬油', '雞白湯', '沾麵',
     '柑橘', '蛤蠣', '濃湯', '叉燒', '濃郁', '柚子', '泡系']
d = {}
with open('../data/ramen_result.csv', 'r', encoding='utf-8') as f:
    with open('../data/ramen_flavor.csv', 'w', newline='', encoding='utf-8')as wf:
        rows = csv.reader(f)
        writer = csv.writer(wf)
        c = 0
        for row in rows:
            print(c)

            # init
            all = 0
            for i in l:
                d[i] = 0

            with open('../breakwords/'+str(c)+'.txt', 'r', encoding='utf-8') as f:
                s = f.read().split('\n')

            # 計算口味的出現次數
            for i in s:
                if i in d:
                    d[i] += 1
                    all += 1
            c += 1
            res = []
            for i in row:
                res.append(i)
            for i in l:
                res.append(round(d[i]/all, 2))  # 計算口味的百分比到小數點後2位
            writer.writerow(res)
