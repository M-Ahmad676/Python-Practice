
def print_even(number):
    for x in range(1, number+1):
        if(x % 2 == 0):
            print("are even:", x)
        else:
            pass

response = int(input("enter a number greater then 20"))
print_even(response)

if response > 20:
    print("Condition True")
else:
    print("condition false")