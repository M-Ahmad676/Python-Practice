def factorial(num):
    
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
       return num * factorial(num-1)
    
def factorial_iteratively(n):
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       result = 1
       for x in range(1, n + 1):
           result*=x
    return result 


number = int(input("Enter any number: "))
print(factorial(number))
print(factorial_iteratively(number))