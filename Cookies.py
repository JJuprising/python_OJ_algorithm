# 主要思想：一一匹配，注意重要突破点实现排序！！
def Cookies_Divide(g,s):
    result_count = 0
    # 注意先排序会使整个查找更简单
    g.sort()
    s.sort()

    i,j = 0,0 # 索引
    while i < len(g) and j < len(s):
        if g[i] <= s[j]:
            result_count += 1
            i += 1
            j += 1
        else:
            j += 1
    return result_count


# 注意这个函数要放在创建的函数下面
if __name__ == "__main__":
    g = list(map(int,input().split()))
    s = list(map(int,input().split()))
    result = Cookies_Divide(g,s)
    print(result)
