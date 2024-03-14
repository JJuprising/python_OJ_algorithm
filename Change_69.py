# 这里就是字符串读取，注意不需要把字符串变成列表再看索引这么复杂，直接字符串就有索引。
# 还有一个点，正常一开始就会想直接找到最大位数上的6换成9，但是注意str[i]是不可以用常量赋值的，所以只能切割组合法。
num = input()

def Change_69(num):
    # range不要忘了
    for i in range(len(num)):
        # 注意若不加单引号，这个6和9就是int型，但是我们要的是字符串类型。
        if num[i] == '6':
            num = num[:i] + '9' + num[i+1:]
            break
    return num

result = Change_69(num)
print(result)