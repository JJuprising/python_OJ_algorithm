def remove_k_digits(num, k):
    stack = []

    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # 处理剩余的 k
    while k > 0:
        stack.pop()
        k -= 1

    # 构建结果字符串
    result = "".join(stack).lstrip("0")
    if not result:
        return "0"
    return result

# 读取输入
input_str = input().split()
num = input_str[0]
k = int(input_str[1])

# 调用函数并输出结果
result = remove_k_digits(num, k)
print(result)