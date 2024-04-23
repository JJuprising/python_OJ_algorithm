
"""
种花问题 蛮力法 本题要注意考虑特殊情况
"""

def plantint(flower,n):
    lenth = len(flowers)
    # 注意虽然说“相邻”，但是首尾要特殊对待
    if lenth<n:
        return "false"
    # 有头种头，有尾种尾
    if flowers[0] == 0 and flowers[1] == 0:
        n -= 1
    if flowers[lenth - 2] == 0 and flowers[lenth - 1] == 0:
        n -= 1
    # print(n)
    # 中间的一般情况

    for i in range(1, lenth - 1):
        if flowers[i - 1] ==0 and flowers[i + 1] == 0 and flowers[i]==0:
            n -= 1
            flowers[i] = 1  # 种上

    # print(flowers)
    if n<=0:
        return "true"
    else:
        return "false"

if __name__=="__main__":
    flowers=list(map(int,input().split()))
    n=int(input())

    print(plantint(flowers,n))





