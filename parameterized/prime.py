def isPrime(number) -> bool:
    if number <0: raise ArithmeticError('No Negative Number')
    if number <2: return False

    i=2
    while(i*i<number):
        if number % i==0: return False
        i+=1
    return True
    
    