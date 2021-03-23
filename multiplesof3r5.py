def solution(number):
    arr = []
    sum = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            arr.append(i)
    for i in range(len(arr)):
        sum += arr[i]
    print(sum)
    return sum


solution(10)