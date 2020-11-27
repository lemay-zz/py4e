#Exercise 2: This program counts the distribution of the hour of the day for
#each of the messages. You can pull the hour from the “From” line by finding
#the time string and then splitting that string into parts using the colon
#character. Once you have accumulated the counts for each hour, print out
#the counts, one per line, sorted by hour as shown below.

heures = dict()
fichier = input('Entrez un nom de fichier : ')
if len(fichier) < 1 :
    fichier = 'mbox-short.txt'

try :
    fhand = open(fichier)

except :
    print('Entrez un nom de fichier valide svp')
    exit()
# Ici les fichiers mbox-short.txt ou mbox.txt ne correspondent pas a ce qui
# etait attendu. La ligne From: ne contient qu'a un seul endroit la date et
# l'heure. J'ai donc choisi de faire ma selection sur "Date:". Par contre
# il y a deux format de ligne avec "Date:". J'ai selectionne celle qui
# mesurait 8 mots de long afin de ne pas compter en double.
for line in fhand :
    if "Date:" not in line : continue
    words = line.split()
    if len(words) != 8 : continue
    hour = words[2]
    hour = hour.split(':')
    hour = hour[0]
# La ligne suivante est une autre facon d'ecrire les lignes 35 a 38
# On peut la lire comme : Chaque entree du dict heures = si hour n'existe pas
# le defaut 0 s'applique + 1. La premiere lecture d'une hour donnera donc 1
# Si hour existe, alors on ajoute 1 au compteur.
    heures[hour] = heures.get(hour, 0) +1
#    if hour not in heures :
#        heures[hour] = 1
#    else :
#        heures[hour] += 1

lst = list()
for k,v in list(heures.items()) :
    lst.append((k,v))

lst.sort()

for k,v in lst :
    print(k,v)
