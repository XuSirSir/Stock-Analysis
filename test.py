# -*- coding: utf-8 -*-
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.pylab import date2num
import matplotlib.finance as mpf
import xlrd
import tushare as ts
import matplotlib


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'

##df = ts.get_hist_data('600028')
##df.to_excel('H:/600028.xlsx')

fname = r"H:\600028.xlsx"
bk = xlrd.open_workbook(fname)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print("no sheet in %s named Sheet1" % fname)

data_list = []
data_open = []
data_high = []
data_low = []
data_time = []
data_close = []
new_data_time = []
for i in range(1,100):
    row_open = sh.cell_value(i,1)
    row_close = sh.cell_value(i,3)
    row_high = sh.cell_value(i,2)
    row_low = sh.cell_value(i,4)
    row_time = sh.cell_value(i,0)

    date_time = datetime.strptime(row_time,'%Y-%m-%d')
    new_data_time.append(date_time)

    t=date2num(date_time)

    data_open.append(row_open)

    data_time.append(t)


    datas = (t,row_open,row_high,row_low,row_close)
    data_list.append(datas)

def plot_k_line():
    #定义一个窗口
    fig = plt.figure()
    #把窗口分为2行1列，取第二行
    ax = fig.add_subplot(212)
    fig.subplots_adjust(bottom=0.2)
    # 设置X轴刻度为日期时间  
    ax.xaxis_date()  
    plt.xticks(rotation=45)  
    plt.yticks()  
    #plt.title(u"中国石化-600028")  
    plt.xlabel(u"时间")  
    plt.ylabel(u"股价（元）")
    mpf.candlestick_ohlc(ax,data_list,width=1.5,colorup='r',colordown='green')  
    plt.grid()

    fig.add_subplot(211)
    ax.xaxis_date()
    fig.set_size_inches(19.2,10.8)
    plt.title(u"中国石化-600028")
    plt.xlabel(u"时间")
    plt.ylabel(u"股价（元）")
    plt.plot(new_data_time, data_open, 'r')
    plt.savefig("H:\\photo1.png",dpi=100)
    plt.show()                                                                                                                                                                                              

def plot_line():
    fig,ax = plt.subplots()
    ax.xaxis_date()
    #fig.set_size_inches(19.2,10.8)
    plt.title(u"中国石化-600028")
    plt.xlabel(u"时间")
    plt.ylabel(u"股价（元）")
    plt.plot(new_data_time, data_open, 'r')
    plt.savefig("H:\\photo2.png",dpi=100)
    plt.show()

def plot_K():
    #定义一个窗口
    fig, ax = plt.subplots()
    fig.subplots_adjust(bottom=0.2)
    # 设置X轴刻度为日期时间
    ax.xaxis_date()  
    plt.xticks(rotation=45)  
    plt.yticks()  
    plt.title(u"中国石化-600028")  
    plt.xlabel(u"时间")  
    plt.ylabel(u"股价（元）")
    mpf.candlestick_ohlc(ax,data_list,width=1.5,colorup='r',colordown='green')  
    plt.grid()
    plt.savefig("H:\\photo3.png",dpi=100)
    plt.show()

plot_k_line()
plot_line()
plot_K()


