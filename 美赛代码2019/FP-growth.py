from sklearn.neighbors import KNeighborsRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.gaussian_process import GaussianProcessRegressor
import sklearn.svm as skS
import sklearn.neighbors as skN
import pandas as pd
import numpy
from tensorflow.keras import layers
from tensorflow import keras
import xlrd
import xlwt
import math
import sklearn
import tensorflow as tf
import numpy as np
import orangecontrib.associate.fpgrowth as oaf
import matplotlib.pyplot as plt


w_list = []
with tf.Session() as sess:
    for year in [year for year in range(2010, 2018)]:
        X = tf.nn.sigmoid((year - 2010) / 3)
        num = sess.run(X)
        w = 2.0 * (1.0 - num)
        # print(w)
        w_list.append(w)
        # print(X)

book = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
for sheet in book.sheets():
    print(sheet.name)

sheet_new = book.sheet_by_name("Data")
print("nrows:", sheet_new.nrows)

# State name
SN = []
SN_dcit = {}
for i in range(1, sheet_new.nrows):
    process_data = sheet_new.row_values(i)
    SN.append(process_data[1])
SN = set(SN)
for key in SN:
    num = 0.0
    for i in range(sheet_new.nrows):
        process_data = sheet_new.row_values(i)
        # SN.append(process_data[1])
        if process_data[1] == key:
            num = process_data[3]
            break

    SN_dcit.update({key: num})
# print(SN_dcit)

# County name
CN_all = {}
for N in SN:
    CN = []
    CN_dict = {}
    for i in range(sheet_new.nrows):
        process_data = sheet_new.row_values(i)
        if process_data[1] == N:
            CN.append(process_data[2])
    CN = set(CN)
    for key in CN:
        num = 0.0
        for i in range(sheet_new.nrows):
            process_data = sheet_new.row_values(i)
            # SN.append(process_data[1])
            if process_data[2] == key and process_data[1] == N:
                num = process_data[5]
                # print(num)
                break

        CN_dict.update({key: num})

    # print(CN_dict)
    CN_all.update({N: CN_dict})


def get_data(med_name, state_name):
    file_name = "data/" + med_name + ".txt"
    with open(file_name, "r") as f:
        temp = f.read()
        _dict = eval(temp)

    CN = CN_all[state_name]
    # print(CN)
    # print(CN.values())
    CN_list = [key for key in CN]

    ouput_data = {}
    # {year: {numbering: {'DR': num, 'name': str}}}
    for key in _dict:
        ouput_data.update({key: []})
        for index in range(len(CN_list)):
            numbering = CN[CN_list[index]]
            # print(numbering)
            if numbering not in _dict[key]:
                ouput_data[key].append(0)
            else:
                num = _dict[key][numbering]["DR"]
                ouput_data[key].append(num)

    out = []
    for key in ouput_data:
        # print(key)
        out.append(ouput_data[key])

    # print(ouput_data)
    # print(out)
    # return ouput_data
    return out, CN_list


# data_test, CN_list = get_data("Heroin", "VA")

# Threshold = 5
# n = 21

# # print(len(data_test))
# data_test_temp = data_test.copy()
# length = len(data_test)
# data_test_temp = np.array(data_test_temp)
# CN_list_temp = CN_list.copy()

# l = np.array([])
# for j in range(len(CN_list)):
#     sum = 0
#     for i in range(length):
#         sum = sum + data_test[i][j]
#     l = np.append(l, sum)

# # Sort
# l.sort()
# # print(l)

# cnt = 0
# for j in range(len(CN_list)):
#     sum = 0
#     for i in range(length):
#         sum = sum + data_test[i][j]
#     # print(sum)
#     if sum <= l[len(l) - n - 1]:
#         data_test_temp = np.delete(data_test_temp, j-cnt, axis=1)
#         CN_list_temp.remove(CN_list[j])
#         cnt = cnt + 1

# data_test = data_test_temp.tolist()
# CN_list = CN_list_temp.copy()
# print("Shape: (%d, %d)" % (len(data_test), len(data_test[0])))

# for in1 in range(len(data_test)):
#     cnt = 1
#     for in2 in range(len(data_test[0])):
#         if data_test[in1][in2] > Threshold:
#             data_test[in1][in2] = cnt
#         else:
#             data_test[in1][in2] = 0
#         cnt = cnt + 1

# # print(data_test)


def tool_trans(l):
    out = []
    for i in range(len(l)):
        if l[i] != 0:
            out.append(l[i])

    return out


# # print(tool_trans([1, 0, 3]))
# for in3 in range(len(data_test)):
#     data_test[in3] = tool_trans(data_test[in3])

# print(data_test)
# print(data_test)
# dict_get_test = dict(oaf.frequent_itemsets(data_test, 2))
# print(dict_get_test)
# for key in dict_get_test:
# print(key,":", dict_get_test[key])


def sepP(dataset):

    def tool_temp(index, formL, behindL):
        outL = []
        for i in range(len(formL)):
            if i != index:
                outL.append(behindL[i])
            else:
                outL.append(formL[index])

        return outL

    output_data = []
    for in1 in range(1, len(dataset)):
        for in2 in range(len(dataset[0])):
            temp_l = tool_temp(in2, dataset[in1-1], dataset[in1])
            output_data.append(temp_l)

    return output_data


def get_data_pro(med_name, state_name, Threshold=66, n=20):
    file_name = "data/" + med_name + ".txt"
    with open(file_name, "r") as f:
        temp = f.read()
        _dict = eval(temp)

    CN = CN_all[state_name]
    # print(CN)
    # print(CN.values())
    CN_list = [key for key in CN]

    ouput_data = {}
    # {year: {numbering: {'DR': num, 'name': str}}}
    for key in _dict:
        ouput_data.update({key: []})
        for index in range(len(CN_list)):
            numbering = CN[CN_list[index]]
            # print(numbering)
            if numbering not in _dict[key]:
                ouput_data[key].append(0)
            else:
                num = _dict[key][numbering]["DR"]
                ouput_data[key].append(num)

    data_test = []
    for key in ouput_data:
        # print(key)
        data_test.append(ouput_data[key])

    # print(ouput_data)
    # print(out)
    # return ouput_data
    # return out, CN_list

    # data_test, CN_list = get_data("Heroin", "VA")

    # Threshold = 5
    # n = 21

    # print(len(data_test))
    data_test_temp = data_test.copy()
    length = len(data_test)
    data_test_temp = np.array(data_test_temp)
    CN_list_temp = CN_list.copy()

    l = np.array([])
    for j in range(len(CN_list)):
        sum = 0
        for i in range(length):
            sum = sum + data_test[i][j]
        l = np.append(l, sum)

    # Sort
    l.sort()
    # print(l)

    cnt = 0
    for j in range(len(CN_list)):
        sum = 0
        for i in range(length):
            sum = sum + data_test[i][j]
        # print(sum)
        if sum <= l[len(l) - n - 1]:
            data_test_temp = np.delete(data_test_temp, j-cnt, axis=1)
            CN_list_temp.remove(CN_list[j])
            cnt = cnt + 1

    data_test = data_test_temp.tolist()
    CN_list = CN_list_temp.copy()

    data_test = sepP(data_test)

    print("Shape: (%d, %d)" % (len(data_test), len(data_test[0])))
    print("CN_list shape: %d." % len(CN_list))

    for in1 in range(len(data_test)):
        cnt = 1
        for in2 in range(len(data_test[0])):
            if data_test[in1][in2] > Threshold:
                data_test[in1][in2] = cnt
            else:
                data_test[in1][in2] = 0
            cnt = cnt + 1

    # print(data_test)

    def tool_trans(l):
        out = []
        for i in range(len(l)):
            if l[i] != 0:
                out.append(l[i])

        return out

    # print(tool_trans([1, 0, 3]))
    for in3 in range(len(data_test)):
        data_test[in3] = tool_trans(data_test[in3])

    return data_test, CN_list


# data_test, CN_list = get_data_pro("Heroin", "VA")
# # print(data_test)
# dict_get_test = dict(oaf.frequent_itemsets(data_test, min_support=120))
# # print(dict_get_test)
# print(len(dict_get_test))


# def fuck(string):
#     list_out = []
#     tempStr = ""
#     ifB = False
#     for i in range(len(string)):
#         temp = string[i]
#         # print(temp)
#         # print(temp.isalnum())
#         if temp.isalnum():
#             # print("#")
#             tempStr = tempStr + temp
#             ifB = True
#         if (temp.isalnum() == False) and ifB:
#             # break
#             list_out.append(int(tempStr))
#             tempStr = ''
#             ifB = False

#     # print(list_out)
#     return list_out


# # fuck("[3, 4, 6, 11, 14, 15, 17, 19, 20]")


# def match(string):
#     string_ = ""
#     for i in range(len(string)):
#         # print(string[i])
#         if string[i] == "{":
#             for j in range(i, len(string)):
#                 if string[j] != "}":
#                     if string[j] == '{':
#                         string_ = string_ + '['
#                     else:
#                         string_ = string_ + string[j]
#                 else:
#                     string_ = string_ + "]"
#                     break
#             break

#     # def fuck(string):
#     #     list_out = []
#     #     tempStr = ""
#     #     ifB = False
#     #     for i in range(len(string)):
#     #         temp = string[i]
#     #         if temp.isalnum and (!ifB):
#     #             tempStr  = tempStr + temp
#     #             ifB = True
#     #         if (!temp.isalnum) and ifB:
#     #             # break
#     #             list_out.append( int(tempStr))
#     #             tempStr = ''
#     #             ifB = False

#     #     return list_out

#     # print(string_)
#     # list_ = list(string_)
#     list_ = fuck(string_)
#     return list_


# # print(type(match("frozenset({3, 4, 6, 11, 14, 15, 17, 19, 20})")))
# # print(match("frozenset({3, 4, 6, 11, 14, 15, 17, 19, 20})"))

# # # {index: list}
# # # {index: lenght}
# # ILi = {}
# # ILe = {}

# # Get max
# M = 0
# for Max in range(1, 20):
#     ifE = False
#     for key in dict_get_test:
#         # a = 0
#         value = dict_get_test[key]

#         # print(type(key))
#         str_key = str(key)
#         # print(str_key)
#         # print(key)
#         list_key = match(str_key)
#         # print(list_key)
#         if len(list_key) == Max:
#             # print(value)
#             # print(list_key)
#             # a = 0
#             # print("!")
#             ifE = True
#             break

#     if ifE:
#         pass
#     else:
#         # print(list_key)
#         M = Max - 1
#         break

# print(M)

# for key in dict_get_test:
#         # a = 0
#     value = dict_get_test[key]

#     # print(type(key))
#     str_key = str(key)
#     # print(str_key)
#     # print(key)
#     list_key = match(str_key)
#     # print(list_key)
#     if len(list_key) == M:
#         # if value != 140:
#         #     print(value)
#         print(value)
#         print(list_key)
#         # a = 0
#         # ifE = True
#         # break

#     if len(list_key) == 1:
#         print(value)
#         print(list_key)

def END(med_name, state_name, year_start=2010.0, Threshold=66, n=20, min_support=120, bias=1.1):
    file_name = "data/" + med_name + ".txt"
    with open(file_name, "r") as f:
        temp = f.read()
        _dict = eval(temp)

    CN = CN_all[state_name]
    # print(CN)
    # print(CN.values())
    CN_list = [key for key in CN]

    ouput_data = {}
    # {year: {numbering: {'DR': num, 'name': str}}}
    year_start = int(year_start)
    for key in _dict:
        if key >= year_start:
            # print("!!!!!!!!!!!!!!!")
            # print(key)
            # print(type(key))
            ouput_data.update({key: []})
            for index in range(len(CN_list)):
                numbering = CN[CN_list[index]]
                # print(numbering)
                if numbering not in _dict[key]:
                    ouput_data[key].append(0)
                else:
                    num = _dict[key][numbering]["DR"]
                    ouput_data[key].append(num)

    data_test = []
    for key in ouput_data:
        # print(key)
        data_test.append(ouput_data[key])

    # print(ouput_data)
    # print(out)
    # return ouput_data
    # return out, CN_list

    # data_test, CN_list = get_data("Heroin", "VA")

    # Threshold = 5
    # n = 21

    # print(len(data_test))
    data_test_temp = data_test.copy()
    length = len(data_test)
    data_test_temp = np.array(data_test_temp)
    CN_list_temp = CN_list.copy()

    l = np.array([])
    for j in range(len(CN_list)):
        sum = 0
        for i in range(length):
            sum = sum + data_test[i][j]
        l = np.append(l, sum)

    # Sort
    l.sort()
    # print(np.shape(l))
    # print(l)

    cnt = 0
    for j in range(len(CN_list)):
        sum = 0
        for i in range(length):
            sum = sum + data_test[i][j]
        # print(sum)
        if sum <= l[len(l) - n - 1]:
            data_test_temp = np.delete(data_test_temp, j-cnt, axis=1)
            CN_list_temp.remove(CN_list[j])
            cnt = cnt + 1

    data_test = data_test_temp.tolist()
    CN_list = CN_list_temp.copy()

    dataset_one = data_test.copy()
    # print(len(data_test))
    # print(len(data_test[0]))
    data_test = sepP(data_test)
    # print(data_test)
    # dataset_one = data_test.copy()

    # print("Shape: (%d, %d)" % (len(data_test), len(data_test[0])))
    # print("CN_list shape: %d." % len(CN_list))

    for in1 in range(len(data_test)):
        cnt = 1
        for in2 in range(len(data_test[0])):
            if data_test[in1][in2] > Threshold:
                data_test[in1][in2] = cnt
            else:
                data_test[in1][in2] = 0
            cnt = cnt + 1

    # print(data_test)

    def tool_trans(l):
        out = []
        for i in range(len(l)):
            if l[i] != 0:
                out.append(l[i])

        return out

    # print(tool_trans([1, 0, 3]))
    for in3 in range(len(data_test)):
        data_test[in3] = tool_trans(data_test[in3])

    # return data_test, CN_list

    # data_test, CN_list = get_data_pro("Heroin", "VA")
    # print(data_test)
    dict_get_test = dict(oaf.frequent_itemsets(data_test, min_support))
    # print(dict_get_test)
    # print(len(dict_get_test))

    def fuck(string):
        list_out = []
        tempStr = ""
        ifB = False
        for i in range(len(string)):
            temp = string[i]
            # print(temp)
            # print(temp.isalnum())
            if temp.isalnum():
                # print("#")
                tempStr = tempStr + temp
                ifB = True
            if (temp.isalnum() == False) and ifB:
                # break
                list_out.append(int(tempStr))
                tempStr = ''
                ifB = False

        # print(list_out)
        return list_out

    # fuck("[3, 4, 6, 11, 14, 15, 17, 19, 20]")

    def match(string):
        string_ = ""
        for i in range(len(string)):
            # print(string[i])
            if string[i] == "{":
                for j in range(i, len(string)):
                    if string[j] != "}":
                        if string[j] == '{':
                            string_ = string_ + '['
                        else:
                            string_ = string_ + string[j]
                    else:
                        string_ = string_ + "]"
                        break
                break

        # def fuck(string):
        #     list_out = []
        #     tempStr = ""
        #     ifB = False
        #     for i in range(len(string)):
        #         temp = string[i]
        #         if temp.isalnum and (!ifB):
        #             tempStr  = tempStr + temp
        #             ifB = True
        #         if (!temp.isalnum) and ifB:
        #             # break
        #             list_out.append( int(tempStr))
        #             tempStr = ''
        #             ifB = False

        #     return list_out

        # print(string_)
        # list_ = list(string_)
        list_ = fuck(string_)
        return list_

    # print(type(match("frozenset({3, 4, 6, 11, 14, 15, 17, 19, 20})")))
    # print(match("frozenset({3, 4, 6, 11, 14, 15, 17, 19, 20})"))

    # # {index: list}
    # # {index: lenght}
    # ILi = {}
    # ILe = {}

    # Get max
    M = 0
    for Max in range(1, 20):
        ifE = False
        for key in dict_get_test:
            # a = 0
            value = dict_get_test[key]

            # print(type(key))
            str_key = str(key)
            # print(str_key)
            # print(key)
            list_key = match(str_key)
            # print(list_key)
            if len(list_key) == Max:
                # print(value)
                # print(list_key)
                # a = 0
                # print("!")
                ifE = True
                break

        if ifE:
            pass
        else:
            # print(list_key)
            M = Max - 1
            break

    # print(M)

    value_M = 0
    end_list = []
    one_ele = {}
    for key in dict_get_test:
            # a = 0
        value = dict_get_test[key]

        # print(type(key))
        str_key = str(key)
        # print(str_key)
        # print(key)
        list_key = match(str_key)
        # print(list_key)
        if len(list_key) == M:
            # if value != 140:
            #     print(value)
            if value > value_M:
                value_M = value
                # print(value_M)
                end_list = list_key
            # print(value)
            # print(list_key)

            # a = 0
            # ifE = True
            # break

        if len(list_key) == 1:
            # print(value)
            # print(list_key)
            one_ele.update({list_key[0]: value})

    # print(one_ele)
    scores = {}
    for ele in end_list:
        name = CN_list[ele-1]
        score_temp = value_M / one_ele[ele]
        scores.update({name: score_temp})

    # print(scores)

    # print(end_list)
    for ele in end_list:
        # print(ele)
        # print(CN_list[ele])
        arr_temp = np.array([])
        # print(len(dataset_one))
        # print(len(dataset_one[0]))
        for i in range(len(dataset_one)):
            # print(dataset_one[i][ele])
            arr_temp = np.append(arr_temp, dataset_one[i][ele - 1])

        # m = arr_temp.mean()
        # s2 = arr_temp.var()
        # s = math.sqrt(s2)
        min_n = arr_temp.min()
        max_n = arr_temp.max()
        cnt = 0
        for e in arr_temp:
            arr_temp[cnt] = (e - min_n) / (max_n-min_n)
            # print(arr_temp[cnt])
            cnt = cnt + 1
        # print(arr_temp)
        # print(data_test)

        score = 0.0
        for i in range(len(arr_temp)):
            # print(w_list[i])
            score = score + arr_temp[i] * w_list[i]

        # print(score)
        name = CN_list[ele-1]
        # scores.update({name: score})
        scores[name] = scores[name] + bias * score

    # print(scores)
    output_scores = {}
    output_scores.update({state_name: scores})
    return output_scores


# scores_test = END("Heroin", "VA", Threshold=67,
    #   n=21, min_support=120, bias=1.1)
# print(scores_test)
# print(len(scores_test[]))
X = []
Y = []
for i in range(30, 150):
    X.append(i / 10.0)
    scores_test = END("Heroin", "VA", Threshold=70,
                      n=21, min_support=i, bias=1.1)
    print(len(scores_test["VA"]))
    Y.append(len(scores_test["VA"]))

plt.figure()
plt.xlabel("min-support / 10")
plt.ylabel("the length of FPS")
plt.plot(X, Y)
plt.savefig("tttttt.jpg")

# X = tf.nn.sigmoid(1.0)
# with tf.Session() as sess:
#     print(sess.run(X))
#     # print(X)

# print(SN)

# l_T = []
# l_Le = []
# # print(len(SN))
# SN = list(SN)
# print(SN)
# cnt = 0
# # for s in ["OH"]:
# # for s in SN:
# # for s in ['KY', 'VA', 'WV']:
# for s in ["VA"]:
#     print(s)
#     for T in range(20, 100):
#         print(".")
#         scores_test = END("Heroin", s, Threshold=T,
#                           n=21, min_support=120, bias=1.1)

#         # print(scores_test)
#     # print(scores_test)
#     # print(len(scores_test[]))
#         temp = len(scores_test[s])
#         sUm = 0
#         for key in scores_test[s]:
#             sUm = sUm + scores_test[s][key]
#         temp = sUm / temp
#         # print(temp)
#         l_T.append(T)
#         l_Le.append(temp)
#         cnt = cnt + 1

# out_scores = END("Heroin", "VA", Threshold=60,
#                  n=21, min_support=120, bias=1.1)
# # print(out_scores)
# scores_list = out_scores["VA"]


# def generation(state_name, year, min_s, T):
#     out_scores = END("Heroin", state_name, year_start=year, Threshold=T,
#                      n=21, min_support=min_s, bias=1.1)
#     # print(out_scores)
#     scores_list = out_scores[state_name]

#     file = xlwt.Workbook(encoding='utf-8')
#     sheet = file.add_sheet('Location_Num', cell_overwrite_ok=True)
#     sheet.write(0, 0, "Latitude")
#     sheet.write(0, 1, "Longitude")
#     sheet.write(0, 2, "Data")

#     # Read test
#     with open('LL.txt', 'r') as f:
#         a = f.read()
#         name_dict = eval(a)
#         # print(len(name_dict))
#         # print(dict_name)

#     def Change(key):
#         string = ""
#         # StateName = {"VA": "Virginia", "OH": "Ohio",
#         #      "PA": "Pennsylvania", "KY": "Kentucky", "WV": "West Virginia"}
#         # StateName[state_name]

#         for c in key:
#             if c != ",":
#                 string = string + c
#             else:
#                 break

#         # print(string)
#         return string

#     cnt = 1
#     for ele in scores_list:
#         for key in name_dict:
#             if ele == Change(key):
#                 sheet.write(cnt, 0, name_dict[key][0])
#                 sheet.write(cnt, 1, name_dict[key][1])
#                 sheet.write(cnt, 2, scores_list[ele])
#                 cnt = cnt + 1

#     name = str(year) + state_name + ".xls"
#     name = "spread/" + name
#     file.save(name)


# # # generation("VA")
# # T = 60
# # min_s = 120
# # for i in range(2010, 2017):
# #     i = float(i)
# #     print(i)

# #     if i == 2015.0:
# #         # print("!")
# #         min_s = 40
# #         T = 50
# #     elif i == 2016.0:
# #         # print("!")
# #         min_s = 21
# #         T = 50
# #     else:
# #         min_s = min_s - 15

# #     generation("VA", i, min_s, T)

# clf = skN.KNeighborsRegressor(n_neighbors=30)
# # # clf = skS.SVR()
# # # from sklearn.linear_model import ElasticNet
# # # clf = ElasticNet(random_state=0)
# # # clf = GaussianProcessRegressor()
# # # clf = GaussianNB()
# # X = [[0], [1], [2], [3]]
# # y = [0, 0, 1, 1]
# # neigh = KNeighborsRegressor(n_neighbors=2)
# # neigh.fit(X, y)

# # print(neigh.predict([[1.5]]))

# l_TC = []
# # print(l_T)
# for i in range(len(l_T)):
#     l_TC.append([l_T[i]])
# # print(l_TC)
# clf.fit(l_TC, l_Le)
# y_ = clf.predict(l_TC)

# # print("L_Le:")
# # print(l_Le)
# # plt.figure()
# # plt.plot(l_T, l_Le)
# # plt.plot(l_T, y_)
# # pic_name = "one.jpg"
# # plt.savefig(pic_name)
# # y_ = np.array(y_)
# innnn = 0
# mm = 10000
# for i in range(len(y_)):
#     if y_[i] < mm:
#         innnn = i
#         mm = y_[i]
# min_n = mm
# xx = l_T[innnn]
# plt.figure()
# plt.title("VA Heroin")
# plt.plot(l_T, l_Le, label="Scores")
# plt.plot(l_T, y_, label="Regression Results")
# plt.xlabel("Threshold")
# plt.ylabel("CCQRT")
# plt.text(xx, min_n, xx, ha='center', va='bottom')
# pic_name = "one.jpg"
# plt.legend()
# plt.savefig(pic_name)


# class PrintDot(keras.callbacks.Callback):
#     def on_epoch_end(self, epoch, logs):
#         if epoch % 100 == 0:
#             print('')
#         print('.', end='')


# def regression(list_X, list_Y, learning_rate=0.005, EPOCHS=500):
#     # Data processing
#     dataset = []
#     for ele in list_X:
#         dataset.append([ele])
#     train_labels = []
#     for ele in list_Y:
#         train_labels.append([ele])
#     dataset = numpy.array(dataset)
#     train_labels = numpy.array(train_labels)

#     # Parameters
#     learning_rate = learning_rate
#     EPOCHS = EPOCHS

#     # Network Parameters
#     n_hidden_1 = 16
#     n_hidden_2 = 64
#     n_hidden_3 = 8
#     input_shape = 1
#     num_classes = 1

#     def build_model(input_shape):
#         model = keras.Sequential([
#             layers.Dense(n_hidden_1, activation=tf.nn.relu,
#                          input_shape=[input_shape]),
#             layers.Dense(n_hidden_2, activation=tf.nn.sigmoid),
#             layers.Dense(n_hidden_3, activation=tf.nn.sigmoid),
#             layers.Dense(num_classes)
#         ])

#         optimizer = tf.train.RMSPropOptimizer(learning_rate)

#         model.compile(loss='mse',
#                       optimizer=optimizer,
#                       metrics=['mae', 'mse'])
#         return model

#     model = build_model(input_shape)
#     model.summary()

#     history = model.fit(
#         dataset, train_labels,
#         epochs=EPOCHS, validation_split=0.2, verbose=0,
#         callbacks=[PrintDot()])

#     hist = pd.DataFrame(history.history)
#     hist['epoch'] = history.epoch
#     hist.tail()

#     def plot_history(history):
#         plt.figure()
#         plt.xlabel('Epoch')
#         plt.ylabel('Mean Abs Error [MPG]')
#         plt.plot(hist['epoch'], hist['mean_absolute_error'],
#                  label='Train Error')
#         plt.plot(hist['epoch'], hist['val_mean_absolute_error'],
#                  label='Val Error')
#         plt.legend()
#         plt.ylim([0, 5])
#         plt.savefig("1.jpg")

#         plt.figure()
#         plt.xlabel('Epoch')
#         plt.ylabel('Mean Square Error [$MPG^2$]')
#         plt.plot(hist['epoch'], hist['mean_squared_error'],
#                  label='Train Error')
#         plt.plot(hist['epoch'], hist['val_mean_squared_error'],
#                  label='Val Error')
#         plt.legend()
#         plt.ylim([0, 5])
#         plt.savefig("2.jpg")

#     print()
#     plot_history(history)

#     # example_result = model.predict(dataset_test[:1])
#     # print("\nresult:", example_result)
#     shape = numpy.shape(dataset)
#     output = []
#     for i in range((shape[0])):
#         result = model.predict(dataset[i:i+1])
#         # print(result[0][0])
#         r = result[0][0]
#         output.append(r)

#     # print(output)
#     return output


# # for i in range(len(l_T)):
# #     l_T[i] = (l_T[i] - 19.0) / 20.0

# # for i in range(len(l_Le)):
# #     l_Le[i] = l_Le[i] * 100.0
# #     print(l_Le[i])

# # y_ = regression(l_T, l_Le, learning_rate=0.01, EPOCHS=500)
# # for i in range(len(y_)):
# #     y_[i] = y_[i] - 0.02

# # plt.figure()
# # plt.title("VA Heroin")
# # plt.plot(l_T, l_Le, label="Scores")
# # plt.plot(l_T, y_, label="Regression Results")
# # pic_name = "one.jpg"
# # plt.legend()
# # plt.savefig(pic_name)

# # for ele in l_T:
# #     print(ele)

# # for e in l_Le:ji
# #     print(e)

# [[A, B, E],
#  [A, C],
#  [D, B],
#  [C, B, E],
#  [B, C, D]]

#  [[B],
#   [C],
#   [B],
#   [B, C],
#   [B, C]]


# def build_tree(list_data, T):
#     if len(list_data) == 0:
#         return
#     else:
#         element = list_data.pop()
#         if element = T.child.name:
#             T.child.count = T.child.count + 1
#             build_tree(list_data, T)
#         else:
#             T = new_child(T)
#             T.new_child.name = element
#             T.new_child.count = 1
#             build_tree(list_data, T)
