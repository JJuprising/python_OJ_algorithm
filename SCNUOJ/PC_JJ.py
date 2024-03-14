

def findtotoal(nums,left,right):
    if left==right-1:
        return nums[left]

    mid=(left+right)//2
    # 最左的最大
    lefttotoal=findtotoal(nums,left,mid)
    # 最右的最大
    righttotal=findtotoal(nums,mid,right)
    # 跨越的最大
    # 从中间到左边最大的
    leftmax=0
    maxleftbondersum=nums[mid-1] # 注意从mid-1一直到left-1 因为上面递归左边是从[left,mid-1]
    for i in range(mid-1,left-1,-1):
        leftmax+=nums[i]
        if leftmax>maxleftbondersum:
            maxleftbondersum=leftmax
    # 从中间到右边最大的
    rightmax=0
    maxrightbondersum =nums[mid]
    for i in range(mid,right):
        rightmax+=nums[i]
        if rightmax>maxrightbondersum:
            maxrightbondersum=rightmax

    return max(maxrightbondersum+maxleftbondersum,max(lefttotoal,righttotal))





if __name__ =="__main__":
    len=int(input())
    nums=list(map(int,input().split()))
    print(findtotoal(nums,0,len))
