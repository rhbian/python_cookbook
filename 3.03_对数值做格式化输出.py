# 对数据做格式化输出

x = 19723.456344
print(format(x, '0.2f'))
# 右对齐。长度为20
print(format(x, '>20.1f'))
print(format(x, '<20.1f'))
print(format(x, '^20.1f'))
print(format(x, '^20,.1f'))
