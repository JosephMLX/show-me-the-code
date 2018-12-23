def get_words(file):
    f = open(file, 'r')
    words = []
    lines = f.read().splitlines()
    for line in lines:
        words.append(line)
    return words


if __name__ == "__main__":
    words = get_words("filtered_words.txt")
    while True:
        word = input()
        if word in words:
            print('Human Rights')
        else:
            print('Freedom')
