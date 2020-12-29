# 更复杂的匹配，需要用到re模块

text = "yeah, but no, but yeah, but no, but yeah"

print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('but'))


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
find_date = datepat.findall(text)
print(find_date)

# 当定义正则表达式时，我们常会将部分模式用括号抱起来的方式引入捕获组。
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/12/2012')
# m = datepat.match(text)
print(m)
print(m.group(0))
print(m.group(1))
print(m.group())

