# -*- coding: utf-8 -*-
'''
@Author: wukong
@Date: 2019-06-10 19:44:10
'''
# coding:utf-8
'''
题目描述
给定一个数，请将该数各个位上数字反转得到一个新数。

这次与NOIp2011普及组第一题不同的是：这个数可以是小数，分数，百分数，整数。整数反转是将所有数位对调；小数反转是把整数部分的数反转，再将小数部分的数反转，不交换整数部分与小数部分；分数反转是把分母的数反转，再把分子的数反转，不交换分子与分母；百分数的分子一定是整数，百分数只改变数字部分。整数新数也应满足整数的常见形式，即除非给定的原数为零，否则反转后得到的新数的最高位数字不应为零；小数新数的末尾不为0（除非小数部分除了0没有别的数，那么只保留1个0）；分数不约分，分子和分母都不是小数（约分滴童鞋抱歉了，不能过哦。输入数据保证分母不为0），本次没有负数。

输入输出格式
输入格式：
一个数s

输出格式：
一个数，即s的反转数

输入输出样例
输入样例#1： 
5087462
输出样例#1： 
2647805
输入样例#2： 
600.084
输出样例#2： 
6.48
输入样例#3： 
700/27
输出样例#3： 
7/72
输入样例#4： 
8670%
输出样例#4： 
768%
说明
所有数据：25%s是整数，不大于20位

25%s是小数，整数部分和小数部分均不大于10位

25%s是分数，分子和分母均不大于10位

25%s是百分数，分子不大于19位

（20个数据）
'''

# 只能得到 65分 无能为力了。。
# 如果发现问题 也可以联系我
# def isReverse(s):
#     tmp1 = ''
#     first = 1
#     for i in range(len(s)-1,-1,-1):
#         if s[i]== '0' and first == 1:
#             continue
#         else:
#             first = 0
#         tmp1 += s[i]
#     tmp =tmp1
#     for i in range(len(tmp1)-1,-1,-1) :
#         if tmp1[i] =='0':
#             tmp = tmp1[0:i]
#         else:
#             break
#     return tmp

# import pdb
# s = input()
# if s.isdigit():
#     tmp = isReverse(s)
#     print(tmp)
# elif r'.' in s :
#     mid = s.find('.')
#     tmp1 = isReverse(s[0:mid])
#     tmp2 = isReverse(s[mid+1:])
#     if s[mid+1:] == '0':
#         tmp2 = '0'
#     tmp = tmp1 +r'.'+tmp2
#     # pdb.set_trace()
#     print(tmp)
# elif r'/' in s :
#     mid = s.find(r'/')
#     tmp1 = isReverse(s[0:mid])
#     tmp2 = isReverse(s[mid+1:])
#     tmp = tmp1 +r'/'+tmp2
#     print(tmp)
# elif r'%' in s :
#     tmp = ''
#     for i in s:
#         if i == '0':
#             continue
#         tmp +=i
#     mid = tmp.index('%')
#     s= tmp[mid-1::-1]+'%'+tmp[-1:mid:-1]
#     print(s)

# 分成两块，先输出前一个数，判断有无符号，无return0，有再输出第二个数；
# 以下是翻译其他人的杰作。。
p = 0 # 放符号
cnt = 0
s = input()
for i in s:
    if i>= '0' and i <= '9' :
        cnt +=1
    else:
        p = i
        break
x = cnt
cnt -=1
while (s[cnt]=='0' and cnt > 0):
    cnt -=1 #去除多余前导0； 
for i in range(cnt,-1,-1):
    print(s[i],end='')
if p == 0:
    pass
else:
    if p=='%':
        print(p)
    else:
        print(p,end='')
        m = s.__len__() -1
        while(s[x+1]=='0' and x<m-1):
            x+=1 #去除末尾0 
        while(s[m]=='0' and m >x+1):
            m-=1 #去除多余前导0
        for i in range(m,x,-1):
            print(s[i],end = '')
