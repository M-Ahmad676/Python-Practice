def factorial(number):
    result = 1
    for x in range(1, number + 1):
        result *= x
    return result


inputNumber = 200
print(factorial(inputNumber))