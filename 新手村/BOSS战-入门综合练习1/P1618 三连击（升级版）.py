# -*- coding: utf-8 -*-
"""
@Author       : wukong
@Date         : 2020-02-26 14:24:52
@LastEditTime : 2020-02-26 14:25:05
@Description  : 三连击（升级版）
@blog         : https://asd1054.github.io/
@Github       : https://github.com/asd1054
@version      : 1.0
"""
# 题目描述
# 将 1, 2,\ldots, 91,2,…,9 共 99 个数分成三组，分别组成三个三位数，且使这三个三位数的比例是
# :B:CA:B:C，试求出所有满足条件的三个三位数，若无解，输出 No!!!。

# //感谢黄小U饮品完善题意

# 输入格式
# 三个数，A,B,CA,B,C。

# 输出格式
# 若干行，每行 33 个数字。按照每行第一个数字升序排列。

# 输入输出样例
# 输入 #1复制
# 1 2 3
# 输出 #1复制
# 192 384 576
# 219 438 657
# 273 546 819
# 327 654 981
# 说明/提示
# 保证 A<B<CA<B<C。


# def unique():
#     """
#     @description:
#         用来找到100-999中不同的数

#     @return:
#         返回一个列表
#     """
#     goal = []
#     for i in range(1, 10):
#         for j in range(1, 10):
#             for k in range(1, 10):
#                 if i != k and i != j and j != k:
#                     goal.append(i * 100 + j * 10 + k)
#     return goal


# def sameUnique(a, b, c):
#     """
#     @description:
#         同时判断三个数是否有一样的，且满足比例关系

#     @return:
#         True or False

#     """
#     pd = str(a) + str(b) + str(c)
#     if len(set(pd)) == 9 and (a * B == b and a * C == c):
#         return True
#     else:
#         return False


# A, B, C = map(int, input().split())
# goal = unique()
# target = []
# # 毕竟还是三个循环 还是太卡了，还得优化
# # for index, value in enumerate(goal):
# #     for j in range(index + 1, len(goal)):
# #         for k in range(index + 2, len(goal)):
# #             if sameUnique(value, goal[j], goal[k]):
# #                 print(value, goal[j], goal[k])


def isAllUnique(a, b, c):
    pd = str(a) + str(b) + str(c)
    if len(pd) == 9 and "0" not in pd:
        return True
    else:
        return False


A, B, C = map(int, input().split())

# # 看了 一下以前的方法，其实一个循环就够了。。。
target = []
for i in range(123, 333):
    if isAllUnique(i, i * B, i * C):
        target.append((i, i * B, i * C))
if target:
    for i, j, k in target:
        print(i, j, k)
else:
    print("No!!!")
# 只得80分，还差最后一个数据没有通过
# TODO to be continued
