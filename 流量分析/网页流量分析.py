# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 20:41:26 2021

@author: latpurple
"""

import matplotlib.pyplot as plt
import sqlite3

def get_moz_origins_data():
    #指定浏览记录路径
    history_db='places.sqlite'
    #连接sqlite数据库
    c=sqlite3.connect(history_db)
    cursor=c.cursor()
    select_statement="select prefix,host,frecency from 'moz_origins' order by frecency desc limit 10"
    #执行查询语句
    cursor.execute(select_statement)
    results = cursor.fetchall()
    print(len(results))
    data={}
    for result in results:
        #将前缀跟域名结合成url，作为字典的索引，访问次数作为字典值
        print(result[0],result[1],result[2])
        url=result[0]+result[1]
        count=result[2]
        data[url]=count
    return data

def analyze(data):
    #利用matplotlib进行绘图操作
    plt.bar(range(len(data)),data.values(),align='edge')
    plt.xticks(rotation=70)
    plt.xticks(range(len(data)),data.keys())
    plt.show()
    
if __name__ == '__main__':
    data=get_moz_origins_data()
    analyze(data)