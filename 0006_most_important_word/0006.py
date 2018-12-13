import os
import operator
from word_statistic import word_statistic

dir = "docs"
file_list = os.listdir(dir)

if __name__ == "__main__":
    for file in file_list:
        dic = word_statistic(os.path.join(dir, file))
        sorted_dic = sorted(dic.items(),key=operator.itemgetter(1))[::-1]
        print(file, "==>", sorted_dic[0][0], sorted_dic[0][1])
