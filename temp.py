import numpy as np
import jieba
import time


# def init():
#     # Initial dictionary
#     # init_arr = np.zeros(10)
#     # print(init_arr)
#     temp_dic = {}
#     word_set_dic = temp_dic.fromkeys(string_of_class)
#     print(word_set_dic)

# temp_dic = {}
# word_set_dic = temp_dic.fromkeys(string_of_class)
# print(word_set_dic)


def load_test_label():

    file_labels = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_labels = file_labels + "Dataset/test_labels.txt"

    # f_label = open(file_labels, 'r', encoding='UTF-8')
    return file_labels


def load_test_file(own_class):

    file_input_name = "C:/Users/28012/Desktop/Statistical Learning/naive Bayes/"
    file_input_name = file_input_name + 'Dataset/test_data_' + own_class + '.txt'

    # f_test = open(file_input_name, 'r', encoding='UTF-8')
    return file_input_name


def load_train_file(own_class):

    file_input_name = "C:/Users/28012/Desktop/Statistical Learning/naive Bayes/"
    file_input_name = file_input_name + 'Dataset/train_data_' + own_class + '.txt'

    # f_test = open(file_input_name, 'r', encoding='UTF-8')
    return file_input_name

# Test


def count_word_train(file_class, name_class):

    word_list = np.loadtxt(file_class, str)
    # print(len(word_list))
    # print(type(word_list))
    # print(word_list)
    word_list = word_list.tolist()
    # print(type(word_list))
    # print(word_list)
    # print(len(word_list))
    # print(word_set_dic)
    if name_class in word_set_dic:
        word_set_dic[name_class] = {}
    else:
        print("ERROR")
        return
    for word in word_list:
        if word in word_set_dic[name_class]:
            word_set_dic[name_class][word] += 1
        else:
            word_set_dic[name_class][word] = 1

    """ Function Programming """
    sorted_list = sorted(word_set_dic[name_class].items(
    ), key=lambda item: item[1], reverse=True)
    # print(sorted_list)

    # print(word_set_dic)
    return name_class


def process_train_word(file_class, name_class):

    word_list = np.loadtxt(file_class, str)
    # print(len(word_list))
    # print(type(word_list))
    # print(word_list)
    word_list = word_list.tolist()
    # print(type(word_list))
    # print(word_list)
    # print(len(word_list))
    # print(word_set_dic)
    cnt = 0
    if name_class in word_set_dic:
        word_set_dic[name_class] = {}
    else:
        print("ERROR")
        return
    for word in word_list:
        cnt = cnt + 1
        if word in word_set_dic[name_class]:
            word_set_dic[name_class][word] += 1
        else:
            word_set_dic[name_class][word] = 1

    """ Function Programming """
    sorted_list = sorted(word_set_dic[name_class].items(
    ), key=lambda item: item[1], reverse=True)
    # print(sorted_list)

    print(cnt)
    copy = word_set_dic[name_class].copy()
    for key in copy.keys():
        copy[key] = copy[key]/cnt

    """ Function Programming """
    sorted_copy_list = sorted(
        copy.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_copy_list)

    return sorted_list, cnt


def naiveBayes():

    # print(word_set_dic)
    # print(word_set_dic)
    # print(count_word_train(f_train_car, 'car') + " Done")
    # print(wd)
    # print(nc)

    f_train_car = load_train_file('car')
    f_train_finance = load_train_file('finance')
    f_train_science = load_train_file('science')
    f_train_health = load_train_file('health')
    f_train_sports = load_train_file('sports')
    f_train_education = load_train_file('education')
    f_train_culture = load_train_file('culture')
    f_train_military = load_train_file('military')
    f_train_joy = load_train_file('joy')
    f_train_fashion = load_train_file('fashion')

    print(count_word_train(f_train_car, 'car') + " Done")
    print(count_word_train(f_train_finance, 'finance') + " Done")
    print(count_word_train(f_train_science, 'science') + " Done")
    print(count_word_train(f_train_health, 'health') + " Done")
    print(count_word_train(f_train_sports, 'sports') + " Done")
    print(count_word_train(f_train_education, 'education') + " Done")
    print(count_word_train(f_train_culture, 'culture') + " Done")
    print(count_word_train(f_train_military, 'military') + " Done")
    print(count_word_train(f_train_joy, 'joy') + " Done")
    print(count_word_train(f_train_fashion, 'fashion') + " Done")

    l1, n1 = process_train_word(f_train_car, "car")
    l2, n2 = process_train_word(f_train_finance, 'finance')
    l3, n3 = process_train_word(f_train_science, 'science')
    l4, n4 = process_train_word(f_train_health, 'health')
    l5, n5 = process_train_word(f_train_sports, 'sports')
    l6, n6 = process_train_word(f_train_education, 'education')
    l7, n7 = process_train_word(f_train_culture, 'culture')
    l8, n8 = process_train_word(f_train_military, 'military')
    l9, n9 = process_train_word(f_train_joy, 'joy')
    l10, n10 = process_train_word(f_train_fashion, 'fashion')

    # print(num)
    # print(len(all_list))
    num = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
    all_list = l1 + l2 + l3 + l4 + l5 + l6 + l7 + l8 + l9 + l10


def test():
    # Load data
    test_label = load_test_label()

    f_test_car = load_test_file('car')
    f_test_finance = load_test_file('finance')
    f_test_science = load_test_file('science')
    f_test_health = load_test_file('health')
    f_test_sports = load_test_file('sports')
    f_test_education = load_test_file('education')
    f_test_culture = load_test_file('culture')
    f_test_military = load_test_file('military')
    f_test_joy = load_test_file('joy')
    f_test_fashion = load_test_file('fashion')


if __name__ == "__main__":

    # Initialization
    dic = {}
    string_of_class = ['car',
                       'finance',
                       'science',
                       'health',
                       'sports',
                       'education',
                       'culture',
                       'military',
                       'joy',
                       'fashion']

    # init()
    # word_set_dic.fromkeys(string_of_class)
    word_set_dic = dic.fromkeys(string_of_class)

    naiveBayes()
    # print(word_set_dic)
    # print(word_set_dic["car"])
    # print(word_set_dic["joy"])
