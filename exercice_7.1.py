# a program to read through a file and print the contents of the file
# (line by line) all in upper case.

try:
    fichier = input('Enter a file name: ')
    fhand = open(fichier)
    for ligne in fhand:
        print(ligne.rstrip().upper())

except BaseException:
    print('Fichier ' + fichier + ' non trouvé')
