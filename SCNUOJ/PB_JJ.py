# 寻找多数
'''
分治法，分左右，统计，不一致再比较
'''

class MaxNum():
    def __init__(self,nums,len):
        self.nums=nums
        self.len=len-1
        self.maxnum=self.findMax(0,self.len)
    def findMax(self,left, right):
        # 规模为1 直接返回
        if left == right:
            return nums[left]

        # 找左右多数
        mid = (left + right) // 2
        leftMax = self.findMax(left, mid)
        rightMax = self.findMax(mid + 1, right)
        if leftMax == rightMax:
            return leftMax
        # 不同，统计在整个区间数量进行比较 注意是整个！ range左开右闭，right+1
        leftcount = sum(1 for i in range(left, right+1) if nums[i] == leftMax)
        rightcount = sum(1 for i in range(left, right+1) if nums[i] == rightMax)
        return leftMax if leftcount > rightcount else rightMax


if __name__ == "__main__":
    Len = int(input())
    nums = list(map(int, input().split()))
    # print(Len,nums)
    print(MaxNum(nums,Len).maxnum)
