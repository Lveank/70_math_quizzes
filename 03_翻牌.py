# -*- coding:utf-8 -*-

"""
从第n张牌开始，每隔n-1张牌翻牌
当所有牌不再变动时，正面向上的牌的数字
注意：翻过的牌会翻回来
"""

# 初始化卡牌表（注意这个列表生成式的写法）
cardlist = [0 for i in range(1, 101)]

for j in range(2, 101):
    k = j - 1
    while k < len(cardlist):
        # python取反操作【~】
        cardlist[k] = ~cardlist[k]
        # 注意：步长是j
        k += j

for item in range(len(cardlist)):
    if cardlist[item] == 0:
        print(item+1, end=" ")
