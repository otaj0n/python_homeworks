s = input()
d = '*'
vow = 'aouei'
for i in s:
    if i in vow:
        s = s.replace(i, d)
print(s)