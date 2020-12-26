# 从字典中提取子集
# 创建一个字典，其本身就是另一个字典的子集

prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.2,
        'FB': 10.75
        }

new_prices = {key:value for key, value in prices.items() if value > 200}
print(new_prices)

# 通过创建元组系列将它们传给dict()函数来完成
p1 = dict((key, value) for key, value in prices.items() if value > 200)
print(p1)
