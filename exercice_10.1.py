# exercise 1: Revise a previous program as follows: Read and parse the “From”
# lines and pull out the addresses from the line. Count the number of messages
# from each person using a dictionary.

# After all the data has been read, print the person with the most commits by
# creating a list of (count, email) tuples from the dictionary. Then sort the
# list in reverse order and print out the person who has the most commits.

courriels = dict()

# On capture le nom du fichier à analyser et on s'assure de son existence
fichier = input('Entrez un nom de fichier : ')

try:
    fhand = open(fichier)

except BaseException:
    print('Entrez un nom de fichier valide svp')
    exit()

# On commence l'analyse et on rempli le dictionnaire avec le email et le
# nombre d'occurence .en mettant le nombre en premier (pour le tri à venir).
for line in fhand:
    if len(line) == 0 or "From:" not in line: continue
    words = line.split()
    email = words[1]
    if email not in courriels:
        courriels[email] = 1
    else:
        courriels[email] += 1

# On transfère le contenu du dictionnaire dans la liste lst
# en mettant le nombre en premier (pour le tri à venir).
lst = list()
for key, val in list(courriels.items()):
    lst.append((val, key))

# on trie du plus grand au plus petit pour trouver le plus grand nombre et
# on inverse la première paire (courriel avant le nombre) avant de l'imprimer
lst.sort(reverse=True)
resultat = lst[0]
print(resultat[1], resultat[0])
