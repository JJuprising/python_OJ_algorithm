
def canPlaceFlower(flower,num):
    count = 0
    length = len(flower)

    # 注意在表头和表尾插入一个0，以便后续遍历初始位和末位。
    flower.append(0)
    flower.insert(0,0)
    for i in range(1,length+1):
        # 注意遍历第一个数和最后一个数的情况，此时该数是没有前一个数或者后一个数的
        # 当该数的前一个数和后一个数均为0时就说明可以种一朵花
        if flower[i+1]+flower[i-1]==0 and flower[i]==0:
            count += 1
            flower[i]=1



    if count >=num:
        return "true"
    else:
        return "false"
flower=list(map(int,input().split()))
num=int(input())
result = canPlaceFlower(flower,num)
print(result)
