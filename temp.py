import numpy as np
import jieba


# read the stop word list
def init_stopwords():
    stopwords_file = open('stopwords.txt', 'r', encoding='UTF-8')
    stopwords_list = []
    for line in stopwords_file.readlines():
        stopwords_list.append(line)
    # print(stopwords_list)
    # print(stopwords_list[0])
    swList = np.array(stopwords_list)
    return swList


# Use jieba library to devide words
def devide_words(raw_word, swList):
    # use jieba
    # words = np.array(jieba.cut(raw_word, cut_all=False))
    words = list(jieba.cut(raw_word, cut_all=False))
    for word in words:
        if word in swList:
            words.remove(word)

    temp = '\n'
    if temp in words:
        words.remove('\n')
    words = np.array(words)
    return words


def loadtoFiles():
    # Devide data into two parts
    # One is training data, the other is test data
    # The number of training data is 4000, the number of test data is 1000

    # file name
    file_input = 'news_data.txt'
    file_output_test_labels = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_labels = file_output_test_labels + \
        "naive Bayes/naive Bayes/test_labels.txt"

    file_output_training_car = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_car = file_output_training_car + \
        'naive Bayes/naive Bayes/train_data_car.txt'
    file_output_test_car = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_car = file_output_test_car + \
        'naive Bayes/naive Bayes/test_data_car.txt'

    file_output_training_finance = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_finance = file_output_training_finance + \
        'naive Bayes/naive Bayes/train_data_finance.txt'
    file_output_test_finance = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_finance = file_output_test_finance + \
        'naive Bayes/naive Bayes/test_data_finance.txt'

    file_output_training_science = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_science = file_output_training_science + \
        'naive Bayes/naive Bayes/train_data_science.txt'
    file_output_test_science = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_science = file_output_test_science + \
        'naive Bayes/naive Bayes/test_data_science.txt'

    file_output_training_health = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_health = file_output_training_health + \
        'naive Bayes/naive Bayes/train_data_health.txt'
    file_output_test_health = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_health = file_output_test_health + \
        'naive Bayes/naive Bayes/test_data_health.txt'

    file_output_training_sports = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_sports = file_output_training_sports + \
        'naive Bayes/naive Bayes/train_data_sports.txt'
    file_output_test_sports = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_sports = file_output_test_sports + \
        'naive Bayes/naive Bayes/test_data_sports.txt'

    # Initialization
    data = open(file_input, 'r', encoding='UTF-8')
    labels = open(file_output_test_labels, "w")
    swList = init_stopwords()

    train_set_car = []
    f_train_car = open(file_output_training_car, "w")
    f_test_car = open(file_output_test_car, "w")

    train_set_finance = []
    f_train_finance = open(file_output_training_finance, "w")
    f_test_finance = open(file_output_test_finance, "w")

    train_set_science = []
    f_train_science = open(file_output_training_science, "w")
    f_test_science = open(file_output_test_science, "w")

    train_set_health = []
    f_train_health = open(file_output_training_health, "w")
    f_test_health = open(file_output_test_health, "w")

    train_set_sports = []
    f_train_sports = open(file_output_training_sports, "w")
    f_test_sports = open(file_output_test_sports, "w")

    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    cnt5 = 0
    cnt6 = 0
    cnt7 = 0
    cnt8 = 0
    cnt9 = 0
    cnt10 = 0

    for line in data.readlines():
        if line[0] == '汽' and line[1] == '车':
            # print("get")
            cnt1 = cnt1 + 1
            # print(words)
            # print(words)
            if cnt1 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_car.extend(words)
            else:
                labels.write("汽车")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_car.write(word + " ")
                f_test_car.write('\n')
        elif line[0] == '财' and line[1] == '经':
            # print("get")
            cnt2 = cnt2 + 1
            if cnt2 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_finance.extend(words)
            else:
                labels.write("财经")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_finance.write(word + " ")
                f_test_finance.write('\n')
        elif line[0] == '科' and line[1] == '技':
            cnt3 = cnt3 + 1
            if cnt3 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_science.extend(words)
            else:
                labels.write("科技")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_science.write(word + " ")
                f_test_science.write('\n')
        elif line[0] == '健' and line[1] == '康':
            cnt4 = cnt4 + 1
            if cnt4 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_health.extend(words)
            else:
                labels.write("健康")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_health.write(word + " ")
                f_test_health.write('\n')
        elif line[0] == '体' and line[1] == '育':
            cnt5 = cnt5 + 1
            if cnt5 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_sports.extend(words)
            else:
                labels.write("体育")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_sports.write(word + " ")
                f_test_sports.write('\n')

    # print(train_set_car[0])
    # print(train_set_car[1])
    # print(train_set_car[12])
    # print(cnt)

    # print(train_set_car.tostring())
    # train_set_car = str(train_set_car, encoding='utf-8')
    # test_set_car = str(test_set_car.tostring())
    for word in train_set_car:
        f_train_car.write(word + " ")
    # f_test_car.write(test_set_car)
    # print(train_set_car)
    f_train_car.close()
    f_test_car.close()

    for word in train_set_finance:
        f_train_finance.write(word + " ")
    f_train_finance.close()
    f_test_finance.close()

    for word in train_set_science:
        f_train_science.write(word + " ")
    f_train_science.close()
    f_test_science.close()

    for word in train_set_health:
        f_train_health.write(word + " ")
    f_train_health.close()
    f_test_health.close()

    for word in train_set_sports:
        f_train_sports.write(word + " ")
    f_train_sports.close()
    f_test_sports.close()


if __name__ == "__main__":

    # arr_sw = init_stopwords()
    # print(arr)
    # test = "我是帅哥"
    # arr_w = devide_words(test, arr_sw)
    # print(arr_w)
    loadtoFiles()
