s = input('Enter a sentence: ')
acr = ''
for i in s.split(' '):
    acr += i[0]
print(acr.upper())