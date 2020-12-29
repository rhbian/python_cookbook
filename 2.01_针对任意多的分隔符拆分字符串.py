# 针对任意多的分隔符拆分字符串
line = 'asdf fjdk; afde, fjk,asf,  foo'
import re
new_line = re.split(r'[;,\s]\s*', line) # \s 空白符
print(new_line)
nline = "".join(new_line)
print(nline)
