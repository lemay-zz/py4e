fhand = open('romeo.txt')
bdmots = []
for line in fhand :
    line = line.split()
    for word in line :
        if word in bdmots : continue
        bdmots.append(word)

print(sorted(bdmots))
