def checkPalindrome(string):
    lowercase = string.lower()
    reverse_string = lowercase[:: -1]
    if(lowercase == reverse_string):
        print("Is Palindrome")
    else:
        print("Is not Palindrome")

inputString = "RaceCar"
checkPalindrome(inputString)

# Palindrome Checker



