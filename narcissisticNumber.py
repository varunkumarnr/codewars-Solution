def narcissistic(value):
    sum = 0
    digits = [int(x) for x in str(value)]
    for i in range(len(digits)):
        sum += pow(digits[i], len(digits))
    if value == sum:
        print("true")
        return True
    else:
        print("not")
        return False


narcissistic(122)