def search4vowels (word):

    """ This func search for vowels in word."""

    """ another type of comment. 
        multistring
    """
    vowels = set('aeiou')

    #word = input('Provide a word to search for vowels: ')

    found = vowels.intersection(set(word))

    for vowel in found:
        print(vowel)
