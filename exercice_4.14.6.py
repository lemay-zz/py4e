def computepay(h,t) :
    overtime = h - 40
    if overtime > 0 :
        h = overtime * 1.5 + 40

    p = round(h * t,2)
    return p


try :
    heures = float(input('Entrer les heures: '))
    taux = float(input('Entrer le taux: '))
    paie = computepay(heures,taux)
    print('Paye : '+ str(paie) + '$')


except :
    print('SVP Entrez un chiffre')
