# 在字符串的开头或结尾处做文本匹配

filename = "spam.txt"
txt_file = filename.endswith(".txt")
print(txt_file)

txt_file = filename.startswith('file:')
print(txt_file)

import os

filenames = os.listdir('.')
print(filenames)

from urllib.request import urlopen

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

py_file = [name for name in filenames if name.endswith('.py')]
print(py_file)
