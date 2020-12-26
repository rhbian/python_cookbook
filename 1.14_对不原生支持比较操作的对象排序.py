# 对不原生支持比较操作的对象排序
from operator import attrgetter

# 在同一个类的实例之间做排序，但是并不原生支持比较操作。

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

users = [User(2), User(3), User(99), User(4)]
print(users)

# 使用lambda表达式
print(sorted(users, key=lambda u: u.user_id))
# 使用attrgetter()函数
print(sorted(users, key=attrgetter('user_id')))

# 查看最大值和最小值
# 提取的是list中的某一个元素
print(min(users, key=attrgetter('user_id')))
print(max(users, key=attrgetter('user_id')))
