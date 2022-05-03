from sys import argv


vowels = ["a", "e", "i", "o", "u"]

text = argv[1]
vowel_count = 0

for i in text:
    if i in vowels:
        vowel_count += 1

print('Number of vowels in the word:')
print(text)
print ("is")
print(vowel_count)

