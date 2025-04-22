def findEven(list):
    evenList = []
    for x in list:
        if x % 2 == 0:
            print("is Even", x)
            evenList.append(x)
        else:
            print("is Odd", x)
    
    return evenList

list = [1,3,4,7,8,10]

print("List of Even Numbers:",findEven(list))