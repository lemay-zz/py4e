#Write a program to read through the mail box data and when you find line
#that starts with “From”, you will split the line into words using the
#split function. We are interested in who sent the message, which is the
#second word on the From line.

#You will parse the From line and print out the second word for each From
#line, then you will also count the number of From (not From:) lines and
#print out a count at the end.

fhand = open('mbox-short.txt')
count = 0
for line in fhand :
    if not line.startswith('From') : continue
    line2 = line
    line = line.split()
    if len(line) > 2 :
        print(line[1])
    if line2.startswith('From:') : continue
    count = count + 1

print('There was ' + str(count) + ' lines in mbox-short.txt with From as the first word')
