import numpy as np
import jieba
import time


# read the stop word list
def init_stopwords():
    stopwords_file = open('stopwords.txt', 'r', encoding='UTF-8')
    stopwords_list = []
    for line in stopwords_file.readlines():
        # if '\n' in line:
        #     cnt = 0
        #     for ele in line:
        #         cnt = cnt + 1
        #         if ele == '\\':
        #             # print(ele)
        #             break
        #     line = line[:cnt-1]
        #     # print(line)
        # print(line.strip("\n"))
        # print(line)
        line = line.strip("\n")
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
    # print(words)
    # swList.tolist()
    # print(swList)
    copy_words = words[:]
    for word in words:
        # print(word)
        if word in swList:
            # print("Done")
            # print(word)
            # Woc, 这个bug是真tm坑人啊
            copy_words.remove(word)

    temp = '\n'
    if temp in copy_words:
        # words.remove('\n')
        copy_words.remove('\n')
    #words = np.array(words)
    copy_words = np.array(copy_words)
    return copy_words


def loadtoFiles():
    # Devide data into two parts
    # One is training data, the other is test data
    # The number of training data is 4000, the number of test data is 1000

    # file name
    file_input = 'news_data.txt'
    file_output_test_labels = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_labels = file_output_test_labels + \
        "Dataset/test_labels.txt"

    file_output_training_car = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_car = file_output_training_car + \
        'Dataset/train_data_car.txt'
    file_output_test_car = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_car = file_output_test_car + \
        'Dataset/test_data_car.txt'

    file_output_training_finance = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_finance = file_output_training_finance + \
        'Dataset/train_data_finance.txt'
    file_output_test_finance = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_finance = file_output_test_finance + \
        'Dataset/test_data_finance.txt'

    file_output_training_science = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_science = file_output_training_science + \
        'Dataset/train_data_science.txt'
    file_output_test_science = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_science = file_output_test_science + \
        'Dataset/test_data_science.txt'

    file_output_training_health = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_health = file_output_training_health + \
        'Dataset/train_data_health.txt'
    file_output_test_health = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_health = file_output_test_health + \
        'Dataset/test_data_health.txt'

    file_output_training_sports = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_sports = file_output_training_sports + \
        'Dataset/train_data_sports.txt'
    file_output_test_sports = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_sports = file_output_test_sports + \
        'Dataset/test_data_sports.txt'

    file_output_training_education = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_education = file_output_training_education + \
        'Dataset/train_data_education.txt'
    file_output_test_education = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_education = file_output_test_education + \
        'Dataset/test_data_education.txt'

    file_output_training_culture = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_culture = file_output_training_culture + \
        'Dataset/train_data_culture.txt'
    file_output_test_culture = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_culture = file_output_test_culture + \
        'Dataset/test_data_culture.txt'

    file_output_training_military = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_military = file_output_training_military + \
        'Dataset/train_data_military.txt'
    file_output_test_military = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_military = file_output_test_military + \
        'Dataset/test_data_military.txt'

    file_output_training_joy = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_joy = file_output_training_joy + \
        'Dataset/train_data_joy.txt'
    file_output_test_joy = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_joy = file_output_test_joy + \
        'Dataset/test_data_joy.txt'

    file_output_training_fashion = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_training_fashion = file_output_training_fashion + \
        'Dataset/train_data_fashion.txt'
    file_output_test_fashion = 'C:/Users/28012/Desktop/Statistical Learning/naive Bayes/'
    file_output_test_fashion = file_output_test_fashion + \
        'Dataset/test_data_fashion.txt'

    # Initialization
    data = open(file_input, 'r', encoding='UTF-8')
    labels = open(file_output_test_labels, "w")
    swList = init_stopwords()
    # print(swList)

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

    train_set_education = []
    f_train_education = open(file_output_training_education, "w")
    f_test_education = open(file_output_test_education, "w")

    train_set_culture = []
    f_train_culture = open(file_output_training_culture, "w")
    f_test_culture = open(file_output_test_culture, "w")

    train_set_military = []
    f_train_military = open(file_output_training_military, "w")
    f_test_military = open(file_output_test_military, "w")

    train_set_joy = []
    f_train_joy = open(file_output_training_joy, "w")
    f_test_joy = open(file_output_test_joy, "w")

    train_set_fashion = []
    f_train_fashion = open(file_output_training_fashion, "w")
    f_test_fashion = open(file_output_test_fashion, "w")

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
        elif line[0] == '教' and line[1] == '育':
            cnt6 = cnt6 + 1
            if cnt6 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_education.extend(words)
            else:
                labels.write("教育")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_education.write(word + " ")
                f_test_education.write('\n')
        elif line[0] == '文' and line[1] == '化':
            cnt7 = cnt7 + 1
            if cnt7 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_culture.extend(words)
            else:
                labels.write("文化")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_culture.write(word + " ")
                f_test_culture.write('\n')
        elif line[0] == '军' and line[1] == '事':
            cnt8 = cnt8 + 1
            if cnt8 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_military.extend(words)
            else:
                labels.write("军事")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_military.write(word + " ")
                f_test_military.write('\n')
        elif line[0] == '娱' and line[1] == '乐':
            cnt9 = cnt9 + 1
            if cnt9 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_joy.extend(words)
            else:
                labels.write("娱乐")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_joy.write(word + " ")
                f_test_joy.write('\n')
        elif line[0] == '时' and line[1] == '尚':
            cnt10 = cnt10 + 1
            if cnt10 <= 400:
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                train_set_fashion.extend(words)
            else:
                labels.write("时尚")
                labels.write('\n')
                line = line[3:]
                words = devide_words(line, swList)
                words = words.tolist()
                for word in words:
                    f_test_fashion.write(word + " ")
                f_test_fashion.write('\n')

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

    for word in train_set_education:
        f_train_education.write(word + " ")
    f_train_education.close()
    f_test_education.close()

    for word in train_set_culture:
        f_train_culture.write(word + " ")
    f_train_culture.close()
    f_test_culture.close()

    for word in train_set_military:
        f_train_military.write(word + " ")
    f_train_military.close()
    f_test_military.close()

    for word in train_set_joy:
        f_train_joy.write(word + " ")
    f_train_joy.close()
    f_test_joy.close()

    for word in train_set_fashion:
        f_train_fashion.write(word + " ")
    f_train_fashion.close()
    f_test_fashion.close()


if __name__ == "__main__":

    t1 = time.clock()
    # arr_sw = init_stopwords()
    # # print(arr_sw)
    # test = "12我是一个有很强自我【约束能力】的帅哥"
    # arr_w = devide_words(test, arr_sw)
    # print(arr_w)
    loadtoFiles()
    t2 = time.clock()
    print(t2-t1)
