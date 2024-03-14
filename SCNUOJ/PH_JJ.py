"""
柠檬水找零
先收5块统计，然后给所有10块找5，获取10块
给20找10和5
"""

if __name__=="__main__":
    nums=list(map(int,input().split()))
    myfive=0
    myten=0
    five=0
    ten=0
    tewn=0
    for num in nums:
        if num == 5:
            five+=1
        if num == 10:
            ten+=1
        if num == 20:
            tewn+=1
    myfive=five
    # 给10 找零
    while myfive>0 and ten>0:
        myfive-=1
        ten-=1
        myten+=1
    if ten>0 or myfive<0:
        #10没找完 结束
        print("false")
    elif tewn>0:# 还要满足20的情况
        # 找20 需要1张5 1张10 或者 3张5
        while tewn>0:
            # 1张5 1张10
            if myten>0:
                myfive-=1
                myten-=1
                tewn-=1
            else:
                myfive-=3
                tewn-=1
        if tewn>0 or myfive<0:
            print("false")
            # print(myfive,myten)
        else:
            print("true")
    else:
        print("true")