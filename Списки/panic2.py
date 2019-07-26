phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

#for i in range(11,7,-1):
#    plist.pop()

#plist.pop(0)

#letter1 = ''.join(plist[0:2])
#letter2 = ''.join(plist[3])
#letter3 = ''.join(plist[6:4:-1])

#new_phrase = letter1 + " " + letter2 + letter3

new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5],plist[4],plist[7],plist[6]])

print(plist)
print(new_phrase)
