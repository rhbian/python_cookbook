# 将多个映射合并为单个映射

# 有多个字典或映射，想在逻辑上将它们合并为一个单独的映射结构，一次执行某些特定的操作，比如查找值或检查键是否存在

# 假设有两个字典
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 进行查找操作，必须检查这两个字典，先在a中查找，没有的话再在b中查找。
# 简单地方法事利用collections中的ChainMap类来解决

from collections import ChainMap

c = ChainMap(a,b)

print(c['x'])
print(c['y'])
print(c['z'])
print(list(c.values()))
print(list(c.keys()))
