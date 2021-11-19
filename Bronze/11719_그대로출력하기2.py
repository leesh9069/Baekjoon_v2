n = int(input())


pibo = [0, 1]

for _ in range(2, n+1):
    pibo.append(pibo[-1]+pibo[-2])

print(pibo[-1])

