n = int(input())
t = 2*n-1
for i in range(1, n+1):
    star = (i*2)-1
    print(" " * int((t-star)/2) + '*' * (i*2 -1))