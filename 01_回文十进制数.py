# -*- coding:utf-8 -*-

"""
求用十进制、二进制、八进制表示都是回文数的所有数字中，大于十进制数10的最小值
注：回文数类似于123454321
"""
import time

# 十进制的10以内没有对称性，因此该数大于等于10
# 由于是回文数，最低位必然不能为0 --> 二进制的末尾只能为1 --> 只考虑奇数（i+=2）
i = 11
while True:
    # 注意内置的转换函数bin(),oct(),hex()
    i_dec = str(i)
    i_bin = str(bin(i))
    i_oct = str(oct(i))

    # 测试
    # print(i_dec, i_dec[::-1])
    # print(i_oct[2:], i_oct[:1:-1])
    # print(i_bin[2:], i_bin[:1:-1])
    # time.sleep(1)

    # 注意切片不要写错
    if i_dec == i_dec[::-1] and i_bin[2:] == i_bin[:1:-1] and i_oct[2:] == i_oct[:1:-1]:
        print(i)
        break
    else:
        i += 2
