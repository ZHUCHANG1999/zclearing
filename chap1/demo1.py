# 开发时间：2021/8/18 11:24

# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('hollowed')

# 含有运算符的表达式
print(3 + 1)

# 将数据输出文件
fp = open('G:/text.txt', 'a+')  # a+如果文件不存在就创建，存在就在文件内容的后面继续追加
print('hollowed', file=fp)
fp.close()

# 不进行换行输出（输出内容在一行当中）
print('hello', 'world', 'python')
