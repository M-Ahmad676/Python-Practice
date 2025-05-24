def countElements(array):
   sum = 0
   for elements in array:
     sum = sum + 1
   print(f"there are {sum} elements in this List")


response = int(input("enter the number elements you want to enter:"))
array = []
count = 0
while response > 0:
    value = int(input("enter value:"))
    array.append(value)
    response = response - 1

countElements(array)