import copy

print("列表浅拷贝、深拷贝")
list1 = [1, 2, 3]
l1 = copy.copy(list1)
l2 = copy.deepcopy(list1)

list1.append(4)
print(list1)
print(l1)
print(l2)

print("字典浅拷贝、深拷贝")
dic1 = {"key1": "test1", "key2": "test2"}
d1 = copy.copy(dic1)
d2 = copy.deepcopy(dic1)
dic1.setdefault("key3", "test3")

print(dic1)
print(d1)
print(d2)

a = [1, 2, 3, [1,2]]
# b = a
# b = a.copy()
b = copy.copy(a)
# b = copy.deepcopy(a)
a[3].insert(1, 3)
print(a)
print(b)