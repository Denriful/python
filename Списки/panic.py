phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

exclude_letters = ["D","'","i","c","!"]

for letter in phrase:
    if letter in exclude_letters:
        plist.remove(letter)

plist.pop()
plist.insert(2," ")
plist.pop(4)
plist.pop(5)
plist.insert(4,"a")

new_phrase="".join(plist)

print(plist)
print(new_phrase)
