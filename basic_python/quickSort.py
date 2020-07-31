def quick_sort(a, start, end):

    # 给定退出条件
    if start >= end:
        return

    # 指定标志位和检索起始位
    flag = a[start]
    low = start
    high = end

    # 根据选定标志位排序，大于标志位的移到标志位右边，小于标志位的移到标志位左边
    while low < high:
        while (low < high) & (a[high] >= flag):
            high = high-1
        a[low] = a[high]
        while (low < high) & (a[low] <= flag):
            low = low+1
        a[high] = a[low]

#     完成第一轮排序，对新数组进行分段，并递归调用
    mid = low
    a[mid] = flag
    quick_sort(a, 0, mid-1)
    quick_sort(a, mid+1, end)

    # 返回完成的数组
    return a


if __name__ == '__main__':
    a = [6, 1, 2, 7, 9, 3, 5, 4, 10, 8]
    a1 = quick_sort(a, 0, len(a)-1)
    print(a1)