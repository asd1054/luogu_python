# -*- coding: utf-8 -*-
"""
@Author       : wukong
@Date         : 2020-02-18 23:55:05
@LastEditTime : 2020-02-26 14:06:42
@Description  : 暂无描述
@blog         : https://asd1054.github.io/
@Github       : https://github.com/asd1054
@version      : 1.0
"""
# """
# 题目描述
# 又是一年秋季时，陶陶家的苹果树结了 nn 个果子。陶陶又跑去摘苹果，这次他有一个 aa 公分的椅子。当他手够不着时，他会站到椅子上再试试。

# 这次与 NOIp2005 普及组第一题不同的是：陶陶之前搬凳子，力气只剩下 ss 了。当然，每次摘苹果时都要用一定的力气。陶陶想知道在 s<0s<0 之前最多能摘到多少个苹果。

# 现在已知 nn 个苹果到达地上的高度 x_ix
# i
# ​
#  ，椅子的高度 aa，陶陶手伸直的最大长度 bb，陶陶所剩的力气 ss，陶陶摘一个苹果需要的力气 y_iy
# i
# ​
#  ，求陶陶最多能摘到多少个苹果。

# 输入格式
# 第 11 行：两个数 苹果数 nn，力气 ss。

# 第 22 行：两个数 椅子的高度 aa，陶陶手伸直的最大长度 bb。

# 第 33 行~第 3+n-13+n−1 行：每行两个数 苹果高度 x_ix
# i
# ​
#  ，摘这个苹果需要的力气 y_iy
# i
# ​
#  。

# 输出格式
# 只有一个整数，表示陶陶最多能摘到的苹果数。

# 输入输出样例
# 输入 #1复制
# 8 15
# 20 130
# 120 3
# 150 2
# 110 7
# 180 1
# 50 8
# 200 0
# 140 3
# 120 2
# 输出 #1复制
# 4
# 说明/提示
# 对于 100\%100% 的数据，n\leq 5000n≤5000, a\leq 50a≤50, b\leq 200b≤200, s\leq 1000s≤1000, x_i\leq 280x
# i
# ​
#  ≤280, y_i\leq 100y
# i
# ​
#  ≤100。
#  """


def oldMeans():
    apple = list(map(int, input().split()))
    taotao = int(input()) + 30
    sum = 0
    for one in apple:
        if one <= taotao:
            sum += 1
    print(sum)


apple_num, tao_power = tuple(map(int, input().split()))
tao_len = sum(map(int, input().split()))
data = list()
for _ in range(apple_num):
    x, y = list(map(int, input().split()))
    if x > tao_len:
        continue
    else:
        data.append((x, y))
data = sorted(data, key=lambda x: x[1])
num = 0
for x, y in data:
    if y <= tao_power:
        num += 1
        tao_power -= y
    else:
        break
print(num)
