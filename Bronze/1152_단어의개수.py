sentence = input().split(' ')
words = []
for i in sentence:
    words.append(i)
    if i == "":
         words.remove(i)

print(len(words))