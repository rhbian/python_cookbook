# 根据字段将记录分组
# 有一系列的字典或对象实例，想根据某个特定的字段(比如说日期)来分组迭代数据。

from operator import itemgetter
from itertools import groupby

rows = [
        {'address': '5412 N clark', 'date': '07/01/2012'},
        {'address': '5418 N clark', 'date': '07/04/2012'},
        {'address': '5800 E 58th',  'date': '07/02/2012'},
        {'address': '2122 N clark', 'date': '07/03/2012'},
        {'address': '5645 N ravenswood', 'date': '07/02/2012'},
        {'address': '1060 W addison', 'date': '07/02/2012'},
        {'address': '4801 N broadway', 'date': '07/01/2012'},
        {'address': '1039 W granville', 'date': '07/04/2012'},
        ]
# print(rows)



# 先排序，再分组。会得到想要的效果
rows.sort(key=itemgetter('date'))

# 使用groupby
# for i in groupby(rows, key=itemgetter('date')):
#     print(i)

for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)


from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
