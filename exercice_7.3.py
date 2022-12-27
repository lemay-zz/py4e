# a program to prompt for a file name, and then read through the file and
# look for lines of the form X-DSPAM-Confidence: 0.8475

try:
    fichier = input("Entrez un nom de fichier : ")
    fhand = open(fichier)

except BaseException:
    if fichier == 'shit':
        print('Soyez poli!')
        exit()
    else:
        print('Le fichier ' + fichier + ' n\'existe pas')
        exit()

confidence = 0.0
count = 0

for ligne in fhand:
    if ligne.startswith('X-DSPAM-Confidence'):
        count = count + 1
        ligne = ligne.rstrip()
        chiffre = float(ligne[len(ligne)-6:])
        confidence = confidence + chiffre

moyenne = confidence/count
print('La confiance moyenne est de : ' + str(moyenne))
