def LemonadeChange(Bills):
    five = 0
    ten = 0
    for bill in Bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five>0:
                five -= 1
                ten += 1
            else:
                return "false"
                count += 1
        elif bill == 20:
            if five>0 and ten>0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return "false"

    return "true"
# 如果前面没有返回false就会返回这个true。


if __name__ == "__main__":
    Bills = list(map(int, input().split()))
    result=LemonadeChange(Bills)
    print(result)