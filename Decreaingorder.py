# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num):
    digits = [int(x) for x in str(num)]
    digits.sort(reverse=True )
    s = [str(i) for i in digits] 
    res = int("".join(s)) 
    return res
    
    

descending_order(54782)