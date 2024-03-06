def majority_element(n, arr):
    counts = {}  # 使用哈希表统计每个元素的出现次数

    for num in arr:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for num, count in counts.items():  # 遍历哈希表找到出现次数超过一半的元素
        if count > n / 2:
            return num


if __name__ == "__main__":
    n = int(input())  # 输入数组长度
    arr = list(map(int, input().split()))  # 输入数组元素
    # map()就是为了利用空格分割数组

    majority = majority_element(n, arr)  # 找到多数元素
    print( majority)  # 输出结果
