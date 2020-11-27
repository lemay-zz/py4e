#Exercise 1: Revise a previous program as follows: Read and parse the “From”
#lines and pull out the addresses from the line. Count the number of messages
#from each person using a dictionary.

#After all the data has been read, print the person with the most commits by
#creating a list of (count, email) tuples from the dictionary. Then sort the
#list in reverse order and print out the person who has the most commits.

courriels = dict()
lst = list()
fichier = input('Entrez un nom de fichier : ')

try :
    fhand = open(fichier)

except :
    print('Entrez un nom de fichier valide svp')
    exit()

for line in fhand :
    if len(line) == 0 or "From:" not in line : continue
    words = line.split()
    email = words[1]
    if email not in courriels :
        courriels[email] = 1
    else :
        courriels[email] += 1


lst.sort(reverse=True)

courriel = list(lst[0])
print(courriel[1], courriel[0])
