def triangles():
    list1 = [[1]]
    list2 = [1]
    for i in range(10):
        # list3用于存储上个数组中每个数之和
        list3 = [1]
        for j in range(len(list1[i])-1):
            list3.append(list2[j]+list2[j+1])
        list3.append(1)
        list1.append(list3)
        list2 = list3
        yield list1[i]


if __name__ == '__main__':
    n = 0
    results = []
    for t in triangles():
        results.append(t)
        n = n + 1
        if n == 10:
            break

    for t in results:
        print(t)

    if results == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]:
        print('测试通过!')
    else:
        print('测试失败!') 
