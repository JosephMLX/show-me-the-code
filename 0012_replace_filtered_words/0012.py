from get_words import get_words

if __name__ == "__main__":
    words = get_words("filtered_words.txt")
    while True:
        sentence = input()
        for word in words:
            if str(word) in sentence:
                sentence = sentence.replace(word, len(str(word)) * '*')
        print(sentence)


