import xlrd
import math
import tensorflow as tf
import numpy as np
import orangecontrib.associate.fpgrowth as oaf


book = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
for sheet in book.sheets():
    print(sheet.name)

sheet_new = book.sheet_by_name("Data")
print("nrows:", sheet_new.nrows)

# State name
SN = []
SN_dcit = {}
for i in range(sheet_new.nrows):
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

def END(med_name, state_name, Threshold=66, n=20, min_support=120):
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

    dataset_one = data_test.copy()
    # print(len(data_test))
    # print(len(data_test[0]))
    data_test = sepP(data_test)
    # print(data_test)
    # dataset_one = data_test.copy()

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

    w_list = []
    with tf.Session() as sess:
        for year in [year for year in range(2010, 2018)]:
            X = tf.nn.sigmoid((year - 2010) / 3)
            num = sess.run(X)
            w = 2.0 * (1.0 - num)
            # print(w)
            w_list.append(w)
            # print(X)

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
        scores.update({name: score})

    # print(scores)
    return scores


scores_test = END("Heroin", "VA", Threshold=67, n=21, min_support=120)
print(scores_test)

# X = tf.nn.sigmoid(1.0)
# with tf.Session() as sess:
#     print(sess.run(X))
#     # print(X)
