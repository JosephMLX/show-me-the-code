import re

f = open('poem.txt', 'r')
words = []
lines = f.read().splitlines()
for line in lines:
    words_in_line = line.split(' ')
    for word in words_in_line:
        word = re.sub(r'[^\w\s]', '', word)
        words.append(word)

d = {}
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1

for key in d:
    print(key, '==>', d[key])