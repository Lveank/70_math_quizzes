# -*- coding:utf-8 -*-

"""
假设要把长度为n厘米的木棒切分为1厘米长的小段，但是1根木棒只能由1人切分，
当木棒被切分为3段后，可以同时由3个人分别切分木棒。 求最多有m个人时，最少要切分几次。
Q1：当n=20，m=3时的最少切分次数
Q2：当n=100，m=5时的最少切分次数
"""


def cutbar(n, m, current):
    count = 0
    while n > current:
        # 换种方式写if-else，参考下文注释。[条件不成立的结果, 条件成立的结果][条件]
        # 如果节数（current）小于人数，那么将节数增倍；否则只增加人数(m)节
        current = [m + current, 2 * current][current < m]
        # 计数+1
        count = count + 1

    return count


if __name__ == '__main__':
    print(cutbar(20, 3, 1))  # 8
    print(cutbar(100, 5, 1))  # 22

# 注：if-else的多种写法：
# a, b, c = 1, 2, 3
# 1.常规
# if a>b:
#     c = a
# else:
#     c = b
#
# 2.表达式
# c = a if a>b else b
#
# 3.二维列表
# c = [b,a][a>b]
#
# 4.传说是源自某个黑客
# c = (a>b and [a] or [b])[0]
