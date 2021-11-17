from collections import Counter
from sys import stdin
n = stdin.readline()
N = stdin.readline().split()
m = stdin.readline()
M = stdin.readline().split()

c = Counter(N)

print(' '.join(f'{c[i]}' if i in c else '0' for i in M))