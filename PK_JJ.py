

nums=list(map(int,input().split()))
nums.sort(reverse=True) # reverse=True 表示降序
tag=1
for i in range(len(nums)-2):
    a=nums[i]
    b=nums[i+1]
    c=nums[i+2]
    if a-b<c and b+c>a:# 两边只差小于第三边，两边之和大于第三边
        print(a+b+c)
        tag=0 # 表示找到了
        break
if tag:
    print(0)

