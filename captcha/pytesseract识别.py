# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 15:56:48 2021

@author: latpurple
"""

from PIL import Image
import pytesseract
import os

base_path='captcha/'
name_dir=os.listdir(base_path)
for name in name_dir:
    file_name=name.split('.')[0]
    
    print(name.split('.')[0])
    img=Image.open(base_path+name)
    gary=img.convert('L')    #灰度处理
    bw=gary.point(lambda x:0 if x<150 else 255,"1") #二值化
    bw.save(open('result/'+file_name+'.png','wb'),'png') #调用库进行识别
    resul=pytesseract.image_to_string(bw,lang='eng',config='--psm 10')[:-1]
    print("{} 处理结果是: {}".format(file_name,resul))