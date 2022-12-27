# Saisir des donnees a l\'ecran jusqu\'a done. Afficher le minumum et le
# maximum. Proteger des erreurs avec try.

maximum = None
minimum = None

while True:
    try:
        data = input('Enter a number: ')

        if data == 'done':
            break

        data = float(data)

        if maximum is None or data > maximum:
            maximum = data

        if minimum is None or data < minimum:
            minimum = data

    except:
        print('Bad data')

print('Minimum is : ' + str(minimum))
print('Maximum is : ' + str(maximum))
