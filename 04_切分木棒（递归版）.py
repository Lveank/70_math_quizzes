# -*- coding:utf-8 -*-

"""
假设要把长度为n厘米的木棒切分为1厘米长的小段，但是1根木棒只能由1人切分，
当木棒被切分为3段后，可以同时由3个人分别切分木棒。 求最多有m个人时，最少要切分几次。
Q1：当n=20，m=3时的最少切分次数
Q2：当n=100，m=5时的最少切分次数
"""


def cutbar(n, m, current):  # current = 现在的节数
    # 为了避免调用层次过深，每个递归函数都会设置一个终止条件
    # 如果现在的节数 >= 目标节数，则判断终止（不需要再进行切割）
    if current >= n:
        return 0
    else:
        # 如果现在的节数 < 分切人数，那么下一次执行时的节数就是现在的2倍
        # 分切次数+1并返回
        if current < m:
            return 1 + cutbar(n, m, 2 * current)
        # 如果现在的节数 >= 分切人数，那么下一次执行的节数仅+m
        # 分切次数+1并返回
        else:
            return 1 + cutbar(n, m, current + m)


# 以下仅是为了说明递归终止条件的意义。这里没有设定终止条件，也可以得到相同的结果。
def bad_cutbar(n, m, current):
    if current < m:
        return 1 + cutbar(n, m, 2 * current)
    else:
        return 1 + cutbar(n, m, current + m)


if __name__ == '__main__':
    print(cutbar(20, 3, 1))  # 8
    print(cutbar(100, 5, 1))  # 22
    print(cutbar(16, 7, 1))

    # print(bad_cutbar(20, 3, 1))  # 8
    # print(bad_cutbar(100, 5, 1))  # 22
