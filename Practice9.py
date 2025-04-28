def unique_Elements(List):
    unique_List = []
    for x in List:
        if x not in unique_List:
            unique_List.append(x)

    return unique_List

inputList = [1,3,4,5,6,2,3,1,4,5,9,5,5,6,7]
print(unique_Elements(inputList))