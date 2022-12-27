def computegrade(grade):
    if grade > 1 or note < 0:
        print('SVP entrez une note entre 0.0 et 1.0')
    else:
        if grade <= 1 and grade >= 0.9:
            letter_grade = 'A'
        elif grade >= 0.8:
            letter_grade = 'B'
        elif grade >= 0.7:
            letter_grade = 'C'
        elif grade >= 0.6:
            letter_grade = 'D'
        else:
            letter_grade = 'Echec!!!'

    return letter_grade


try:
    note = float(input('Entrez une note entre 0.0 et 1.0 :'))
    lettre = computegrade(note)
    mention = ''
    if lettre == 'A':
        mention = 'Bravo!'
    print('Votre note est : ' + lettre + ' ' + mention)

except:
    print('SVP entrez une note entre 0.0 et 1.0')
