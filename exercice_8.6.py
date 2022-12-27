# Rewrite the program that prompts the user for a list of numbers and
# prints out the maximum and minimum of the numbers at the end when the
# user enters “done”. Write the program to store the numbers the user
# enters in a list and use the max() and min() functions to compute the
# maximum and minimum numbers after the loop completes.

numlist = []
while True:
    new = input('Entrez un chiffre :')
    if new == 'done': break

    try:
        new = float(new)

    except BaseException:
        print('Entrez un nombre valide svp')
        continue

    numlist.append(new)

print('Le maximum saisi est ' + str(max(numlist)) + ' et le minimum est ' + str(min(numlist)))
