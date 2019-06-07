'''
题目描述
试计算在区间 11 到 n n的所有整数中，数字 x(0 ≤ x ≤ 9)x(0≤x≤9)共出现了多少次？例如，在 11到 11 11中，即在 1,2,3,4,5,6,7,8,9,10,111,2,3,4,5,6,7,8,9,10,11 中，数字 11 出现了 44 次。

输入输出格式
输入格式：
22个整数n,xn,x，之间用一个空格隔开。

输出格式：
11个整数，表示xx出现的次数。

输入输出样例
输入样例#1： 
11 1
输出样例#1： 
4
说明
对于 100\%100%的数据，1≤ n ≤ 1,000,000,0 ≤ x ≤ 91≤n≤1,000,000,0≤x≤9。
'''

n,x = input().split()
sum = 0 
for i in range(1,int(n)+1):
    tmp =str(i)
    if tmp.count(x):
        sum +=tmp.count(x)
print(sum)