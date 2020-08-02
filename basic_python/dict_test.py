dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print("返回指定键对应的值")
print(dict.get("Name"))

print("返回列表所有键/值，数据结构为列表")
print(dict.keys())
print(dict.values())

print("返回（键，值）元组列表")
print(dict.items())

print("删除指定键的字典元素")
print(dict.pop("Class"))
print(dict)

print("返回并删除字典中的最后一对键值")
print(dict.popitem())
print(dict)


print("将一个字典中的值更新到另一个字典中")
dict1 = {'Age': 7}
dict.update(dict1)
print(dict)


print("设置指定键的值")
dict.setdefault("Name", "Alice")
print(dict)

print("判断字典中是否含有某个键")
print("Name" in dict.keys())


print("创建字典")
dict4={}
dict4 = dict4.fromkeys(["age", "birth"], 10)
print(str(dict4))