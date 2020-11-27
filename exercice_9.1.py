#Write a program that reads the words in words.txt and stores them as keys
#in a dictionary. It doesn’t matter what the values are. Then you can use
#the in operator as a fast way to check whether a string is in the
#dictionary.

weird_dict = dict()
fhand = open('words.txt')

for line in fhand :
    line = line.split()
    for word in line :
        weird_dict[word] = ''

print('the' in weird_dict) # just to test if it's working
print(weird_dict)
