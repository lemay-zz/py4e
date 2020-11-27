#Write a program that reads the words in words.txt and stores them as keys
#in a dictionary. We'll then count the occurence of each words in the file.

weird_dict = dict()
fhand = open('words.txt')

for line in fhand :
    line = line.split()
    for word in line :
        weird_dict[word] = weird_dict.get(word,0) + 1

print(weird_dict)
print('======================')
print('Le maximum est : ' + max(weird_dict))

print('======================')

lst = list(weird_dict.keys())
lst.sort()
for key in lst :
    print(key, weird_dict[key])

print('======================')
for word in weird_dict :
    if weird_dict[word] > 3 :
        print(word , weird_dict[word])
