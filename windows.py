from tkinter import *
from fwfz import *

class CWindows:
    def __init__(self):
        from tkinter import Tk
        # 初始化Tk()
        self.myWindow = Tk()
        # 设置标题
        self.myWindow.title('FWFZ')
        # 设置窗口大小
        width = 280
        height = 210
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.myWindow.winfo_screenwidth()
        screenheight = self.myWindow.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.myWindow.geometry(alignstr)
        # 设置窗口是否可变长、宽，True：可变，False：不可变
        self.myWindow.resizable(width=False, height=False)
        # 定义label关联字符串
        self.password = StringVar()
        self.装备 = StringVar()
        self.时间 = StringVar()
        self.黄金 = StringVar()
        self.木材 = StringVar()
        self.鱼肉 = StringVar()
        self.能量 = StringVar()
        # 控件布局与方法关联
        self.添加控件()
        # 进入消息循环
        self.myWindow.mainloop()
    def update(self):
        try:
            self.装备.set('持久:'+self.m_Cfw.当前装备持久)
            self.时间.set('时间:'+self.m_Cfw.当前装备计时)
            self.黄金.set('黄金:'+self.m_Cfw.黄金数量)
            self.木材.set('木材:'+self.m_Cfw.木材数量)
            self.鱼肉.set('鱼肉:'+self.m_Cfw.鱼肉数量)
            self.能量.set('能量:'+self.m_Cfw.当前体力)
        except:
            pass
        self.myWindow.after(1000, self.update)
    def 添加控件(self):
        self.装备.set('持久:')
        self.时间.set('时间:')
        self.黄金.set('黄金:')
        self.木材.set('木材:')
        self.鱼肉.set('鱼肉:')
        self.能量.set('能量:')

        # 定义控件变量
        self.label_UserName = Label(self.myWindow, text="用户名:", width=6, height=1)
        self.label_PassWord = Label(self.myWindow, text="密  码:", width=6, height=1)
        self.text_UserName = Entry(self.myWindow, width=25)
        self.text_PassWord = Entry(self.myWindow, show='*', width=25)
        self.btn_登陆 = Button(self.myWindow, text='登陆', width=8, height=1, command=self.btn1fun)
        self.label_装备 = Label(self.myWindow, textvariable=self.装备, width=0, height=1)
        self.label_时间 = Label(self.myWindow, textvariable=self.时间, width=0, height=1)
        self.label_黄金 = Label(self.myWindow, textvariable=self.黄金, width=0, height=1)
        self.label_木材 = Label(self.myWindow, textvariable=self.木材, width=0, height=1)
        self.label_鱼肉 = Label(self.myWindow, textvariable=self.鱼肉, width=0, height=1)
        self.label_能量 = Label(self.myWindow, textvariable=self.能量, width=0, height=1)

        # 控件布局
        self.label_UserName.grid(column= 0, row = 0, columnspan=1, sticky=W)
        self.label_PassWord.grid(column= 0, row = 1, columnspan=1, sticky=W)
        self.btn_登陆.grid(column=6, row=0, rowspan=2,sticky=W, padx=5, pady=0)
        self.text_UserName.grid(column=1, row=0, columnspan=5, sticky=W)
        self.text_PassWord.grid(column=1, row=1, columnspan=5, sticky=W)
        self.label_装备.grid(column=0, row=2, columnspan=3, sticky=W)
        self.label_时间.grid(column=4, row=2, columnspan=3, sticky=W)
        self.label_黄金.grid(column=0, row=3, columnspan=3, sticky=W)
        self.label_木材.grid(column=4, row=3, columnspan=3, sticky=W)
        self.label_鱼肉.grid(column=0, row=4, columnspan=3, sticky=W)
        self.label_能量.grid(column=4, row=4, columnspan=3, sticky=W)
        # labelFrame_自动买卖 = LabelFrame(self.myWindow, text="自动买卖:", width=300, height=70).grid(column=0, row=5, columnspan=7, sticky=W)
        #btn_自动卖 = Button(self.myWindow, text='自动卖', width=8, height=0).grid(column=0, row=5, sticky=W, padx=0, pady=0)
    def btn1fun(self):
        m_UserName = self.text_UserName.get()
        m_PassWord = self.text_PassWord.get()
        self.m_Cfw = Cfw(m_UserName, m_PassWord)
        self.text_UserName['state'] = DISABLED
        self.text_PassWord['state'] = DISABLED
        self.btn_登陆['state'] = DISABLED
        self.myWindow.after(1000, self.update)



