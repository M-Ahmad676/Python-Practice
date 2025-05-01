contacts = {
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com"},
    "Bob": {"phone": "987-654-3210", "email": "bob@example.com"}
}

def add_contacts(name, phone, email):
    contacts[name] = {"phone": phone, "email":email}
    print(contacts)

def search_contacts(name):
    if name in contacts:
        print(f"Name: {name}, phone:{contacts[name]['phone']}, email:{contacts[name]['email']}")
    else:
        print("contact Not Found !")

print('Select Options')
print('1) Add Contact')
print('2) Search Contact')
choice = int(input("Enter 1 or 2 to select option:" ))

if choice == 1:
   name = input("Enter Name of Contact: ")
   number = input("Enter Phone Number: ")
   email = input("Enter Email Address: ")
   add_contacts(name,number,email)
else:
      name = input("Enter Name of Contact: ")
      search_contacts(name)
