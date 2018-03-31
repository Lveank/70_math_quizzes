# -*- coding:utf-8 -*-

"""
在四位数中间插入运算符，使得计算结果为：
“将原数字各个位数上的数逆序排列后得到的数”
351 --> 3 * 51 = 513
求位于1000到9999中满足上述条件的数
"""

# 【重点！】使用逆波兰表示法，方便遍历【关键是要想到运算符号也是可遍历的】
# 【注意！】使用*意外的任何符号，最后结果都不能凑够四位数。
# 缩减符号，减少判断，还能绕开除数为0的bug
op = ["*", ""]

# 循环，四位数字，最多插三个运算符
for i in range(1000, 10000):
    for j in range(len(op)):
        for k in range(len(op)):
            for l in range(len(op)):
                # 先逆序排列，再插入运算符号
                val = str(i)[3] + op[j] + str(i)[2] + op[k] + str(i)[1] + op[l] + str(i)[0]
                # 一定要插入1个运算符
                if len(val) > 4:
                    # 需要对0进行特殊处理，否则会被认为是Python2中的八进制数字（虽然在Python3中已改为0o标记）
                    # 由于0开头的数逆序肯定不符合条件，所以可以用异常处理跳过
                    try:
                        if i == eval(val):
                            print(val + " = " + str(i))
                    except Exception as e:
                        pass
