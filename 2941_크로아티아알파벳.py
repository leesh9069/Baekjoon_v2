words = str(input())

croatia_word = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'dz=', 'z=']
num = len(words)

cnt = 0
for i in croatia_word:
    if i in words:
        cnt += words.count(i)

print(num - cnt)