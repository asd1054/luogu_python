# -*- coding: utf-8 -*-
'''
@Author: wukong
@Date: 2019-06-10 19:07:13
'''
# coding : utf-8 
'''
题目描述
一般的文本编辑器都有查找单词的功能，该功能可以快速定位特定单词在文章中的位置，有的还能统计出特定单词在文章中出现的次数。

现在，请你编程实现这一功能，具体要求是：给定一个单词，请你输出它在给定的文章中出现的次数和第一次出现的位置。注意：匹配单词时，不区分大小写，但要求完全匹配，即给定单词必须与文章

中的某一独立单词在不区分大小写的情况下完全相同（参见样例1 ），如果给定单词仅是文章中某一单词的一部分则不算匹配（参见样例2 ）。

输入输出格式
输入格式：
共22行。

第11行为一个字符串，其中只含字母，表示给定单词；

第22行为一个字符串，其中只可能包含字母和空格，表示给定的文章。

输出格式：
一行，如果在文章中找到给定单词则输出两个整数，两个整数之间用一个空格隔开，分别是单词在文章中出现的次数和第一次出现的位置（即在文章中第一次出现时，单词首字母在文章中的位置，位置从00 开始）；如果单词在文章中没有出现，则直接输出一个整数-1−1。

输入输出样例
输入样例#1： 
To
to be or not to be is a question
输出样例#1： 
2 0

输入样例#2： 
to
Did the Ottoman Empire lose its power at that time
输出样例#2： 
-1
说明
数据范围

1≤ 1≤单词长度≤10≤10。

1≤ 1≤文章长度≤1,000,000≤1,000,000。
'''


import pdb
# 没有现成的方法实现，只好自己写算法了 ，，哈哈
word = input().lower()
essay = input().lower()
tmp_word = ''
pd_letter = 1
sum = 0
ans = -1
for i in range(len(essay)):
    if essay[i] == ' ':
        pd_letter = 0
    if pd_letter == 1:
        tmp_word += essay[i]
    else:
        if word == tmp_word:
            sum += 1
            # pdb.set_trace()
            if sum ==1:
                ans = i-len(word)
        tmp_word = ''
        pd_letter = 1
        
if ans == -1:
    print(-1)
else:
    print(sum,ans)

     
        
        