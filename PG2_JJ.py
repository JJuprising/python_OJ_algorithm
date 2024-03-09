if __name__=="__main__":
    # 读取构造链表
    nums = list(map(int,input().split()))
    nums.sort()
    for num in nums:
        print(num,end=' ')