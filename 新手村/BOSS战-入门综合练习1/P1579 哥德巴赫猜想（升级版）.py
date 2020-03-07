# -*- coding: utf-8 -*-
"""
@Author       : wukong
@Date         : 2020-03-07 15:58:28
@Description  : 歌德巴赫猜想升级版
@blog         : https://asd1054.github.io/
@Github       : https://github.com/asd1054
@version      : 1.0
"""
# 题目背景
# 1742年6月7日哥德巴赫写信给当时的大数学家欧拉，正式提出了以下的猜想：任何一个大于9的奇数都可以表示成3个质数之和。质数是指除了1和本身之外没有其他约数的数，如2和11都是质数，而6不是质数，因为6除了约数1和6之外还有约数2和3。需要特别说明的是1不是质数。

# 这就是哥德巴赫猜想。欧拉在回信中说，他相信这个猜想是正确的，但他不能证明。

# 从此，这道数学难题引起了几乎所有数学家的注意。哥德巴赫猜想由此成为数学皇冠上一颗可望不可及的“明珠”。

# 题目描述
# 现在请你编一个程序验证哥德巴赫猜想。

# 先给出一个奇数n，要求输出3个质数，这3个质数之和等于输入的奇数。

# 输入格式
# 仅有一行，包含一个正奇数n，其中9<n<20000

# 输出格式
# 仅有一行，输出3个质数，这3个质数之和等于输入的奇数。相邻两个质数之间用一个空格隔开，最后一个质数后面没有空格。如果表示方法不唯一，请输出第一个质数最小的方案，如果第一个质数最小的方案不唯一，请输出第一个质数最小的同时，第二个质数最小的方案。

# 输入输出样例
# 输入 #1复制
# 2009
# 输出 #1复制
# 3 3 2003

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


def output():
    for i in range(2, n):
        if isPrime(i):
            for j in range(2, n - i):
                k = n - i - j
                if not isPrime(j) or not isPrime(k):
                    continue
                if i + j + k > n:
                    break
                if i + j + k == n:
                    print(i, j, k)
                    return


n = int(input())  # 9<n<20000
output()
