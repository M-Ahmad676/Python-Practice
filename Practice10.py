class Calculator:
    def addition(self,num1,num2):
        return num1 + num2
    def subtraction(self,num1, num2):
        return num1-num2
    def multiplication(self,num1, num2):
        return num1*num2
    def division(self,num1,num2):

        if num2 == 0:
            return"Invalid Value cannot divide by 0"
        return num1/num2


def main():
    cal = Calculator()

    print("Select Option")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")

    choice = input("Enter Choice 1/2/3/4: ")

    choice = int(choice)

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == 1:
        print(f"{num1}+{num2} = {cal.addition(num1,num2)}")
    elif choice == 2:
        print(f"{num1} - {num2} = {cal.subtraction(num1,num2)}" )  
    elif choice == 3:
        print(f"{num1} * {num2} = {cal.multiplication(num1,num2)}" )  
    elif choice == 4:
        print(f"{num1} / {num2} = {cal.division(num1,num2)}" )  


main()