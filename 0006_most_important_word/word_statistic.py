import re


def word_statistic(file):
    f = open(file, 'r')
    words = []
    lines = f.read().splitlines()
    for line in lines:
        words_in_line = list(filter(None, line.split(' ')))
        for word in words_in_line:
            word = re.sub(r'[^\w\s]', '', word)
            words.append(word)

    statistic = {}
    for word in words:
        if word not in statistic:
            statistic[word] = 1
        else:
            statistic[word] += 1
    return statistic


if __name__ == "__main__":
    dic = word_statistic("poem.txt")
    for key in dic:
        print(key, '==>', dic[key])