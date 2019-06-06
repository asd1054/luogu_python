"""
题目描述
伦敦奥运会要到了，小鱼在拼命练习游泳准备参加游泳比赛，可怜的小鱼并不知道鱼类是不能参加人类的奥运会的。

这一天，小鱼给自己的游泳时间做了精确的计时（本题中的计时都按24小时制计算），它发现自己从a时b分一直游泳到当天的c时d分，请你帮小鱼计算一下，它这天一共游了多少时间呢？

小鱼游的好辛苦呀，你可不要算错了哦。

输入输出格式
输入格式：
一行内输入 4 个整数，分别表示 a, b, c, d。

输出格式：
一行内输出 2 个整数 e 和 f，用空格间隔，依次表示小鱼这天一共游了多少小时多少分钟。其中表示分钟的整数 f 应该小于60。

输入输出样例
输入样例#1： 
12 50 19 10
输出样例#1： 
6 20
说明
对于全部测试数据，0\le a,c \le 240≤a,c≤24，0\le b,d \le 600≤b,d≤60，且结束时间一定晚于开始时间。
"""

# 测试数据较少懒得修改了
# a,b,c,d = map(int,input().split()) # 也可以 eval(input().split())
# minute = 0
# hour = 0
# if b > d:
#     hour += 1
#     minute = 60-b + d
# else :
#     minute = d - b
# hour += c-a -1
# print(hour,minute)


a,b,c,d = map(int,input().split()) # 也可以 eval(input().split()) 测试貌似不行。。
sum = c*60+d-a*60-b
hour = int(sum/60)
minute = sum%60
print(hour,minute)