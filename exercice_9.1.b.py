# Write a program that reads the words in words.txt and stores them as keys
# in a dictionary. We'll then count the occurence of each words in the file.

weird_dict = dict()
fhand = open('words.txt')

for line in fhand:
    line = line.strip().split()
    for word in line:
        if word.isalpha():
            weird_dict[word] = weird_dict.get(word, 0) + 1

print(weird_dict)

clef = list(weird_dict.keys())
valeur = list(weird_dict.values())
mot_repete = (clef[valeur.index(max(valeur))])
print('==================================================================')
print('Le mot "' + mot_repete + '" est utilisé ' + str(max(weird_dict.values())) + ' fois.')
print('==================================================================')

# lst = list(weird_dict.keys())
# lst.sort()
# for key in lst:
#     print(key, weird_dict[key])
#
# print('======================')
# for word in weird_dict:
#    if weird_dict[word] > 3:
#        print(word, weird_dict[word])
