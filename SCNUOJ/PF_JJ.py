"""
k个最长重复字符串 分治
没理解题意
找出

s 中的最长子串，且该字符串的每一个字符出现次数都不少于 k！！
好好审题

所以先统计出现的字符数，小于 k 的字符进行分割(这些小于k的必定不纳入子串中了)
所以要不就在左边，要不就在右边

注意split函数，如果是"aaabb".split(b)，那结果就是 'aaa' (b) '' (b) ''，后两个空串

"""


def findrepeat(str, n):
    if len(str) < n:
        return 0
    for char in set(str):  # 出现 字符的集合
        # 统计次数
        if str.count(char) < n:
            # 递归
            return max(findrepeat(substring, n) for substring in str.split(char))

    # 注意要返回长度!!
    print(111111)
    print(f"返回len(str){len(str)}")
    return len(str)


if __name__ == "__main__":
    input_str = input()
    split_data = input_str.split()
    str = split_data[0]
    n = int(split_data[1])
    print(f"{findrepeat(str, n)}")
