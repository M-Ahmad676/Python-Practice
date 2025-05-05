def palindrome(word):
    lower_case = word.lower()
    reverse_word = lower_case[::-1]
    print(reverse_word)
    if lower_case == reverse_word:
        print("Is Palindrome")
    else:
        print("Is not Palindrome")

input_word = input("Enter a Word: ")
palindrome(input_word)