# -*- coding:utf-8 -*-

"""
求兑换1000日元纸币时会出现多少种组合？
注：不计硬币兑出的先后顺序；只考虑10、50、100、500日元硬币的情况；最多只能兑出15枚硬币。
"""

count = 0


def change(target, coins, usable):
    """
    target：目标钱数
    coins：可找面值，列表
    usable：总硬币数
    """
    global count
    if len(coins) != 0:
        coin = coins.pop(0)  # list.pop([index = -1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
        if int(target / coin) <= usable:
            count += 1
        else:
            for i in range(0, int(target / coin)):
                change(target - coin * i, coins, usable - 1)


change(1000, [10, 50, 100, 500], 15)
print(count)
