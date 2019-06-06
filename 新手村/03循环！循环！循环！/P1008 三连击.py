'''
题目背景
本题为提交答案题，您可以写程序或手算在本机上算出答案后，直接提交答案文本，也可提交答案生成程序。

题目描述
将1,2, \cdots ,91,2,⋯,9共99个数分成33组，分别组成33个三位数，且使这33个三位数构成1:2:31:2:3的比例，试求出所有满足条件的33个三位数。

输入输出格式
输入格式：
木有输入

输出格式：
若干行，每行33个数字。按照每行第11个数字升序排列。

输入输出样例
输入样例#1： 
无
输出样例#1： 
192 384 576
* * *
...

* * *
（输出被和谐了）
'''




def isSame(n):
    a = n//100
    b = n//10 % 10
    c = n % 10
    if a == b or a ==c or b == c:
        return False
    else :
        return True

def isAllSame(a,b,c):
    num = []
    aim = [a,b,c]
    for i in aim:
        tmp = i//100
        num.append(tmp)
        tmp = i//10 % 10
        num.append(tmp)
        tmp = i % 10
        num.append(tmp)
    # 列表去重
    num = list(set(num))
    if len(num) <9:
        return False
    else :
        return True

for i in range(123,333):
    
    if isSame(i):
        a = i
        b = 2*i
        c = 3*i
        if isAllSame(a,b,c):
            print(a,b,c)