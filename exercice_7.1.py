#a program to read through a file and print the contents of the file 
#(line by line) all in upper case.

fhand = open('mbox-short.txt')
for ligne in fhand :
    print(ligne.rstrip().upper())
