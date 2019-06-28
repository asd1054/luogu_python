# -*- coding: utf-8 -*-
'''
@Author: wukong
@Date: 2019-06-28 15:24:28
'''
"""
题目背景
某蒟蒻迷上了“小书童”，有一天登陆时忘记密码了（他没绑定邮箱or手机），于是便把问题抛给了神犇你。

题目描述
蒟蒻虽然忘记密码，但他还记得密码是由一个字符串组成。密码是由原文字符串（由不超过 50 个小写字母组成）中每个字母向后移动 nn 位形成的。z 的下一个字母是 a，如此循环。他现在找到了移动前的原文字符串及 nn，请你求出密码。

输入输出格式
输入格式：
第一行：n。第二行：未移动前的一串字母

输出格式：
一行，是此蒟蒻的密码

输入输出样例
输入样例#1： 
1
qwe
输出样例#1： 
rxf
说明
字符串长度<=50
"""

# 说白了其实就是凯撒密码 
n = int(input())
s = input()
cipher = ''
for i in s:
    if ord('A') <= ord(i) <= ord('Z') or ord("a") <= ord(i) <= ord("z"):
        if ord(i) > 96:
            #小写
            tmp = (ord(i)-96+n)%26 +96
            if tmp == 96:
                tmp += 26                   
            cipher += chr(tmp)
        else :
            #大写
            tmp = (ord(i)-64+n)%26 +64
            if tmp == 64:
                tmp += 26 
            cipher += chr(tmp)
    else:
        cipher += i
print(cipher)