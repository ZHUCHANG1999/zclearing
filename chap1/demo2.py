# 开发时间：2021/8/19 16:03

# 转义字符
print('hello\nworld')
print('hello\tworld')
print('hello\rworld')  # world将hello覆盖
print('hello\bworld')  # \b是退一个格，将o退没了

print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r，或者R
print('hello\nworld')
# 注意最后一个字符不能是一个单个的反斜杠
print(R'hello\nworld')
