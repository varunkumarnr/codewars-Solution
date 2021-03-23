def is_prime(num):
    while num > 1:
        for i in range(2, int(num / 2) + 1):
            # for(i=2;i<=(num/2)+1;i++)
            if (num % i) == 0:
                print("not prime")
                return False
                break
        else:
            print("prime")
            return True
    return False


is_prime(5)