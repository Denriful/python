def search4vowels ():
# print vowesl in provided word
    """ another type of comment. 
        multistring
    """
    vowels = set('aeiou')

    word = input('Provide a word to search for vowels: ')

    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)
