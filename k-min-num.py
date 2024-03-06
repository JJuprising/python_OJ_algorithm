def find_min_k(array,k):
    array.sort()
    return array[0:k]

if __name__=="__main__":
    length,k=map(int,input().split(" "))
    array=list(map(int,input().split(" ")))

    min_k=find_min_k(array,k)
    print(*min_k)