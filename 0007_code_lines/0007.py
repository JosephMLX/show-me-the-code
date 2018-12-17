import glob

code_lines = 0
comment_lines = 0
empty_lines = 0

if __name__ == "__main__":
    for file in glob.glob('codes/*.py'):
        f = open(file, 'r')
        lines = f.read().splitlines()
        for line in lines:
            if line == '':
                empty_lines += 1
            elif line[0] == '#':
                comment_lines += 1
            else:
                code_lines += 1

    print('code lines:', code_lines)
    print('comment lines:', comment_lines)
    print('empty lines:', empty_lines)
