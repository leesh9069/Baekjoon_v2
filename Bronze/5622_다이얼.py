word = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = 0

for i in word:
    if i in alpha[0:3]:
        num += 3
    elif i in alpha[3:6]:
        num += 4
    elif i in alpha[6:9]:
        num += 5
    elif i in alpha[9:12]:
        num += 6
    elif i in alpha[12:15]:
        num += 7
    elif i in alpha[15:19]:
        num += 8
    elif i in alpha[19:22]:
        num += 9
    elif i in alpha[22:]:
        num += 10

print(num)