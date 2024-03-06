length,k=map(int,input().split(" "))
array=list(map(int,input().split(" ")))
array=array.sorted()
print(array[length-k])