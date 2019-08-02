def search4vowels(phrase:str) -> set:

    """ This func search for vowels in word."""

    """ another type of comment. 
        multistring
    """
    vowels = set('aeiou')

    #word = input('Provide a word to search for vowels: ')

    #found = vowels.intersection(set(word))
    return vowels.intersection(set(phrase))

    #for vowel in found:
    #    print(vowel)

    #return bool(found)
