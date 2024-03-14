# 思路：1.首先可以先对数组排序，可以更加方便逐步遍历
# 2.注意三个数字是一组，因此在定遍历范围的时候，注意范围选取，range(len(nums)-1,1,-1)就是这个目的

nums = list(map(int,input().split()))
nums.sort()
result = 0
for i in range(len(nums)-1,1,-1):
    a = nums[i]
    b = nums[i-1]
    c = nums[i-2]
    if a+b > c and b+c > a and a+c > b:
        result = a+b+c
        print(result)
        break
if result == 0:
    print(result)