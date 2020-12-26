# 序列中含有一些数据，我们需要提取出其中的值或根据某些标准对系列做删减

# 根据条件来筛选列表
mylist = [1, 4, -5, 10, -7, 2, 3, -1]

filter_list = [n for n in mylist if n > 0]
print("mylist is {}.\nfilter list is {}".format(mylist, filter_list))


pos = (n for n in mylist if n > 0)
print(pos)
for x in pos:
    print(x)

# 非数学类的比较，可以利用类的属性来比较
values = ['1', '2', '-3', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)

#  
addresses = [
        '5412 N clark',
        '5148 N clark',
        '5800 E 58TH',
        '2122 N clark',
        '5645 N ravenswood',
        '1060 W addison',
        '4801 N broadway',
        '1039 W granville',
        ]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress
more5 = [n>5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))
