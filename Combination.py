# 回溯法
def combination(n,k):
    result = []
    path = []
    def backtrace(n,k,startNum):
        if len(path) == k:
            result.append(path[:]) # 切片
            return
        for i in range(startNum,n+1):
            path.append(i)
            backtrace(n,k,i+1)
            path.pop()
    backtrace(n,k,1)
    return result

n,k=list(map(int,input().split()))
print(combination(n,k))