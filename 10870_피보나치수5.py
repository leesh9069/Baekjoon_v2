n = int(input())
cnt = 1
pibo = [0, 1]

for i in range(2, n+1):
    c = pibo[i-1] + pibo[i-2]
    pibo.append(c)

print(pibo[n])