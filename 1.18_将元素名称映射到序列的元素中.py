# 访问元组或者列表中的元素通常是通过元素的位置来进行。
# 希望能通过名称来访问元素。

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('Honesy@example.com', '2012-10-19')
print(sub)
print(type(sub))

print(sub.addr)
print(sub.joined)

# namedtuple创建了一个元组子类的实例，该实例与普通的元组可互换
print(len(sub))

# 支持索引和分解
ad, jo = sub
print(ad)
print(jo)

# 大型的元组列表，通过元素的位置来访问数据。如果表单中新增了一列数据，那么代码会崩溃。如果首先将返回的元组转型为命名元组，就不会出现问题。

# 普通的元组
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total

# 使用命名元组
from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total
