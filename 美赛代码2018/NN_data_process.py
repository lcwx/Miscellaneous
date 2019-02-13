# import tensorflow as tf
import math
import matplotlib.pyplot as plt
import numpy
import tensorflow as tf
import xlrd
import pandas as pd
from numpy.polynomial.polynomial import Polynomial
from scipy.interpolate import lagrange
from tensorflow import keras
from tensorflow.keras import layers

feature = []

feature.append("NNTCB")
feature.append("NUETV")
feature.append("RETCB")
feature.append("PATCP")
feature.append("PATCB")
feature.append("LOTCB")
feature.append("REPRB")
feature.append("GDPRX")
feature.append("TPOPP")
feature.append("FFTCB")
feature.append("TETCB")
feature.append("WWTCB")
feature.append("ESTCB")
feature.append("TEPRB")
feature.append("AVACD")
feature.append("RFEIV")
feature.append("REPRB")
feature.append("TEICB")

# print(feature)
print("length of features: ", len(feature))

book = xlrd.open_workbook("ProblemCData.xlsx")
for sheet in book.sheets():
    print(sheet.name)

sheet_new = book.sheet_by_name("seseds")
print("nrows: ", sheet_new.nrows)
# print(sheet_new.row_values(12))


def preprocess(name):
    count = 0
    list_AZ = []
    for i in range(sheet_new.nrows):
        process_list = sheet_new.row_values(i)
        if process_list[1] == name:
            count = count + 1
            list_AZ.append(process_list)

    dict_AZ_processed = {}
    for year in range(1959, 2011):
        list_temp = []
        for i in range(len(list_AZ)):
            ele = list_AZ[i]
            temp = ele[2]
            if int(temp) == year:
                ele_new = []
                ele_new.append(ele[0])
                ele_new.append(ele[3])
                list_temp.append(ele_new)
        if len(list_temp) > 0:
            dict_AZ_processed.update({year: list_temp})

    # print("length: ", len(dict_AZ_processed))
    # print(list_AZ_processed)
    # print("AZ number: ", count)

    # print(dict_AZ_processed.keys)
    # print(len(dict_AZ_processed.keys))
    for key in dict_AZ_processed:
        # print(key)
        list_for_process = dict_AZ_processed[key]
        # no use
        set_ = []
        for j in range(len(list_for_process)):
            # print(list_for_process[j][0])
            # print(len(list_for_process))
            set_.append(list_for_process[j][0])
        set_ = set(set_)
        # print(len(set_))

        temp_dict = {}
        for k in range(len(list_for_process)):
            keys_ = temp_dict.keys()
            if list_for_process[k][0] in keys_:
                print("ERROR!")
                break
            temp_dict.update({list_for_process[k][0]: list_for_process[k][1]})

        dict_AZ_processed.update({key: temp_dict})

    # print("length: ", len(dict_AZ_processed))
    return dict_AZ_processed


dict_CA = preprocess("CA")
print("length: ", len(dict_CA))

dict_AZ = preprocess("AZ")
print("length: ", len(dict_AZ))

dict_NM = preprocess("NM")
print("length: ", len(dict_NM))

dict_TX = preprocess("TX")
print("length: ", len(dict_TX))


def create_dataset_state(dict_state, state_name, feature):
    count_deficiency = 0
    dataset = []

    for key in dict_state:
        # if key == 2009:
        #     print("!!!!!!!!!!!!!!!!!!!!")
        one_data = numpy.array([])
        for ele in feature:
            if ele in dict_state[key].keys():
                one_data = numpy.append(one_data, dict_state[key][ele])
            else:
                one_data = numpy.append(one_data, 0)
                count_deficiency = count_deficiency + 1
                # print("There is a deficiency in", key, "of", ele, "!")
        # print("################")
        # print(one_data)
        # print("################")
        dataset.append(one_data)
        # print(dataset)

        # # print(key)
        # if key == 2005:
        #     temp = numpy.array([])
        #     for ele in feature:
        #         # print(dict_state[key][ele])
        #         temp = numpy.append(temp, dict_state[key][ele])
        #     ave = temp.mean()
        #     s2 = temp.var()
        #     s = math.sqrt(s2)

        #     for index in range(len(temp)):
        #         temp[index] = (temp[index]-ave)/s
        #         print(temp[index])

    print("number of deficiency: ", count_deficiency)
    print("length of dataset: ", len(dataset))
    dataset = numpy.array(dataset)
    # print(dataset)
    return dataset


dataset_CA = create_dataset_state(dict_CA, "CA", feature)
# create_dataset_state(dict_AZ, "AZ", feature)
# create_dataset_state(dict_NM, "NM", feature)
# create_dataset_state(dict_TX, "TX", feature)


def Lagrange_me(list_X, list_Y, x0):
    poly = lagrange(list_X, list_Y)
    poly = Polynomial(poly).coef
    output = 0
    # print(poly)
    for i in range(len(poly)):
        output = output + poly[i] * math.pow(x0, (len(poly)-1-i))

    return output


# test
list_X = [0, 1, 2]
list_Y = [0, 1, 8]
print(Lagrange_me(list_X, list_Y, 3))

# complement


def complement(dataset, draw=False):
    # print(numpy.shape(dataset))
    # print(numpy.size(dataset[0]))
    # print(numpy.size(dataset))
    num1 = numpy.shape(dataset)[0]
    num2 = numpy.shape(dataset)[1]
    for i_2 in range(num2):
        # print(numpy.size(dataset[0]))
        # print(i_2)
        index_X = []
        index_Y = []
        index_L = numpy.array([])
        for i_1 in range(num1):
            # print(numpy.size(dataset))
            # print(i_1,i_2)
            if dataset[i_1][i_2] != 0:
                index_X.append(i_1)
                index_Y.append(dataset[i_1][i_2])
            else:
                index_L = numpy.append(index_L, i_1)

        index_L.sort()
        # print("\n*****************")
        # print(index_X)
        # # print(index_Y)
        # print(index_L)
        # print("*****************\n")
        if draw:
            plt.figure()
            plt.plot(index_X, index_Y)
            plt.savefig("test_pic/%d.jpg" % i_2)
        for ele in index_L:
            # print(Lagrange_me(index_X, index_Y, ele))
            ele = int(ele)
            # print(ele)
            # print(index_X)
            # print(index_Y)
            dataset[ele][i_2] = Lagrange_me(index_X, index_Y, ele)
            # print(Lagrange_me(index_X, index_Y, 25))

        index_X.clear()
        index_Y.clear()
        for i in range(num1):
            index_X.append(i)
            # if dataset[i][i_2] > 1000000:
            #     index_Y.append(0)
            # else:
            #     index_Y.append(dataset[i][i_2])
            index_Y.append(dataset[i][i_2])

        if draw:
            plt.figure()
            plt.plot(index_X, index_Y)
            plt.savefig("result_pic/%d.jpg" % i_2)

    return dataset

# overflow
# complement(dataset_CA)


# normalization
def norm(dataset_O, ifvar=True):
    dataset = dataset_O.copy()

    num1 = numpy.shape(dataset)[0]
    num2 = numpy.shape(dataset)[1]
    for i in range(num1):
        ave = dataset[i].mean()
        s2 = dataset[i].var()
        s = math.sqrt(s2)
        if ifvar:
            for j in range(num2):
                dataset[i][j] = (dataset[i][j]-ave)/s
                # print(temp[index])
        else:
            for j in range(num2):
                dataset[i][j] = dataset[i][j]/s

    return dataset


dataset_test = norm(dataset_CA)
dataset_test = complement(dataset_test)
train_labels = dataset_test.copy()[1:]
dataset_test = dataset_test[:49]

print(numpy.shape(dataset_test))
print(numpy.shape(train_labels))

# Parameters
learning_rate = 0.01
EPOCHS = 3000

# Network Parameters
n_hidden_1 = 56
n_hidden_2 = 56
n_hidden_3 = 32
input_shape = 18
num_classes = 18


def build_model(input_shape):
    model = keras.Sequential([
        layers.Dense(n_hidden_1, activation=tf.nn.relu,
                     input_shape=[input_shape]),
        layers.Dense(n_hidden_2, activation=tf.nn.relu),
        layers.Dense(n_hidden_3, activation=tf.nn.relu),
        layers.Dense(num_classes)
    ])

    optimizer = tf.train.RMSPropOptimizer(learning_rate)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse'])
    return model


model = build_model(18)
model.summary()

# print(numpy.shape(dataset_test[0]))
# dataset_test[0] = numpy.reshape(dataset_test[0],())
# example_result = model.predict(dataset_test[:1])
# print(example_result)

# Display training progress by printing a single dot for each completed epoch


class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0:
            print('')
        print('.', end='')


history = model.fit(
    dataset_test, train_labels,
    epochs=EPOCHS, validation_split=0.2, verbose=0,
    callbacks=[PrintDot()])

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()


def plot_history(history):
    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Abs Error [MPG]')
    plt.plot(hist['epoch'], hist['mean_absolute_error'],
             label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
             label='Val Error')
    plt.legend()
    plt.ylim([0, 0.5])
    plt.savefig("NN_result/1.jpg")

    plt.figure()
    plt.xlabel('Epoch')
    plt.ylabel('Mean Square Error [$MPG^2$]')
    plt.plot(hist['epoch'], hist['mean_squared_error'],
             label='Train Error')
    plt.plot(hist['epoch'], hist['val_mean_squared_error'],
             label='Val Error')
    plt.legend()
    plt.ylim([0, 0.5])
    plt.savefig("NN_result/2.jpg")


plot_history(history)

example_result = model.predict(dataset_test[:1])
print("\nresult:", example_result)
