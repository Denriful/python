vowels = {"a","e","i","o","u"}
#word = "Milliways"
word = input("Provide a word to search for vowels: ")

found = vowels.intersection(set(word))

#found = []
#for letter in word:
#    if letter in vowels:
#        print(letter)
#        if letter not in found:
#            found.append(letter)

for vowel in found:
    print(vowel)
