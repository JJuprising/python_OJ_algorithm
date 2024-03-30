# 容器的宽可由索引判断
# 注意容器的高必须是两侧较小的那一个数
# 若按照常规思路，直接双重遍历会编译超时，所以采用贪婪算法，留下大的数，小的数则放弃

nums = list(map(int,input().split()))
# 设置索引和遍历范围
i = 0
j = len(nums)-1
max_water = 0

while (i<j):
    square = (j-i) * min(nums[i],nums[j])
    if square > max_water:
        max_water = square

    # 之所以用if-else是因为j-1和i+1是选一即可
    # 注意这里是比较nums中的数值nums[j]，不要比较成i和j了
    elif nums[j]<nums[i]:
        j -= 1
    else:
        i += 1

print(max_water)