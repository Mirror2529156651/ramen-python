import tkinter as tk  # 引入套件
from PIL import ImageTk, Image

# 全域變數
# 口味
flavor_list = ['豚骨', '麻辣', '味噌', '鹽味', '醬油', '雞白湯', '沾麵', '柑橘', '蛤蠣',
               '濃湯', '叉燒', '濃郁', '柚子', '泡系']
# 行政區
district_list = ['中正', '中山', '萬華', '信義', '松山', '大安', '內湖', '士林']
# 捷運站
mrt_list = ['南京復興', '忠孝復興', '大安', '科技大樓', '劍南路', '西湖', '港墘', '東湖',
            '公館', '台電大樓', '古亭', '小南門', '台北車站', '中山', '雙連', '劍潭', '士林',
            '西門', '忠孝敦化', '國父紀念館', '市政府', '象山', '信義安和', '台北小巨蛋', '中山國小']

class Ramen(tk.Frame):  # 繼承現存的window frame

    def __init__(self, master=None):  # define constructor
        tk.Frame.__init__(self)  # 做出視窗
        self.grid()  # 產生網格放widget用
        self.creat_widgets()  # 呼叫creatWidgets函數

    def creat_widgets(self):
        # label 參考資料
        # https://www.delftstack.com/zh-tw/tutorial/tkinter-tutorial/tkinter-label/
        # 標題
        self.titleLable = tk.Label(self, text='台北拉麵愛好會', font=('TkDefaultFont', 20))
        self.titleLable.grid(row=0, column=0, columnspan=6, sticky=tk.NE + tk.SW, pady=5)
        # 說明文字
        self.titleLable = tk.Label(self, text='想知道哪裡有好吃拉麵又不想花太多時間搜尋嗎？\
        \n動動手指選擇你想去的地方、你喜歡的口味，\n讓台北在地拉麵同好會幫你推薦道地的拉麵好味道！')
        self.titleLable.grid(row=1, column=0, columnspan=6)

        # checkbutton 參考資料
        # https://www.delftstack.com/zh-tw/tutorial/tkinter-tutorial/tkinter-checkbutton/
        # 口味 checkbutton
        self.flavorLable = tk.Label(self, text='喜好口味：', font=('TkDefaultFont', 16))
        self.flavorLable.grid(row=2, column=0, columnspan=6, sticky=tk.W, pady=2)
        self.creat_widgets_checkbutton(flavor_list, 'flavor', 3)  # 3 row
        # 行政區
        self.districtLable = tk.Label(self, text='行政區：', font=('TkDefaultFont', 16))
        self.districtLable.grid(row=6, column=0, columnspan=6, sticky=tk.W, pady=2)
        self.creat_widgets_checkbutton(district_list, 'district', 7)  # 3 row
        # 捷運站
        self.mrtLable = tk.Label(self, text='鄰近捷運站：', font=('TkDefaultFont', 16))
        self.mrtLable.grid(row=10, column=0, columnspan=6, sticky=tk.W, pady=2)
        self.creat_widgets_checkbutton(mrt_list, 'mrt', 11)  # 5 row

        # 查詢按鈕
        # self.submitButton = tk.Button(self, text='送出查詢', height=2)
        self.submitButton = tk.Button(self, command = lambda: self.return_result(), text='送出查詢', height=2)
        self.submitButton.grid(row=20, column=1, columnspan=4, sticky=tk.NE + tk.SW, pady=5)

    # 產生一堆 checkbutton
    def creat_widgets_checkbutton(self, list, variable_name, start_row):
        for i in range(len(list)):
            globals()[variable_name + str(i)] = list[i]  # 變數的名字
            # e.g. mtr0 = '南京復興', type(mtr0)=<class 'str'>
            temp = globals()[variable_name + str(i)]
            globals()[variable_name + str(i) + '_value'] = tk.BooleanVar()  # 變數按鈕的布林值
            temp_value = globals()[variable_name + str(i) + '_value']
            self.temp = tk.Checkbutton(self, text=list[i], variable=temp_value)
            # 5 column / 1 row, 這邊要拆成幾個成一列可以再調整
            i += 1
            j = i // 5  # 商數
            k = i % 5  # 餘數
            if k == 0:
                j -= 1
                k = 5
            else:
                k -= 1
            self.temp.grid(row=j + start_row, column=k, sticky=tk.W)

    # submitButton按下去跑出查詢結果
    def return_result(self):
        # 篩給演算法的資料
        check_flavor = self.true_checkbutton(flavor_list, 'flavor')
        check_district = self.true_checkbutton(district_list, 'district')
        check_mrt = self.true_checkbutton(mrt_list, 'mrt')
        # final_choose = self.algorithm()
        final_choose = self.algorithm(check_flavor, check_district, check_mrt)
        # 顯示結果
        self.ramen_result(final_choose)

    # checkbutton 是否已勾選
    def true_checkbutton(self, list, variable_name):
        temp_list = []
        for i in range(len(list)):
            if globals()[variable_name + str(i) + '_value'].get() is True:
                temp = list[i]
                temp_list.append(temp)
        return(temp_list)

    # 演算法by翁佳安
    def algorithm(self, check_flavor, check_district, check_mrt):
        choose_list = []
        import copy
        if len(check_district) == 0:
            check_district = copy.deepcopy(district_list)
        if len(check_mrt) == 0:
            check_mrt = copy.deepcopy(mrt_list)
        if len(check_flavor) == 0:
            check_flavor = copy.deepcopy(flavor_list)
        with open('../data/ramen_data.csv','r',encoding='utf-8') as f:
            # 從店家裡挑掉不符合勾選行政區、捷運站的店家
            store_num = -1
            for i in f:
                store_num += 1  # 給店家一個編號
                line = i.split(',')
                if line[1] not in check_district:
                    continue
                if line[2] not in check_mrt:
                    continue
                choose_store = [store_num,line[0]]
                choose_list.append(choose_store)
        with open('../data/ramen_data.csv','r',encoding='utf-8') as f:
            for k in f:
                line = k.split(',')
                for i in range(len(choose_list)):
                    if choose_list[i][1] == line[0]:
                        choose_list[i].append(float(line[4]))
                        choose_list[i].append(float(line[5]))
        import csv
        with open('../data/ramen_data.csv','r',encoding='utf-8') as f:
            line = f.readlines()
            for i in range(len(choose_list)):
                num = choose_list[i][0]
                choose_line = [ '{}'.format(x) for x in list(csv.reader([line[num]], delimiter=',', quotechar='"'))[0]]
                flavor_point = 0
                for flavor in check_flavor:
                    for s in range(14):
                        if flavor == flavor_list[s]:
                            flavor_point += float(choose_line[14+s])
                choose_list[i].append(flavor_point)
                # 詳細資訊要的東西
                choose_list[i].append(choose_line[2])  # 捷運站
                choose_list[i].append(choose_line[6])  # 地址
                choose_list[i].append(choose_line[7])  # 星期1
                choose_list[i].append(choose_line[8])  # 星期2
                choose_list[i].append(choose_line[9])  # 星期3
                choose_list[i].append(choose_line[10])  # 星期4
                choose_list[i].append(choose_line[11])  # 星期5
                choose_list[i].append(choose_line[12])  # 星期6
                choose_list[i].append(choose_line[13])  # 星期7
                choose_list[i].append(choose_line[3])  # 地圖連結
        # choose_list裡每一個list中依照順序是店家編號、店名、評分、評論數、口味權重
        choose_list.sort(key=lambda x:(x[4],x[2],x[3]),reverse=True)
        global final_choose
        final_choose = []
        for i in range(len(choose_list)):
            if i == 3:
                break
            else:
                final_choose.append(choose_list[i])
        return(final_choose)

    # 演算法算出來 全部的拉麵
    def ramen_result(self, final_choose):
        # 得到ㄉ演算法結果（二維list，已按照排序
        # [[0編號, 1店名, 2評分, 3評分數, 4口味權重]]
        # 知道編號跟店名就好其他不重要
        # 如果return空list的話？？？
        self.firstWindow = tk.Toplevel(self)
        # 查詢結果label
        self.resultLabel = tk.Label(self.firstWindow, text='演算法結果', font=('TkDefaultFont', 16))
        self.resultLabel.grid(row=0, column=0, columnspan=6, sticky=tk.W, pady=2)
        if len(final_choose) == 0:
            self.noneLabel = tk.Label(self.firstWindow, text='沒有條件符合的店家，請再試一次。')
            self.noneLabel.grid(row=23, column=0, columnspan=6, sticky=tk.W, pady=2)
        else:
            times = 0
            for each_list in final_choose:
                self.ramen_log(each_list[0], each_list[1], times)
                times += 1

    # 各個拉麵印資料
    def ramen_log(self, number, name, more):
        # 店名
        self.resultLabel = tk.Label(self.firstWindow, text=name)
        self.resultLabel.grid(row=2, column=0+more, columnspan=1, sticky=tk.W, pady=2)
        # 圖片
        img_path = '../assets/' + str(number) + '.png'
        img_temp = Image.open(img_path)
        resized_image = img_temp.resize((200,200))  # 改圖片尺寸
        self.image = ImageTk.PhotoImage(resized_image)
        self.imglabel = tk.Label(self.firstWindow, image=self.image)
        self.imglabel.grid(row=3, column=0+more, columnspan=1, sticky=tk.W, pady=2)
        # 按鈕
        self.moreInfo = tk.Button(self.firstWindow, command = lambda: self.ramen_info(number), text='點我看更多', height=2)
        self.moreInfo.grid(row=4, column=0+more, columnspan=1, sticky=tk.W, pady=2)

    # 新視窗拉麵資訊
    def ramen_info(self, number):
        for each_list in final_choose:
            if each_list[0] == number:
                data_line = each_list
                break
        self.newWindow = tk.Toplevel(self)
        # 店名
        self.ramenTitle = tk.Label(self.newWindow, text=data_line[1], font=('TkDefaultFont', 18))
        self.ramenTitle.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=5)
        # 資訊：捷運站
        self.ramenInfo1 = tk.Label(self.newWindow, text='捷運站：'+data_line[5]+'站')
        self.ramenInfo1.grid(row=1, column=0, columnspan=1, sticky=tk.W)
        # 資訊：地址
        self.ramenInfo2 = tk.Label(self.newWindow, text='地址：\n'+data_line[6], justify='left')
        self.ramenInfo2.grid(row=2, column=0, columnspan=1, sticky=tk.W)
        # 資訊：營業時間
        self.ramenInfo3 = tk.Label(self.newWindow, text='營業時間：\n星期一：'+data_line[7]
                                                        + '\n星期二：'+data_line[8]
                                                        + '\n星期三：'+data_line[9]
                                                        + '\n星期四：'+data_line[10]
                                                        + '\n星期五：'+data_line[11]
                                                        + '\n星期六：'+data_line[12]
                                                        + '\n星期日：'+data_line[13],
                                                        justify='left')
        self.ramenInfo3.grid(row=3, column=0, columnspan=1, sticky=tk.W)
        # 資訊：超連結
        self.ramenInfo4 = tk.Label(self.newWindow, text='超連結：'+data_line[6])
        self.ramenInfo4.grid(row=10, column=0, columnspan=1, sticky=tk.W)
        # 圖片放右邊
        cloud_path = '../wordclouds/' + str(number) + '.png'
        cloud_temp = Image.open(cloud_path) 
        resized_image = cloud_temp.resize((200,200))
        self.cloud = ImageTk.PhotoImage(resized_image)
        self.label = tk.Label(self.newWindow, image=self.cloud)
        self.label.grid(row=1, column=1, rowspan=5, sticky=tk.E)


root = tk.Tk()  # master
ramen = Ramen(master=root)
ramen.master.title("Ramen Python")  # window title
# start the program
ramen.mainloop()
