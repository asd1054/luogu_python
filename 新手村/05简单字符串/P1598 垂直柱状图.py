# -*- coding: utf-8 -*-
'''
@Author: wukong
@Date: 2019-06-13 17:37:34
'''
# coding : utf-8

'''
题目描述
写一个程序从输入文件中去读取四行大写字母（全都是大写的，每行不超过100个字符），然后用柱状图输出每个字符在输入文件中出现的次数。严格地按照输出样例来安排你的输出格式。

输入输出格式
输入格式：
四行字符，由大写字母组成，每行不超过100个字符

输出格式：
由若干行组成，前几行由空格和星号组成，最后一行则是由空格和字母组成的。在任何一行末尾不要打印不需要的多余空格。不要打印任何空行。

输入输出样例
输入样例#1： 
THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG.
THIS IS AN EXAMPLE TO TEST FOR YOUR
HISTOGRAM PROGRAM.
HELLO!
输出样例#1： 
                            *
                            *
        *                   *
        *                   *     *   *
        *                   *     *   *
*       *     *             *     *   *
*       *     * *     * *   *     * * *
*       *   * * *     * *   * *   * * * *
*     * * * * * *     * * * * *   * * * *     * *
* * * * * * * * * * * * * * * * * * * * * * * * * *
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
说明
每行输出后面不允许出现多余的空格。
'''

def list_add(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c

from functools  import reduce #累次计算

artcle = input()
artcle += input()
artcle += input()
artcle += input()

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
bottom = ' '.join(alphabet)
s = dict.fromkeys(alphabet,0)
1234

for i in range(65,91):
	key = chr(i)
	num = artcle.count(key)
	s[key] = num
length = sorted(s.items(),key=lambda x:x[1],reverse=True)[0][1]

content = []
for i in range(65,91):
    key = chr(i)
    tmpl = s[key]
    tmps = '*' * tmpl
    tmps = '\n'.join(tmps.rjust(length,' '))
    content.append(tmps)
    if i != 90:
        content.append(' '*length)
tmp = []
for i in content:
    tmp.append(i.replace('\n',''))
above = []
above = reduce(list_add,tmp)
above.append(bottom)
for i in above:
    print(i)