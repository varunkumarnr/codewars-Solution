def count_bits(n):
    arr = []
    i = 0
    count=0
    while(n>0):
        arr.append(n%2)
        n = int(n/2)
        i+=1
    for j in range(len(arr)):
        if(arr[j]==1):
            count+=1
    return count
count_bits(1234)