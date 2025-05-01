def fibonnaci(n):
    a,b = 0,1
    while b < n:
        a,b = b, a+b
    return b == n or n == 0

number = int(input("Enter a Number to check if its included in the Series :"))
if fibonnaci(number):
    print(f"{number} is a Fibonnaci Number")
else:
    print(f"{number} is not a Fibonnaci Number")
