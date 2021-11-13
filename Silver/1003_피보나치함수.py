n = int(input())

def pibo(number):
    lst = [[1, 0], [0, 1]]
    for i in range(2, number+1):
        num_lst = [lst[i-1][1], sum(lst[i-1])]
        lst.append(num_lst)

    return lst[-1]

for _ in range(n):
    num = int(input())
    if num == 0:
        print(1, 0)
    elif num == 1:
        print(0, 1)
    else:
        a = pibo(num)
        print(a[0], a[1])