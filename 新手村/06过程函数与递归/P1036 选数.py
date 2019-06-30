# -*- coding: utf-8 -*-
'''
@Author: wukong
@Date: 2019-06-29 10:06:22
'''
"""
题目描述
已知 nn 个整数 x_1,x_2,…,x_nx 
1
​	 ,x 
2
​	 ,…,x 
n
​	 ，以及11个整数kk(k<nk<n)。从nn个整数中任选kk个整数相加，可分别得到一系列的和。例如当n=4,k=3n=4,k=3,44个整数分别为3,7,12,193,7,12,19时，可得全部的组合与它们的和为：

3+7+12=223+7+12=22

3+7+19=293+7+19=29

7+12+19=387+12+19=38

3+12+19=343+12+19=34。

现在，要求你计算出和为素数共有多少种。

例如上例，只有一种的和为素数：3+7+19=293+7+19=29。

输入输出格式
输入格式：
键盘输入，格式为：

n,kn,k(1 \le n \le 20,k<n1≤n≤20,k<n)

x_1,x_2,…,x_n (1 \le x_i \le 5000000)x 
1
​	 ,x 
2
​	 ,…,x 
n
​	 (1≤x 
i
​	 ≤5000000)
输出格式：
屏幕输出，格式为： 11个整数（满足条件的种数）。

输入输出样例
输入样例#1： 
4 3
3 7 12 19
输出样例#1： 
1
"""
# #import pdb
# cnt = 0
# def combination(x):
#     global cnt 
#     for i in range(0,x.__len__()):
#         for j in range(i+1,x.__len__()):
#             for k in range(j+1,x.__len__()):
#                 # pdb.set_trace()
#                 t = x[i] + x[j] +x[k]
#                 # print(t)
#                 # print(x[i] , x[j] , x[k])
#                 if isPrime(t):
#                     cnt +=1
# def isPrime(num):
#     for i in range(2,num):
#         if (num % i) == 0:
#             return False
#     return True
# n , k = map(int,input().split())
# x =list(map(int,input().split()))
# x  = list(set(x))
# combination(x)
# print(cnt)


# DFS 算法
total = 0
n , k = map(int,input().split())
x =list(map(int,input().split()))
def isPrime(num):
    for i in range(2,num):
        if (num % i) == 0:
            return False
    return True
def dfs(step,sum,cnt):
    global total,x
    if(step == n +1 or cnt ==k):
        if(isPrime(sum) and cnt == k):
            total +=1
        return
    dfs(step+1,sum+x[step-1],cnt+1)
    dfs(step+1,sum,cnt)

dfs(1,0,0)
print(total)
