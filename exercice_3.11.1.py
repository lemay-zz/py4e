hours = float(input('Entrer les heures: '))
taux = float(input('Entrer le taux: '))
overtime = hours - 40
if overtime > 0 :
    hours = overtime * 1.5 + 40

paie = round(hours*taux,2)
print('Paye : '+ str(paie) + '$')
