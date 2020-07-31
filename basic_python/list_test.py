# 定义列表
list1 = [1, 2, 3]
list2 = [7, 8, 9]
# 练习列表操作
list3 = list1 + list2
print(list3)
list4 = list1*2
print(list4)
list5 = list3[1:4]  # 前闭后开
print(list5)

# star, end, step； start=-1表示从最后开始，step为负，表示从后向前
list6 = list3[-1:0:-2]
print(list6)
print(list2)

# 切片默认从左向右取，如果想从最后一位取，需要加上负的步长
list7 = list2[-1:0:-1]
print(list7)

# ***************练习列表常用方法****************
# 列表当作堆栈使用
stack = [1,2,3]
stack.append(4)
print(stack)
s1 = stack.pop()
print(s1)
print(stack)

# 在指定位置2出入元素
stack.insert(2, 5)
print(stack)

# 移除对应值的元素
stack.remove(5)

# 返回值对应的index
print(stack.index(3))

# 返回元素在列表中出现的个数
print(list4.count(1))

print("返回列表长度")
print(len(stack))

print("返回列表最大值")
print(max(stack))

print("返回列表最小值")
print(min(stack))
# 将一个列表与另一个拼接
list1.extend(list2)
print(list1)

print("对列表排序")
list1.sort(reverse=True)
print(list1)

print("反向列表中元素")
list1.reverse()
print(list1)

print("复制序列")
list_copy = list1.copy()
print(list_copy)

list1[0] = 77
print(list1)
print(list_copy)

print("清除列表")
list1.clear()
print(list1)
