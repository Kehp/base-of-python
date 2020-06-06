# -*- coding: utf-8 -*-
from functools import reduce

def is_palindrome(n):
    list1 = []
    l = n
    def add(x, y):
        return x*10+y
    for i in range(len(str(l))):
        list1.append(l%10)
        l //= 10
    m = reduce(add, list1)
    return m == n
 
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
