n = int(input())

for _ in range(n):
    word = input()
    if word.count("(") == word.count(")"):
        f = 0
        r = 0
        for i in word:
            if i == '(':
                f += 1
            else:
                r += 1
            if r > f:
                word = 'NO'
        if word == 'NO':
            print('NO')
        else:
            print('YES')

    else:
        print('NO')