# 利用shell通配符做字符串匹配

from fnmatch import fnmatch, fnmatchcase

fn = fnmatch('foo.txt', '*.txt')
print(fn)


names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
dat_file = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(dat_file)
# 不区分大小写的话用fnmatch()
# 区分大小写的话用fnmatchcase()
