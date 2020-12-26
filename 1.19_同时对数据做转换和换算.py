# 同时对数据做转换和换算
nums = [1, 2, 3, 4, 5]
s = sum(x*x for x in nums)
print(s)

# Determine if any .py files exist in a direcctory

import os
files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print("There be python")
else:
    print("sorry, no python")


# output a tuple as csv
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# 根据数据结构的域进行数据转换
portfolio = [
        {'name': "GOOG", 'shares': 50},
        {'name': "YHOO", 'shares': 75},
        {'name': 'AOL',  'shares': 20},
        {'name': 'SCOX', 'shares': 65}
        ]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
