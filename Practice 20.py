def find_Second_Largest(list):
    first = second = float('-inf')
    for x in list:
        if x > first:
            second = first
            first = x
        elif second < x < first:
            second = x
    return second

inputList = [10,4,5,6,7,9,3,11]
print(find_Second_Largest(inputList))
