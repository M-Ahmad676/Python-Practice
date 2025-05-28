age = int(input("enter your age:"))
student_status = input("are you a student:")

if age >= 60 and student_status == "yes":
    print(f"you will get 30 % discount")
elif age >= 60 and student_status == "no":
    print(f"you will get 20 % discount")
elif age < 60 and student_status == "yes":
    print(f"you will get 10 % discount")
else:
    print("no discount")