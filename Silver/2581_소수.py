m = int(input())
n = int(input())

lst = []
for i in range(m, n+1):
    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break

    else:
        lst.append(i)

if len(lst) == 0:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))