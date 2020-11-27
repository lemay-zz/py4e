
str = 'X-DSPAM-Confidence:0.8475'
depart = str.find(':') + 1
reponse = float(str[depart:])
print(reponse)