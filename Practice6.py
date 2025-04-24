def Maximum(List):
    number = 0
    for x in List:
        if x > number:
            number = x
    return number

myList = [1,22,9,8,34,90,3]
print(Maximum(myList))

# Find Max in a List