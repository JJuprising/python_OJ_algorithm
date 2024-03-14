def Findk(str,k):
    if len(str) < k :
        return 0

    # 判断每个字符的个数是否满足k，不满足的话，就以它为分界线来切分字符串，然后对切分的字符串进行递归处理。
    for charactor in set(str):
        if str.count(charactor) < k:
            return max(Findk(sub,k) for sub in str.split(charactor))

    return len(str)

if __name__ == '__main__':
    input_str = input()
    split_data = input_str.split()
    str = split_data[0]
    k = int(split_data[1])
    print(Findk(str,k))