import tkinter as tk  # 引入套件
from PIL import ImageTk, Image


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
        flavor_list = ['豚骨', '麻辣', '味噌', '鹽味', '醬油', '雞白湯', '沾麵', '柑橘', '蛤蠣',
                       '濃湯', '叉燒', '濃郁', '柚子', '泡系']
        self.flavorLable = tk.Label(self, text='喜好口味：', font=('TkDefaultFont', 16))
        self.flavorLable.grid(row=2, column=0, columnspan=6, sticky=tk.W, pady=2)
        self.creat_widgets_checkbutton(flavor_list, 'flavor', 3)  # 3 row
        # 行政區
        district_list = ['中正區', '中山區', '萬華區', '信義區', '松山區', '大安區', '內湖區', '士林區']
        self.districtLable = tk.Label(self, text='行政區：', font=('TkDefaultFont', 16))
        self.districtLable.grid(row=6, column=0, columnspan=6, sticky=tk.W, pady=2)
        self.creat_widgets_checkbutton(district_list, 'district', 7)  # 3 row
        # 捷運站
        mrt_list = ['南京復興', '忠孝復興', '大安', '科技大樓', '劍南路', '西湖', '港墘', '東湖',
                    '公館', '台電大樓', '古亭', '小南門', '台北車站', '中山', '雙連', '劍潭', '士林',
                    '西門', '忠孝敦化', '國父紀念館', '市政府', '象山', '信義安和', '台北小巨蛋', '中山國小']
        self.mrtLable = tk.Label(self, text='鄰近捷運站：', font=('TkDefaultFont', 16))
        self.mrtLable.grid(row=10, column=0, columnspan=6, sticky=tk.W, pady=2)
        self.creat_widgets_checkbutton(mrt_list, 'mrt', 11)  # 5 row

        # 查詢按鈕
        # self.submitButton = tk.Button(self, text='送出查詢', height=2)
        self.submitButton = tk.Button(self,command=self.return_result, text='送出查詢', height=2)
        self.submitButton.grid(row=20, column=1, columnspan=4, sticky=tk.NE + tk.SW, pady=5)

    # 產生一堆 checkbutton
    def creat_widgets_checkbutton(self, list, variable_name, start_row):
        for i in range(len(list)):
            globals()[variable_name + str(i)] = list[i]
            temp = globals()[variable_name + str(i)]
            self.temp = tk.Checkbutton(self, text=list[i])
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

    # 查詢結果
    def return_result(self):
        self.resultLabel = tk.Label(self, text='演算法結果(click for more information)', font=('TkDefaultFont', 16))
        self.resultLabel.grid(row=22, column=0, columnspan=6, sticky=tk.W, pady=2)
        self.ramen_result()

    # 演算法算出來的拉麵
    def ramen_result(self):
        self.resultLabel = tk.Label(self, text='店名')
        self.resultLabel.grid(row=23, column=0, columnspan=6, sticky=tk.W, pady=2)
        self.image = tk.PhotoImage(file='ramen.png')
        self.resizedImage = self.image.subsample(3)  # 縮小幾倍
        self.ramenButton = tk.Button(self, command=self.ramen_info, image=self.resizedImage)
        self.ramenButton.grid(row=24, column=0, columnspan=2, sticky=tk.W, pady=2)

    # 拉麵資訊新視窗
    def ramen_info(self):
        self.newWindow = tk.Toplevel(self)
        # self.newWindow.minsize('400x400')
        self.ramenTitle = tk.Label(self.newWindow, text="拉麵店名", font=('TkDefaultFont', 18))
        self.ramenTitle.grid(row=0, column=0, columnspan=2, sticky=tk.NE + tk.SW, pady=5)
        self.ramenInfo1 = tk.Label(self.newWindow, text='資訊1')
        self.ramenInfo1.grid(row=1, column=0, columnspan=1, sticky=tk.W)
        self.ramenInfo2 = tk.Label(self.newWindow, text='資訊2')
        self.ramenInfo2.grid(row=2, column=0, columnspan=1, sticky=tk.W)
        self.ramenInfo3 = tk.Label(self.newWindow, text='資訊3')
        self.ramenInfo3.grid(row=3, column=0, columnspan=1, sticky=tk.W)
        self.ramenInfo4 = tk.Label(self.newWindow, text='資訊4')
        self.ramenInfo4.grid(row=4, column=0, columnspan=1, sticky=tk.W)
        # 圖片放右邊
        self.label = tk.Label(self.newWindow, image=self.resizedImage)
        # self.label.image = self.resizedImage # keep a reference!
        self.label.grid(row=1, column=1, rowspan=5, sticky=tk.E)


root = tk.Tk()  # master
ramen = Ramen(master=root)
ramen.master.title("Ramen Python")  # window title
# start the program
ramen.mainloop()
