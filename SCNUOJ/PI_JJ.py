"""
找最小的饼干满足需求最少的

"""

if __name__=="__main__":
    childs=list(map(int,input().split()))
    cakes=list(map(int,input().split()))
    # print(cakes,childs)
    childs.sort()
    cakes.sort()
    count=0
    tar=-1
    C_Len=len(childs)
    for cake in cakes:
        for i in (tar+1,C_Len):
            if i >=C_Len:

                break
            elif cake>=childs[i]:
                count+=1
                tar=i # 标记下一次投喂的孩子位置
                break
    print(count)
