#Write a program to read through a mail log, build a histogram using a
#dictionary to count how many messages have come from each email address,
#and print the dictionary

#Add code to the above program to figure out who has the most messages in
#the file. After all the data has been read and the dictionary has been
#created, look through the dictionary using a maximum loop (see Chapter 5:
#Maximum and minimum loops) to find who has the most messages and print
#how many messages the person has.

occurence = dict()

fichier = input('Entrer un nom de fichier : ')

try:
    fhand = open(fichier)

except :
    print('Entrer un nom de fichier valide svp!')
    exit()

for line in fhand :
    mots = line.split()
    if len(mots) < 2 or mots[0] != 'From' : continue
    email = mots[1]
    if email not in occurence :
        occurence[email] = 1
    else:
        occurence[email] += 1

# identifier le maximum dans le dictionnaire occurence

largest = None

for courriel in occurence :
    val = int(occurence[courriel])
    if largest is None or val > largest :
        largest = val
        largest_mail = courriel

print('La personne ayant le plus de courriels est',largest_mail,':',str(largest))

