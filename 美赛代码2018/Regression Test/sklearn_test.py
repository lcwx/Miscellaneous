from sklearn import linear_model
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy
import math
import pandas as pd
import xlrd
import matplotlib.pyplot as plt
import sklearn

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


count = 0
list_AZ = []
for i in range(sheet_new.nrows):
    process_list = sheet_new.row_values(i)
    if process_list[1] == "AZ":
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

print("length: ", len(dict_AZ_processed))
# print(list_AZ_processed)
print("AZ number: ", count)

print(dict_AZ_processed.keys)
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

dict_CA = preprocess("CA")
print("length: ", len(dict_CA))

dict_AZ = preprocess("AZ")
print("length: ", len(dict_AZ))

dict_NM = preprocess("NM")
print("length: ", len(dict_NM))

dict_TX = preprocess("TX")
print("length: ", len(dict_TX))


# def drawGraph(state_name, cat):
#     dict_State = preprocess(state_name)
#     x = []
#     y = []

#     for key in dict_State:
#         x.append(key)
#     # print(x)
#     for key in dict_State:
#         # print(type(dict_State[key]))
#         dict_one_year = dict_State[key]
#         if cat not in dict_one_year.keys():
#             y.append(-1000000)
#         else:
#             y.append(dict_one_year[cat])
#     # print(y)

#     plt.figure()
#     plt.plot(x, y)
#     pic_name = "results/" + state_name + "_" + cat + ".jpg"
#     plt.savefig(pic_name)


# def drawSmoothLine(state_name, cat):
#     dict_State = preprocess(state_name)
#     x = []
#     y = []

#     for key in dict_State:
#         x.append(key)
#     # print(x)
#     for key in dict_State:
#         # print(type(dict_State[key]))
#         dict_one_year = dict_State[key]
#         if cat not in dict_one_year.keys():
#             y.append(-1000000)
#         else:
#             y.append(dict_one_year[cat])
#     # print(y)
#     x = np.array(x)
#     y = np.array(y)
#     xnew = np.linspace(x.min(), x.max(), 1000)

#     smooth = spline(x, y, xnew)

#     plt.figure()
#     plt.plot(xnew, smooth)
#     pic_name = "results/" + state_name + "_" + cat + "_smooth" + ".jpg"
#     plt.savefig(pic_name)


# drawGraph("CA", "PATCP")
# drawGraph("AZ", "PATCP")
# drawGraph("NM", "PATCP")
# drawGraph("TX", "PATCP")
# drawGraph("CA", "REPRB")
# drawGraph("AZ", "REPRB")
# drawGraph("NM", "REPRB")
# drawGraph("TX", "REPRB")
# drawGraph("CA", "NNTCB")
# drawGraph("AZ", "NNTCB")
# drawGraph("NM", "NNTCB")
# drawGraph("TX", "NNTCB")

# drawSmoothLine("CA", "PATCP")

class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs):
        if epoch % 100 == 0:
            print('')
        print('.', end='')


def regression(list_X, list_Y, learning_rate=0.1, EPOCHS=1000):
    # Data processing
    # print(list_Y)
    dataset = []
    for ele in list_X:
        dataset.append([ele])
    train_labels = []
    # c_t = list_Y.copy()
    # c_t = numpy.array(c_t)
    # m = c_t.mean()
    # s = math.sqrt(c_t.var())
    # v = (ele - m) / s
    for ele in list_Y:
        train_labels.append(ele)
    dataset = numpy.array(dataset)
    train_labels = numpy.array(train_labels)
    # print(numpy.shape(train_labels))
    # print(train_labels)

    # Parameters
    learning_rate = learning_rate
    EPOCHS = EPOCHS

    # Network Parameters
    n_hidden_1 = 64
    n_hidden_2 = 64
    n_hidden_3 = 16
    input_shape = 1
    num_classes = 1

    def build_model(input_shape):
        model = keras.Sequential([
            layers.Dense(n_hidden_1, activation=tf.nn.relu,
                         input_shape=[input_shape]),
            layers.Dense(n_hidden_2, activation=tf.nn.relu),
            layers.Dense(n_hidden_3, activation=tf.nn.sigmoid),
            layers.Dense(num_classes)
        ])

        # optimizer = tf.train.RMSPropOptimizer(learning_rate)
        optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    model = build_model(input_shape)
    model.summary()

    # example_batch = dataset[:10]
    # print(example_batch)
    # example_result = model.predict(example_batch)
    # print(example_result)

    history = model.fit(
        dataset, train_labels,
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
        plt.ylim([0, 5])
        plt.savefig("1.jpg")

        plt.figure()
        plt.xlabel('Epoch')
        plt.ylabel('Mean Square Error [$MPG^2$]')
        plt.plot(hist['epoch'], hist['mean_squared_error'],
                 label='Train Error')
        plt.plot(hist['epoch'], hist['val_mean_squared_error'],
                 label='Val Error')
        plt.legend()
        plt.ylim([0, 1])
        plt.savefig("2.jpg")

    print()
    plot_history(history)

    # example_result = model.predict(dataset_test[:1])
    # print("\nresult:", example_result)
    shape = numpy.shape(dataset)
    output = []
    for i in range((shape[0])):
        result = model.predict(dataset[i:i+1])
        # print(result[0][0])
        r = result[0][0]
        output.append(r)

    # print(output)
    return output


def drawTwoGraph(state_name, cat):
    dict_State = preprocess(state_name)
    x = []
    y = []

    for key in dict_State:
        v = (key - 1960)
        if v > 15:
            v = v / 5 + 13
            x.append(v)
        else:
            x.append(v)
    # print(x)
    # for key in dict_State:
    #     x.append(key)
    # # print(x)
    # x = numpy.array(x)
    # # print(x)
    # m = x.mean()
    # s2 = x.var()
    # s = math.sqrt(s2)
    # cnt = 0
    # for ele in x:
    #     x[cnt] = (ele - m) / s
    #     cnt = cnt + 1

    for key in dict_State:
        # print(type(dict_State[key]))
        dict_one_year = dict_State[key]
        if cat not in dict_one_year.keys():
            y.append(-1000000)
        else:
            y.append(dict_one_year[cat])
    # print(y)

    # plt.figure()
    # plt.plot(x, y)
    # pic_name = "results/" + state_name + "_" + cat + ".jpg"
    # plt.savefig(pic_name)

    c_y = y.copy()
    c_y = numpy.array(c_y)
    m = c_y.min()
    # s = math.sqrt(c_y.var())
    M = c_y.max()
    c_y = c_y.tolist()
    y.clear()
    for ele in c_y:
        v = (ele - m) / (M - m)
        # print(v)
        y.append([v])
    y_ = regression(x, y, learning_rate=0.002, EPOCHS=100)
    plt.figure()
    plt.plot(x, y)
    plt.plot(x, y_)
    plt.savefig("results.jpg")


# drawTwoGraph("CA", "PATCP")
# drawTwoGraph("AZ", "PATCP")
# drawTwoGraph("AZ", "REPRB")

def sklearnDraw(state_name, cat):
    dict_State = preprocess(state_name)
    x = []
    y = []

    for key in dict_State:
        # key = key - 1960
        # print(key)
        x.append([key])

    # for key in dict_State:
    #     v = (key - 1960)
    #     if v > 15:
    #         v = v / 5 + 13
    #         x.append(v)
    #     else:
    #         x.append(v)

    for key in dict_State:
        # print(type(dict_State[key]))
        dict_one_year = dict_State[key]
        if cat not in dict_one_year.keys():
            y.append(-1000000)
        else:
            y.append(dict_one_year[cat])
    # print(y)

    # plt.figure()
    # plt.plot(x, y)
    # pic_name = "results/" + state_name + "_" + cat + ".jpg"
    # plt.savefig(pic_name)

    c_y = y.copy()
    c_y = numpy.array(c_y)
    m = c_y.min()
    # s = math.sqrt(c_y.var())
    M = c_y.max()
    c_y = c_y.tolist()
    y.clear()
    for ele in c_y:
        v = (ele - m) / (M - m)
        # print(v)
        y.append(v)
    # print(y)

    # n_samples, n_features = 10, 5
    # numpy.random.seed(0)
    # y = numpy.random.randn(n_samples)
    # X = numpy.random.randn(n_samples, n_features)
    # clf = linear_model.SGDRegressor(max_iter=100, tol=0.1)
    # clf = sklearn.svm.SVR()
    # clf = sklearn.neighbors.KNeighborsRegressor(n_neighbors=6)
    # clf = sklearn.linear_model.SGDRegressor(max_iter=1000, tol=0.01)
    clf = sklearn.linear_model.BayesianRidge()
    # clf = sklearn.gaussian_process.GaussianProcessRegressor()
    clf.fit(x, y)

    # print(clf.predict(x))
    y_ = clf.predict(x)

    plt.figure()
    plt.plot(x, y)
    plt.plot(x, y_)
    plt.savefig("results_Bayes.jpg")


sklearnDraw("CA", "PATCP")
