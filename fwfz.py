from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import threading
from windows import *
import tkinter

class Cfw:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        self.driver = webdriver.Chrome(chrome_options=options)
        screen = tkinter.Tk()
        x = screen.winfo_screenwidth()
        y = screen.winfo_screenheight()
        self.driver.set_window_rect(x - 1150, 0, 1150, 768)
        screen.destroy()
        self.username = username
        self.password = password
        self.当前装备持久 = ''
        self.当前装备计时 = ''
        self.当前体力 = ''
        self.运行操作线程()
        self.黄金数量 = ''
        self.木材数量 = ''
        self.鱼肉数量 = ''
        self.能量数量 = ''

    def 运行操作线程(self):
        self.登录账号()
        t = threading.Thread(target=self.操作线程)
        t.start()

    def 操作线程(self):
        工具列表标签 = 0
        工具计时标签 = ['','','','','','','','','']
        登录窗口卡死标签 = False
        while (1):
            # 点击确定按钮
            try:
                self.driver.find_element_by_class_name("login-button").click()  # 如果有登录按键就按
            except:
                pass
            try:
                self.driver.find_element_by_class_name("login-button--text").click()  # 等待登录按键加载
            except:
                pass
            try:
                self.driver.find_element_by_class_name('plain-button.short.undefined').click()
            except:
                pass
            # 切换工具
            try:
                工具列表元素 = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div[1]/section/div/section/img')
            except:
                pass
            try:
                self.当前装备计时 = self.driver.find_element_by_xpath("//div[@class=\'card-container--time\']").text  # 获取计时
                self.当前装备持久 = self.driver.find_element_by_xpath("//div[@class=\'content\']").text  # 获取持久度
                self.当前体力 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/section[1]/div[5]/div[2]/div').text
                # 如果当前时间为'00:00:00' 点击Mine按钮
                if self.当前装备计时 == '00:00:00':
                    self.driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div/div[1]/section/div/div/div[2]/div[3]/div[1]/button/div').click()
                # 如果当前持久为 < 50 点击Mine按钮
                if int(self.当前装备持久.split('/')[0]) < 50:
                    self.driver.find_element_by_xpath(
                        '//*[@id="root"]/div/div/div/div[1]/section/div/div/div[2]/div[3]/div[2]/button/div').click()
                if int(self.当前体力) < 50:
                    self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/section[1]/div[5]/div[3]').click()
                    while(1):
                        try:
                            self.driver.find_element_by_class_name('modal-input').send_keys(400)
                            break
                        except:
                            pass
                    while(1):
                        try:
                            self.driver.find_element_by_class_name('plain-button.long ').click()
                            break
                        except:
                            pass
            except Exception as e:
                pass
            # 查找时间为'00:00:00'的装备
            try:
                装备剩余时间 = self.driver.find_element_by_class_name('card-container--time').text
            except:
                pass
            if self.获取物资数量() == True:
                if float(self.黄金数量) < 10.0:  # 黄金低于设定的数，购买黄金
                    pass
            else:
                pass
            # 下面是出现CUP NET 质压时关闭窗口
            try:
                # <option value="CPU">CPU</option>
                # <div class="modal-stake-close">
                self.driver.find_element_by_class_name('image-button.close-modal').click()
            except:
                pass
            # 页面静止时
            计时标签 = []
            if 工具列表标签 < len(工具列表元素):
                try:
                    工具列表元素[工具列表标签].click()
                    if 工具计时标签[工具列表标签] == self.driver.find_element_by_xpath("//div[@class=\'card-container--time\']").text:
                        if 工具计时标签[工具列表标签] == '' or 工具计时标签[工具列表标签] == '00:00:00':
                            allwindows = self.driver.window_handles #   获取窗口数量。判断是不是有登录窗口卡死
                            if len(allwindows) == 1:
                                if 登录窗口卡死标签 == 0:
                                    self.driver.refresh()
                                    工具计时标签 = ['', '', '', '', '', '', '', '', '']
                            if len(allwindows) == 2:
                                if 登录窗口卡死标签 is True:
                                    self.driver.switch_to.window(allwindows[-1])
                                    self.driver.close()
                                    self.driver.switch_to.window(allwindows[0])
                                    self.driver.refresh()
                                    工具计时标签 = ['', '', '', '', '', '', '', '', '']
                                if 登录窗口卡死标签 is False:
                                    登录窗口卡死标签 = ~登录窗口卡死标签
                    工具计时标签[工具列表标签] = self.driver.find_element_by_xpath("//div[@class=\'card-container--time\']").text
                    工具列表标签 = 工具列表标签 + 1
                except:
                    pass
            else:
                工具列表标签 = 0
            time.sleep(3)

    def 登录账号(self=None):
        self.driver.get('https://play.farmersworld.io/')
        while (1):
            try:
                self.driver.find_element_by_class_name("login-button").click()  # 等待登录按键加载
                break
            except:
                pass
        while (1):
            try:
                self.driver.find_element_by_class_name("login-button--text").click()  # 等待登录按键加载
                break
            except:
                pass
        while (1):
            allwindows = self.driver.window_handles  # 等待弹出2个窗口
            if len(allwindows) < 3:
                pass
            else:
                break
        self.driver.switch_to.window(allwindows[-1])  # 切换到最后一个页面
        while (1):
            try:
                self.driver.find_element_by_name('userName').send_keys(self.username)  # 等待用户名框加载
                break
            except:
                pass
        while (1):
            try:
                self.driver.find_element_by_name('password').send_keys(self.password)  # 等待密码框加载
                break
            except:
                pass
        while (1):
            try:
                self.driver.find_element_by_class_name(
                    'button-primary.full-width.button-large.text-1-5rem.text-bold').click()  # 等待登录按键加载
                break
            except:
                pass
        while (1):
            allwindows = self.driver.window_handles  # 等待弹出窗口关闭
            if len(allwindows) > 1:
                pass
            else:
                break
        self.driver.switch_to.window(allwindows[0])  # 切换到第一个页面
        while (1):
            try:
                self.driver.find_element_by_class_name('navbar-container').is_displayed()  # 登录完成
                break
            except:
                pass

    def 获取物资数量(self):
        try:
            # //*[@id="root"]/div/div/div/section[1]/div[1]/div/div
            self.黄金数量 = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/section[1]/div[1]/div/div').text  # 黄金数量
        except:
            pass
        try:
            # //*[@id="root"]/div/div/div/section[1]/div[2]/div/div
            self.木材数量 = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/section[1]/div[2]/div/div').text  # 木材数量
        except:
            pass
        try:
            # //*[@id="root"]/div/div/div/section[1]/div[4]/div/div
            self.鱼肉数量 = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/section[1]/div[4]/div/div').text  # 鱼肉数量
        except:
            pass
        try:
            # //*[@id="root"]/div/div/div/section[1]/div[5]/div[2]/div
            self.能量数量 = self.driver.find_element_by_xpath(
                '//*[@id="root"]/div/div/div/section[1]/div[5]/div[2]/div').text  # 能量数量
        except:
            pass
        if self.黄金数量 != '' and self.木材数量 != '' and self.鱼肉数量 != '' and self.能量数量 != '':
            return True
        else:
            return False

    def 购买黄金(self,购买数量):
        self.driver.get('https://wax.alcor.exchange/trade/fwg-farmerstoken_wax-eosio.token')
        卖价列表 = self.driver.find_elements_by_class_name('ltd d-flex text-danger')
        最低卖价 = 卖价列表[len(卖价列表)-1]
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane-0"]/div/div/div[1]/form/div[5]/div/button')))
            self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[1]/div/div/input').send_keys(最低卖价)
            self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[2]/div/div/input').clear()
            self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[2]/div/div/input').send_keys(购买数量)
            #self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[5]/div/button').click()
        except:
            pass

    def 购买食物(self,购买数量):
        self.driver.get('https://wax.alcor.exchange/trade/fwf-farmerstoken_wax-eosio.token')
        卖价列表 = self.driver.find_elements_by_class_name('ltd d-flex text-danger')
        最低卖价 = 卖价列表[len(卖价列表)-1]
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pane-0"]/div/div/div[1]/form/div[5]/div/button')))
            self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[1]/div/div/input').clear()
            self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[1]/div/div/input').send_keys(最低卖价)
            self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[2]/div/div/input').clear()
            self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[2]/div/div/input').send_keys(购买数量)
            #self.driver.find_element_by_xpath('//*[@id="pane-0"]/div/div/div[1]/form/div[5]/div/button').click()
        except:
            pass
