try :
    note = float(input('Entrez une note entre 0.0 et 1.0 :'))
    if note > 1 or note < 0 :
        print('SVP entrez une note entre 0.0 et 1.0')
    else :
        if note <= 1 and note >= 0.9 :
            print('A')
        elif note >= 0.8 :
            print('B')
        elif note >= 0.7 :
            print('C')
        elif note >= 0.6 :
            print('D')
        else :
            print('Echec!!!')

except :
    print('SVP entrez une note entre 0.0 et 1.0') 
   
    
