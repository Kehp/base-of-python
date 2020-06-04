from functools import reduce


def str2float(s):
    a = s.split('.')
    l = len(a[1])

    def fl(x, y):
        return x+y/pow(10, l)
    return reduce(fl, list(map(int, a)))


if __name__ == '__main__':
    print('str2float(\'5987.3697\') =', str2float('5987.3697'))
    if abs(str2float('5987.3697') - 5987.3697) < 0.00001:
        print('测试成功!')
    else:
        print('测试失败!')
