'''
@Author: wukong
@Date: 2019-07-04 14:37:18
'''
"""
题目描述
因为 151 既是一个质数又是一个回文数（从左到右和从右到左是看一样的），所以 151 是回文质数。

写一个程序来找出范围 [a,b] (5 \le a < b \le 100,000,000)[a,b](5≤a<b≤100,000,000)( 一亿)间的所有回文质数。

输入输出格式
输入格式：
第 1 行: 二个整数 a 和 b .

输出格式：
输出一个回文质数的列表，一行一个。

输入输出样例
输入样例#1： 
5 500
输出样例#1： 
5
7
11
101
131
151
181
191
313
353
373
383
说明
Hint 1: Generate the palindromes and see if they are prime.

提示 1: 找出所有的回文数再判断它们是不是质数（素数）.

Hint 2: Generate palindromes by combining digits properly. You might need more than one of the loops like below.

提示 2: 要产生正确的回文数，你可能需要几个像下面这样的循环。

题目翻译来自NOCOW。

USACO Training Section 1.5

产生长度为5的回文数:

for (d1 = 1; d1 <= 9; d1+=2) {    // 只有奇数才会是素数
     for (d2 = 0; d2 <= 9; d2++) {
         for (d3 = 0; d3 <= 9; d3++) {
           palindrome = 10000*d1 + 1000*d2 +100*d3 + 10*d2 + d1;//(处理回文数...)
         }
     }
 }
 """


import math


def isPrime(num):
    """
    判断是否是质数
    
    参数
    ----
    num: int 测试的数字
    """
    if num == 1:
        return False
    elif (num % 2) == 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num) + 1)):
            if (num % i) == 0:
                return False
        return True


def checkBit(num):
    """
    检查位数，4位6位的 直接排除掉
    """
    if ((1000 <= num and num <= 9999) or (100000 <= num and num <= 999999)):
        return False
    return True


def isHuiWenShu(num):
    """
    判断回文数
    """
    huiwenshu = 0
    tmp = num
    while (tmp):
        huiwenshu = huiwenshu * 10 + tmp % 10
        tmp //= 10
    if huiwenshu == num:
        return True
    return False


a, b = map(int, input().split())
# 有一种玄学的证明方法,有偶数位的回文数（除了11）必然不是质数
# 证明方法：显然
# 这个数必为11的倍数
if a % 2 == 0:
    a += 1  # 方便后面遍历直接 奇数加2
b = min(9999999, b)  # 再大的书都不可能是回文质数 因为最大可能取到的数是1亿
for i in range(a, b + 1, 2):
    if checkBit(i) is False:
        continue
    if isHuiWenShu(i) is False:
        continue
    if isPrime(i) is False:
        continue
    print(i)


## 剩下