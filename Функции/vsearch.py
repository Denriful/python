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


def search4letters(phrase:str, letters:str) -> set:

""" Return sets of letters in phrase """

    return set(letters).intersection(set(phrase))
