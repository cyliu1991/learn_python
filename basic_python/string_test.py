print("创建字符串")
var1 = 'Hello World!'
var2 = "Python Runoob"

print("字符串重负输出")
print(var1*2)

print("判断字符串中是否包含给定的字符")
print('He' in var1)
print('He' not in var1)

print("字符串格式化")
print("I want to say %s" % var1)


print("字符串的提一个字母大写")
str3 = 'hello world!'
print(str3.capitalize())

print(str3.center(50))


print("某个字符在字符串中出现的次数")
print(str3.count('l'))


print("判断字符串是否以某个字符结束")
print(str3.endswith('!'))


print("检查字符串是否包含在指定范围")
print(str3.find('ll'))

print("判断字符是否都为数字或字母")
print(str3.isalnum())
print("123abc".isalnum())

print("判断字符是否都为字母")
print(str3.isalpha())
print("abc".isalpha())

print("判断字符串是否仅包含10进制数字")
print("0x12".isdecimal())
print("12".isdecimal())


print("判断字符串中是否仅包含数字")
print("123a".isdigit())
print("123".isdigit())

print("判断字符串是否为小写\大写字母")
print("abc".islower())
print("123".islower())
print("A".islower())
print("A".isupper())


print("判断字符串中是否只有空格")
print("".isspace())
print(" ".isspace())


print("字符串中的小写字母转换为大写")
print("abc".upper())
print("ABC".lower())


print("以标题形式返回字符串，所有单词首字母大写，其余小写")
print(str3.title())


print("将字符串中的大小写反转")
str4 = str3.title()
print(str4.swapcase())


print("将字符串切片")
print(str3.split(" "))