def queue(n):
    #if n > 15:
        #print("error")

    result = []
    # 用path来保存当前已经选择的数字
    def backtrace(path):
        if len(path) == n:
            result.append(path[:])
            return

        for i in range(1, n + 1):
            if i not in path:
                path.append(i)
                backtrace(path)
                path.pop()
    backtrace([])
    return result

n = int(input())
res=queue(n)
right = 0
count = 0
for i in res:
    for j in range(n):
        if int(i[j]) % (j+1) == 0 and (j+1) % int(i[j]) == 0:
            count +=1
    if count == n:
        right +=1

print(right)