def search4vowels ():
# print vowesl in provided word

    vowels = {"a","e","i","o","u"}

    word = input("Provide a word to search for vowels: ")

    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)
