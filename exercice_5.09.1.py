# Saisir des donnees a l\'ecran jusqu\'a done. Afficher la somme.
# Proteger des erreurs avec try

somme = 0.0
count = 0

while True:
    try:
        data = input('Enter a number: ')
        if data == 'done':
            break
        somme = somme + float(data)
        count = count + 1
    except:

        print('Bad data')

print('Sum is : ' + str(somme))
print('Count is : ' + str(count))
print('Average is : ' + str(somme/count))
