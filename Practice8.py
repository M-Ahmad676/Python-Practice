file = open ('DemoFile.txt', 'r')

content = file.read()

character_count = len(content)
words = content.split()
wordCount = len(words)

lines = content.splitlines()
line_count = len(lines)


print("Character Count: ", character_count)
print("Word Count: ", wordCount)
print("Line Count:" , line_count)

file.close()