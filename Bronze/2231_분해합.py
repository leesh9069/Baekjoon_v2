n = int(input())
new_lst = []

for i in range(n):
    lst = []
    for j in str(i):
        lst.append(int(j))

    if i + sum(lst) == n:
        new_lst.append(i)
        break

if len(new_lst) != 0:
    print(new_lst[0])

else:
    print(0)