def chop(zelist) :
    del zelist[0]
    del zelist[-1]

def middle(zelist) :
    last_index = len(zelist) - 1
    newlist = zelist[1:last_index] # alternate method than del zelist[-1]
    return newlist

dalist = [2,5,7,34,78,154]
dalist2 = [2,5,7,34,78,154]
print(chop(dalist))
print(middle(dalist2))
