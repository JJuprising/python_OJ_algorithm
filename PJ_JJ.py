"""
 6和9组成的最大数字翻转一个数，找最高权重的就好
"""

# 要用字符串读取
str=input()
for i in range(len(str)):
    if str[i] == '6':
        str=str[:i] + '9' + str[i+1:] # 注意这里不能str[i]='9'常量赋值不允许
        break
print(str)