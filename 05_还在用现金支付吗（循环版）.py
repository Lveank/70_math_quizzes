# -*- coding:utf-8 -*-

"""
求兑换1000日元纸币时会出现多少种组合？
注：不计硬币兑出的先后顺序；只考虑10、50、100、500日元硬币的情况；最多只能兑出15枚硬币。
"""
count = 0
# a*10 + b*50 + c*100 + d*500 = 1000
# a+b+c+d <= 15
for a in range(16):  # 10最多15枚
    for b in range(16):  # 50最多15枚
        for c in range(11):  # 100最多10枚
            for d in range(3):  # 500最多2枚
                if (a * 10 + b * 50 + c * 100 + d * 500 == 1000) and (a + b + c + d <= 15):
                    print("%d个10￥, %d个50￥, %d个100￥, %d个500￥" % (a, b, c, d))
                    count += 1

print(count)
