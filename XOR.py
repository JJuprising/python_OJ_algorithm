'''def XOR(nums):
    if not nums:
        return 0
    result = [nums[0]]
    for i in result[1:]:
        result += [k ^ i for k in result] + [i]
        # 每增加一个元素，它的子集就相当于加上新元素和新元素与原来子集的结合
        print(result)
    return sum(result)

nums = [1,3]
print(XOR(nums))'''

def XOR(nums):
    if not nums:
        return 0

    result = [0]  # 初始值为0，表示空子集的异或总和为0

    for i in nums:
        # 相当于每加入一个新元素，就与现有的所有异或值再进行异或运算
        result += [i ^ res for res in result]  # 将新元素与原来子集的每个值异或，并加入结果集
        # 每增加一个元素，它的子集就相当于加上新元素和新元素与原来子集的结合
        print(result)

    return sum(result)


Input = input()
nums = list(map(int, Input.split()))  # 将输入的字符串按空格分割，并转换为整数列表
print(XOR(nums))

