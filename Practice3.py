vowels = "aeiouAEIOU"
count = 0
inputString = "Cornelleous"

for char in inputString:
    if char in vowels:
        count += 1

print(count)  # ✅ Now this works
