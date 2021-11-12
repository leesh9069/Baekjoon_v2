n = int(input())

for _ in range(n):
    num, test = input().split()
    result = ''
    lst = []
    for j in test:
        lst.append(j)
        result += j * int(num)

    print(result)
