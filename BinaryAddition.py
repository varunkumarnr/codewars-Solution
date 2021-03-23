def add_binary(a, b):
    sum = a + b
    n = " "
    while sum > 0:
        n = str(sum % 2) + n
        sum = int(sum / 2)
    print(int(n))
    return int(n)


add_binary(3, 4)
