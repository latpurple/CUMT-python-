# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 18:12:33 2021

@author: latpurple
"""

import random

#生成数字--字母表
# words_dir=[]
# for i in range(10):
#     words_dir.append(i)

# for i in range(ord('A'),ord('A')+26):
#     words_dir.append(chr(i))

# for i in range(ord('a'),ord('a')+26):
#     words_dir.append(chr(i))

# print(words_dir)

words_dir=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 
           'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
           'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 
           'c', 'd', 'e', 'f', 'g', 'h', 'i', 
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 
           'x', 'y', 'z']
# print(words_dir)

#生成8--10位长度的密码
EIGHT=8
NINE=9
TEN=10

def create_dir(charset=words_dir,length=8):
    tmp=[]
    for i in range(length):
        # print(random.choice(charset))
        tmp.append(str(random.choice(charset)))
    # print(tmp)
    passwd=''.join(tmp)
    return passwd

# passwd=create_dir()
# with open('passwd.txt','w') as f:
#     f.write(passwd)
#     f.write('\n')

#生成8、9、10长度的密码
for num in [8,9,10]:
    print(num)    
    for i in range(500):
        passwd=create_dir(length=num)
        #以追加方式写入   
        with open('passwd.txt','a') as f:
            f.write(passwd)
            f.write('\n')
    print('密码生成完成')