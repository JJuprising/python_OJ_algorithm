# 最大K个数

'''
sort or 手写快速排序（练思路
'''


def part(nums, left, right):
    # 对比值
    pviot = nums[left]
    i = left
    j = right
    while i < j:
        while nums[j] < pviot and i < j:  # i<j
            j -= 1
        if i < j:
            # 交换两者
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            # 注意这里
            i += 1
        while nums[i] > pviot and i < j:  # i<j
            i += 1
        if i < j:
            # 交换两者
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            # 注意这里
            j-=1
    return i


def Quicksort(nums, left, right):
    if left < right:
        mid = part(nums, left, right)
        # 注意递归方法
        Quicksort(nums, left, mid-1)
        Quicksort(nums, mid+1, right)


if __name__ == "__main__":
    n, k = map(int, input().split())  # 注意这个输入是按行的，分割
    nums = list(map(int, input().split()))

    Quicksort(nums, 0, n-1)

    print(nums[k-1], end=' ')

