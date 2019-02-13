import pandas as pd
from sklearn.cluster import KMeans
import xlrd
import math
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D


F_L = 10
T_L = 11

book_list = []
for i in range(10, 17):
    # print(i)
    string = "part2_data/" + str(i) + ".xlsx"
    book = xlrd.open_workbook(string)
    book_list.append(book)
    # for sheet in book.sheets():
    #     print(sheet.name)

# sheet_new = book.sheet_by_name("Data")
# print("nrows:", sheet_new.nrows)
features = ["FH", "NH", "HLA", "HH", "MD", "SEE", "SEH", "SEC", "EAH", "WD"]
StateName = {"VA": "Virginia", "OH": "Ohio",
             "PA": "Pennsylvania", "KY": "Kentucky", "WV": "West Virginia"}
NameState = {"Virginia": "VA", "Ohio": "OH",
             "Pennsylvania": "PA", "Kentucky": "KY", "West Virginia": "WV"}


def change_name(string):
    ifP = False
    form_c = ''
    name = ""
    for c in string:
        # print(c)
        if (form_c == "," and c == " ") or ifP:
            # print(c)
            if ifP == False:
                ifP = True
            else:
                # print("c")
                ifP = True
                name = name + c

        form_c = c

    name = NameState[name]
    print(name)
    return name


# change_name("Upshur County, West Virginia")


def process_data(book, year):
    # {year: {state_county_numbering:[data]}}
    output_data = {}
    output_data.update({year: {}})

    sheet = book.sheet_by_name("Sheet1")
    # print("nrows:", sheet.nrows)
    for index in range(2, sheet.nrows):
        data_list = sheet.row_values(index)
        # print(len(data_list))
        # print(data_list[0])
        # name = change_name(data_list[0])
        # print(data_list[1])
        numbering = int(data_list[0])
        # print(data_list[0])
        numbering = str(numbering)
        # print(type(numbering))
        # print(numbering)
        # if len(data_list)> 100:
        #     print(len(data_list))
        if len(data_list) == T_L:
            li = data_list[2:].copy()
            # print(len(li))
            li.append(0.0)

            # li = np.array(li)
            # # print(li)
            # # m = li.mean()
            # m = 0
            # for i in range(np.shape(li)[0]):
            #     li[i] = li[i] - m
            # li = list(li)

            output_data[year].update({numbering: li})
        else:
            li = data_list[2:].copy()
            # print(li)

            # li = np.array(li)
            # m = li.mean()
            # for i in range(np.shape(li)[0]):
            #     li[i] = li[i] - m
            # li = list(li)

            output_data[year].update({numbering: li})

    # print(output_data)
    return output_data


data_set = {}
# output_data_test = process_data(book_list[0], "2010")
# print(output_data_test)
for i in range(2010, 2017):
    cnt = i - 2010
    i = str(i)
    data_set.update(process_data(book_list[cnt], i))

# print(data_set)

book_part_one = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
for sheet in book_part_one.sheets():
    print(sheet.name)

sheet_part1 = book_part_one.sheet_by_name("Data")
# print("nrows:", sheet_part1.nrows)

# {year: {numbering: num}}
labels = {}
for year in range(2010, 2017):
    year_s = str(year)
    labels.update({year_s: {}})
    year = float(year)
    for i in range(1, sheet_part1.nrows):
        p_d = sheet_part1.row_values(i)
        if p_d[0] == year:
            if p_d[5] in labels[year_s]:
                pass
            else:
                labels[year_s].update({str(int(p_d[5])): p_d[8]})

# print(labels)

# Test 2012
test_X = []
test_Y = []

test_year = "2013"
temp = np.array([])
for numbering in labels[test_year]:
    # if labels["2012"][numbering] > 500:
    #     temp = np.append(temp, -1)
    # else:
    #     temp = np.append(temp, labels["2012"][numbering])
    temp = np.append(temp, labels[test_year][numbering])
    # test_Y.append()
    test_X.append(data_set[test_year][numbering])

t_m = temp.mean()
t_s2 = temp.var()
t_s = math.sqrt(t_s2)

# for i in range(np.shape(temp)[0]):
#     # print("!")
#     temp[i] = (temp[i] - t_m) / t_s
cnt = 0
for i in range(np.shape(temp)[0]):
    if math.fabs(temp[i]-t_m) > 2.0 * t_s:
        # if math.fabs(temp[i]-t_m) > 1500:
        cnt = cnt + 1
        temp[i] = t_m
# print(cnt)
test_Y = temp.tolist()
# print(test_Y)

pca = PCA(n_components=1)
X_trans = pca.fit_transform(test_X)
# X_trans = pca.fit(test_X)
# pca.fit(test_X)
# pca.transform()
# print(pca.predict(test_X))
# print(len(test_X))
# print(len(test_X[0]))
# pca.fit_transform()
# print(X_trans)


def getNB(n_f, pca):

    def generation_arr(num, n_feature):
        l = [0 for _ in range(n_feature)]
        l[num] = 1
        # print(l)
        return l

    list_t = []
    for i in range(n_f):
        list_t.append(generation_arr(i, n_f))

    return pca.transform(list_t), list_t


# # # print(getNB(F_L, pca))
# in_test = np.array([[(i ** 2) for i in range(1, 104)]])
# # W_M = getNB(F_L, pca)
# # print(pca.transform(E))
# # W_M = np.array(W_M)
# # print(np.dot(in_test, W_M))
# # # print(np.dot(test_X, W_M))
# # # print(pca.fit_transform(test_X))
# # print(getNB(228, pca))
# arr_test, E = getNB(103, pca)
# arr_test = np.array(arr_test)
# # print(np.dot(E, arr_test))
# # print(pca.transform(E))
# # print(E)

# a = pca.transform(E)[0][0]
# b = np.dot(E, arr_test)[0][0]
# print(b / a)


# # m = -100000
# # ind = 0
# # for i in range(len(arr_test)):
# #     if arr_test[i][0] > m:
# #         ind = i
# #         m = arr_test[i][0]
# # print(m)
# # print(m)
# # print(ind)
# # print(arr_test)
# # arr = np.array(arr)
# # print(np.sort(arr))
# # print(arr)

# X = []
# for l in X_trans:
#     X.append(l[0])
# # print(X)
# plt.figure()
# plt.scatter(X, test_Y, color='r', s=10)
# # plt.plot(X, test_Y)
# # plt.plot(l_T, y_)
# pic_name = "test.jpg"
# plt.savefig(pic_name)


def test():
    K_X = []
    for i in range(len(X_trans)):
        temp_l = X_trans[i].copy()
        temp_l = np.append(temp_l, test_Y[i])
        K_X.append(temp_l)

    # print(K_X)
    kmeans = KMeans(n_clusters=2, random_state=0).fit(K_X)
    # kmeans.labels_
    Cls = kmeans.predict(K_X)
    # kmeans.cluster_centers_

    K_X = np.array(K_X)

    x1 = X_trans[:, 0]
    x2 = X_trans[:, 1]
    x3 = K_X[:, 2]

    cmap = plt.get_cmap('viridis')
    colors = [cmap(i) for i in np.linspace(0, 1, len(np.unique(Cls)))]
    ax = plt.subplot(111, projection='3d')

    for i, l in enumerate(np.unique(Cls)):
        _x1 = x1[Cls == l]
        _x2 = x2[Cls == l]
        _x3 = x3[Cls == l]
        # _y = y[Cls == l]
        # class_distr.append(plt.(_x1, _x2,, color=colors[i]))
        ax.scatter(_x1, _x2, _x3, color=colors[i])
    # ax.scatter(x1, x2, x3)

    plt.suptitle("PCA Dimensionality Reduction")
    plt.title("Digit Dataset")

    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')

    # plt.show()
    plt.savefig("3d.jpg")

# test()


class PCA_hand():
    def calculate_covariance_matrix(self, X, Y=None):
        # Calculate conv
        m = X.shape[0]
        X = X - np.mean(X, axis=0)
        Y = X if Y == None else Y - np.mean(Y, axis=0)
        return 1 / m * np.matmul(X.T, Y)
        # return 1 / m * np.dot(X.T, Y)

    def transform(self, X, n_components):

        covariance_matrix = self.calculate_covariance_matrix(X)
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

        idx = eigenvalues.argsort()[::-1]
        eigenvectors = eigenvectors[:, idx]
        eigenvectors = eigenvectors[:, :n_components]

        # Transform
        # a = eigenvectors[0][0]
        # print(type(a))
        return np.matmul(X, eigenvectors), eigenvectors
        # return np.dot(X, eigenvectors)


# pca_test = PCA_hand()
# X_trans, _ = pca_test.transform(np.array(test_X), 1)
# print(_)

# X = []
# for l in X_trans:
#     X.append(l[0])
# # print(X)
# plt.figure()
# plt.scatter(X, test_Y, color='r', s=10)
# # plt.plot(X, test_Y)
# # plt.plot(l_T, y_)
# pic_name = "test_h.jpg"
# plt.savefig(pic_name)

def trans(year):

    # Test 2012
    test_X = []
    test_Y = []

    test_year = str(year)
    temp = np.array([])
    for numbering in labels[test_year]:
        # if labels["2012"][numbering] > 500:
        #     temp = np.append(temp, -1)
        # else:
        #     temp = np.append(temp, labels["2012"][numbering])
        temp = np.append(temp, labels[test_year][numbering])
        # test_Y.append()
        test_X.append(data_set[test_year][numbering])

    t_m = temp.mean()
    t_s2 = temp.var()
    t_s = math.sqrt(t_s2)

    # for i in range(np.shape(temp)[0]):
    #     # print("!")
    #     temp[i] = (temp[i] - t_m) / t_s
    cnt = 0
    for i in range(np.shape(temp)[0]):
        if math.fabs(temp[i]-t_m) > 2.0 * t_s:
            # if math.fabs(temp[i]-t_m) > 1500:
            cnt = cnt + 1
            temp[i] = t_m
    # print(cnt)
    test_Y = temp.tolist()
    # print(test_Y)

    pca_test = PCA_hand()
    X_trans, M = pca_test.transform(np.array(test_X), 1)
    # print(M)
    _M = []
    for ele in M:
        _M.append(ele[0])

    # print(_M)

    # X = []
    # for l in X_trans:
    #     X.append(l[0])
    # # print(X)
    # plt.figure()
    # plt.scatter(X, test_Y, color='r', s=10)
    # # plt.plot(X, test_Y)
    # # plt.plot(l_T, y_)
    # pic_name = "test_" + test_year + ".jpg"
    # plt.savefig(pic_name)

    return _M


M = trans(2013)
# M_S = np.array([])
M_S = {}
for index, ele in enumerate(M):
    # M_S = np.append(M_S, math.fabs(ele))
    M_S.update({index: math.fabs(ele)})
# print(M_S)
# M_S.sort()
# print(M_S)

in_list = []
keys = M_S.keys()
l = len(M_S)
M_S_C = M_S.copy()

for _ in range(l):
    M = -100
    index = -1
    for key in M_S:
        if M_S[key] > M:
            M = M_S[key]
            index = key
    in_list.append(index)
    M_S.pop(index)

# print(in_list)
# print(M_S_C[in_list[0]])

string = "part2_data/" + "13" + ".xlsx"
book = xlrd.open_workbook(string)
# book_list.append(book)
sheet = book.sheet_by_name("Sheet1")
# print("nrows:", sheet.nrows)
# for index in range(2, sheet.nrows):
_data_list = sheet.row_values(1)
# print(_data_list)
# print(_data_list[2])

for i in range(20):
    # print(in_list[i])
    print(_data_list[in_list[i] + 2])

# # trans(2012)
# T_M = []
# for y in range(2010, 2017):
#     T_M.append(trans(y))

# tt = pd.DataFrame(columns=[i for i in range(1, 11)], data=T_M)
# tt.to_csv("M.csv", encoding='gbk')


# Percent; SCHOOL ENROLLMENT - Population 3 years and over enrolled in school - College or graduate school
def Create_Data(year, name):
    _year = year
    _year = str(_year)[2:]
    string = "part2_data/" + _year + ".xlsx"
    book = xlrd.open_workbook(string)
    # book_list.append(book)
    sheet = book.sheet_by_name("Sheet1")
    datalist = sheet.row_values(1)

    index2 = 0
    for i in range(len(datalist)):
        if datalist[i] == name:
            # print(i)
            index2 = i
    index2 = index2 - 2

    out = {year: ([], [])}
    # Test 2012
    test_X = []
    test_Y = []

    test_year = str(year)
    temp = np.array([])
    for numbering in labels[test_year]:
        # if labels["2012"][numbering] > 500:
        #     temp = np.append(temp, -1)
        # else:
        #     temp = np.append(temp, labels["2012"][numbering])
        temp = np.append(temp, labels[test_year][numbering])
        # test_Y.append()
        test_X.append(data_set[test_year][numbering])

    # t_m = temp.mean()
    # t_s2 = temp.var()
    # t_s = math.sqrt(t_s2)

    # for i in range(np.shape(temp)[0]):
    #     # print("!")
    #     temp[i] = (temp[i] - t_m) / t_s
    # cnt = 0
    # for i in range(np.shape(temp)[0]):
    #     if math.fabs(temp[i]-t_m) > 2.0 * t_s:
    #         # if math.fabs(temp[i]-t_m) > 1500:
    #         cnt = cnt + 1
    #         temp[i] = t_m
    # # print(cnt)
    test_Y = temp.tolist()
    # print(test_Y)

    for i in range(len(test_Y)):
        if test_Y[i] > 3000:
            test_Y[i] = 0

    # pca_test = PCA_hand()
    # X_trans, M = pca_test.transform(np.array(test_X), 1)
    # print(M)
    # _M = []
    # for ele in M:
    #     _M.append(ele[0])

    # print(_M)

    # X = []
    # for l in X_trans:
    #     X.append(l[0])
    # # print(X)
    # plt.figure()
    # plt.scatter(X, test_Y, color='r', s=10)
    # # plt.plot(X, test_Y)
    # # plt.plot(l_T, y_)
    # pic_name = "test_" + test_year + ".jpg"
    # plt.savefig(pic_name)

    for i in range(len(test_Y)):
        out[year][1].append(test_Y[i])
        out[year][0].append(test_X[i][index2])

    # print(out)
    return out


DD = {}

# name_ = "Percent; MARITAL STATUS - Females 15 years and over - Never married" 
# name = "Percent; MARITAL STATUS - Never married"
# name_ = "Percent; EDUCATIONAL ATTAINMENT - Percent bachelor's degree or higher"
name = "Percent; SCHOOL ENROLLMENT - Population" + \
    " 3 years and over enrolled in school - College or graduate school"
D_1 = Create_Data(
    2010, "Percent; SCHOOL ENROLLMENT - College or graduate school")
D_2 = Create_Data(
    2011, "Percent; SCHOOL ENROLLMENT - College or graduate school")
D_3 = Create_Data(
    2012, "Percent; SCHOOL ENROLLMENT - College or graduate school")
D_4 = Create_Data(2013, name)
D_5 = Create_Data(2014, name)
D_6 = Create_Data(2015, name)
D_7 = Create_Data(2016, name)


# D_1 = Create_Data(2010, name)
# D_2 = Create_Data(2011, name)
# D_3 = Create_Data(2012, name)
# D_4 = Create_Data(2013, name_)
# D_5 = Create_Data(2014, name_)
# D_6 = Create_Data(2015, name_)
# D_7 = Create_Data(2016, name_)


DD.update(D_1)
DD.update(D_2)
DD.update(D_3)
DD.update(D_4)
DD.update(D_5)
DD.update(D_6)
DD.update(D_7)

# book = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
# for sheet in book.sheets():
#     print(sheet.name)

# sheet_new = book.sheet_by_name("Data")
# print("nrows:", sheet_new.nrows)

# # {county: {year: num}}
# # dataset = {}
# numbering_list = []

# for i in range(sheet_new.nrows):
#     process_data = sheet_new.row_values(i)
#     if process_data[1] == "WV":
#         if process_data[5] not in numbering_list:
#             numbering_list.append(process_data[5])

# print(numbering_list)
# print(DD)

TT_D_X = []
TT_D_Y = []
# plt.figure()
for key in DD:
    # plt.scatter(X, test_Y, color='r', s=10)
    # plt.plot(X, test_Y)
    # plt.plot(l_T, y_)
    # plt.plot(DD[key][0], DD[key][1])
    # if key == 2013:
        # plt.scatter(DD[key][0], DD[key][1], s=2)

    for i in range(len(DD[key][0])):
        # TT_D_X.append(DD[key][0][i])
        # TT_D_Y.append(DD[key][1][i])
        if DD[key][0][i] > 37:
            if DD[key][1][i] > 500:
                DD[key][1][i] = 0

    plt.scatter(DD[key][0], DD[key][1], s=1)

    for i in range(len(DD[key][0])):
        TT_D_X.append(DD[key][0][i])
        TT_D_Y.append(DD[key][1][i])

pic_name = "test_result.jpg"
# plt.xlabel("Percent; SCHOOL ENROLLMENT - College or graduate school")
plt.xlabel(name)
plt.ylabel("Total Drug Reports County")

XXX = []
YYY = []
for r in range(199):
    Sum = 0
    cnt = 1
    for i in range(len(TT_D_X)):
        if TT_D_X[i] < r / 2 + 0.5 and TT_D_X[i] >= r / 2:
            Sum = Sum + TT_D_Y[i]
            cnt = cnt + 1

    Sum = Sum / cnt
    YYY.append(Sum)
    XXX.append(r / 2)

plt.plot(XXX, YYY)
plt.savefig(pic_name)
# print(TT_D_X)
