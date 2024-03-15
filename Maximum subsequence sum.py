# 子序列的起始位置可能是任意的，结束位置也可以是任意的。
# 可以一层循环确定子序列的起始位置，嵌套一层循环确定子序列的结束位置并求和。
# 穷举法
def getMaxSubString(arr,len):
    sum_list = []
    for i in range(len):
        cur_sum = 0
        for j in range(i, len):
            cur_sum += arr[j]
            sum_list.append(cur_sum)
    max_element = max(sum_list)
    return max_element

if __name__ == '__main__':
    len = int(input())
    arr = list(map(int,input().split()))
    result = getMaxSubString(arr,len)
    print(result)