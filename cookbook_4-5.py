# 元组和列表

print("*"*15+" 列表 "+"*"*15) 
my_list = ["a", "a", "b", "c", "z"]

# 增加元素
my_list.append("d")

# 
my_list2 = ["e", "f"]
my_list3 = ["h"]

# 列表扩充
print(my_list.extend(my_list2))
print(my_list)

# 计数
print(my_list.count("a"))

l_index = my_list.index("a")
print(l_index)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

z = my_list.index("z")
print(z)
my_list.clear() # 删除列表中所有元素



print("*"*15+" 元组 "+"*"*15)
