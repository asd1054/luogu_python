'''
题目描述
已知：S_n= 1+1/2+1/3+…+1/nS 
n
​	 =1+1/2+1/3+…+1/n。显然对于任意一个整数KK，当nn足够大的时候，S_nS 
n
​	 大于KK。

现给出一个整数KK（1 \le k \le 151≤k≤15），要求计算出一个最小的nn；使得S_n>KS 
n
​	 >K。

输入输出格式
输入格式：
一个正整数KK
输出格式：
一个正整数NN
输入输出样例
输入样例#1： 
1
输出样例#1： 
2
'''
import pdb
k = int(input())
Sn = 0
n = 1
while 1:
    Sn += 1.0/n
    
    n +=1
    if Sn > k:
        break
    #pdb.set_trace()
print(n)

