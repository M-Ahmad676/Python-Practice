def reverse(sentence):
    rev = ""
    for word in sentence.split(" "):
        rev = word + " " + rev
    return rev

def shortReverse(sentence):
    return " ".join(sentence.split(" ")[::-1])

sentence = "I love race cars"
print(reverse(sentence))
print(shortReverse(sentence))