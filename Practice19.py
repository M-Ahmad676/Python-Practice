def find_vowels(word):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count +=1
        else:
            print(f"is a consonant: {letter}")
            consonant_count +=1

    return vowel_count, consonant_count

word = "sigma"
vowels , consonants = find_vowels(word)
print("Vowels:",vowels)
print("consonants:", consonants)
