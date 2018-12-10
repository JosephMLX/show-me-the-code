# written by Joseph Meng 2018
# mlx7.xyz

from random import randrange


candidate = ''
for i in range(65, 91):
    candidate += chr(i)
for i in range(48, 58):
    candidate += chr(i)


def generate_promotion_code(code_num):
    promotion_code_list = []
    for _ in range(code_num):
        promotion_code = ''
        for j in range(12):
            random_index = randrange(len(candidate))
            promotion_code += candidate[random_index]
        promotion_code_list.append(promotion_code)
    return promotion_code_list


if __name__ == "__main__":
    code_list = generate_promotion_code(200)
    print(code_list)
