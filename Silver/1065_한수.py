n = int(input())
new_list = []
if n >= 100:
    for i in range(100, n+1):
        lst = []
        for j in str(i):
            lst.append(int(j))
        if lst[0] - lst[1] == lst[1] - lst[2]:
            new_list.append(i)
    print(len(new_list)+99)

else:
    print(n)