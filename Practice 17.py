def min_max(List):
    minimum = List[0]
    maximum = List[0]
    for x in List:
        if x > maximum:
            maximum = x
        elif minimum > x:
            minimum = x
    return maximum, minimum

def builtIn(List):
    min_val = min(List)
    max_val = max(List)

    return min_val, max_val

List = [4,7,1,5,9,3]
print(min_max(List))
print(builtIn(List))
