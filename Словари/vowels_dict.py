vowels = ["a","e","i","o","u"]
word = "Hitchhiker"
#word = input("Provide a word to search for vowels: ")
found = {}
#found['a']=0
#found['e']=0
#found['i']=0
#found['o']=0
#found['u']=0

for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        
#        if found[letter] not in found:
#            found[letter] = 0
#        else:
        found[letter] += 1
        

for vowel,value in found.items():
#    if value > 0 :
        print(vowel,' was found ',value,' times')

    
