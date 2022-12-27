# exercice_9.1.c
# lire un fichier et compter le nombre d'occurence de chacun des mots.
# on enregistre le tout dans un dictionnaire qu'on imprime à la fin.

# on importe string pour accéder à la méthode punctuation qui permet le
# retait des signes de ponctuation
import string

# on demande le nom du fichier à analyser et on valide son existence
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except BaseException:
    print('File cannot be opened:', fname)
    exit()

# on créer le dictionnaire qui va recueillir tous les compteurs de mots
counts = dict()

# le début de la boucle permet le nettoyage des données:
# on enlève les caractères de fin de lign
# on retire les signes de ponctuation
# on met en minuscule
# et enfin on découpe la ligne en mots

for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    # la boucle suivante est optimisée avec la méthode get
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Ancienne boucle avec le test if word not in count. Même résultat, mais
# plus long. (plus facile à lire?)
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
print(counts)
