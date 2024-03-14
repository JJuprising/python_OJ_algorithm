

if __name__=="__main__":
    nums=list(map(int,input().split()))

    maxS=0
    i=0
    lenth=len(nums)
    # 遍历所有情况
    j=lenth-1
    """
    这里如果直接双重循环遍历所有情况会超时
    进行贪心，留下大的，小的退格
    
    """

    while(i<j):
        s=(j-i)*min(nums[i],nums[j])
        if s>maxS:
            maxS=s
        if nums[i]>nums[j]:
            j-=1
        else:
            i+=1

    print(maxS)