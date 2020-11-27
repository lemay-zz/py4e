def count(word,char) :
    occurence = 0
    for letter in word :
        if letter == char :
            occurence = occurence + 1
    return(occurence)

mot = input('Entrez un mot: ')
lettre = input('Entrez la lettre a chercher: ')

print(count(mot,lettre))
