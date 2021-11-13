from collections import Counter
import sys
n = int(sys.stdin.readline())

num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

avg = sum(num) / len(num)
print(int(round(avg)))
num.sort()
print(num[n//2])

cnt = Counter(num).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(num) - min(num))