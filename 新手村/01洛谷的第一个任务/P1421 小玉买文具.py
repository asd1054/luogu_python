"""
题目描述
班主任给小玉一个任务，到文具店里买尽量多的签字笔。已知一只签字笔的价格是1元9角，而班主任给小玉的钱是a元b角，小玉想知道，她最多能买多少只签字笔呢。

输入输出格式
输入格式：
输入的数据，在一行内，包括两个整数，依次表示a和b，a<=10000,b<=9。

输出格式：
输出一个整数，表示小玉最多能买多少只签字笔。

输入输出样例
输入样例#1： 
10 3
输出样例#1： 
5
"""

a,b = input().split(' ') # a yuan b jiao
s = int((int(a)*10+int(b))//19)
print(s)