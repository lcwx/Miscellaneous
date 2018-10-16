import time
import csv
import math


def read_train_data(filename):
    csvFile = open(filename, "r")
    reader = csv.reader(csvFile)

    output = [[1 for j in range(1, 12)] for i in range(1, 892)]
    num = 0
    for item in reader:
        if reader.line_num == 1:
            continue
        for cnt in range(11):
            output[num][cnt] = item[cnt + 1]
        num = num + 1

    train_data = [[1 for j in range(1, 12)] for i in range(1, 701)]
    test_data = [[1 for j in range(1, 12)] for i in range(1, 192)]

    cnt = 0
    for i in range(891):
        if cnt < 700:
            for t in range(11):
                train_data[cnt][t] = output[cnt][t]
            cnt = cnt + 1
        else:
            for r in range(11):
                test_data[cnt - 700][r] = output[cnt - 700][r]
            cnt = cnt + 1

    csvFile.close()
    return train_data, test_data


def info_gain_ratio(data):
    


if __name__ == "__main__":

    fn = "dataset/train.csv"
    train_test, test_test = read_train_data(fn)
