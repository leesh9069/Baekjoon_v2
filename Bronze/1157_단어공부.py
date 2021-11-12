words = input().upper() #BAAA
words_list = list(set(words)) #['B','A']

count_words = []
for x in words_list:
    cnt = words.count(x) #1, 3
    count_words.append(cnt) #[1, 3]

if count_words.count(max(count_words)) > 1:
    print('?')

else:
    max_index = count_words.index(max(count_words))
    print(words_list[max_index])