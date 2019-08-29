# Sum of primes number in range of N.

def sumprimes(n):
    sum = 0
    for i in range(0,len(n)):
        num = n[i]
        if num > 1:
            if (num%j != 0 for j in range(2, int(num**0.5)+1)):
                sum = sum + num
        else:
                sum = 0
    return(sum)
