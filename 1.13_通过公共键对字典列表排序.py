#　通过公共键对字典列表排序
from operator import itemgetter

# data 
# a list of dict

rows = [
        {'fname': 'Brain', 'lname': 'Jones',   'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John',  'lname': 'Cleese',  'uid': 1001},
        {'fname': 'Big',   'lname': 'Jones',   'uid': 1004},
        ]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
# for i in itemgetter('fname'):
#     print(type(i))

rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)

# 
min_value = min(rows, key=itemgetter('uid'))
print(min_value)
max_value = max(rows, key=itemgetter('uid'))
print(max_value)
