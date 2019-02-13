import xlrd
import csv
import matplotlib.pyplot as plt
import numpy as np

book = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
for sheet in book.sheets():
    print(sheet.name)

sheet_new = book.sheet_by_name("Data")
print("nrows:", sheet_new.nrows)

data_list = []
list_name = []
for i in range(sheet_new.nrows):
    process_data = sheet_new.row_values(i)
    # print(type(process_data))
    # print(process_data[6])
    list_name.append(process_data[6])
    data_list.append(sheet_new.row_values(i))

set_name = set(list_name)
# print(set_name)
print("length:", len(set_name))

# headers = ["name"]
# rows = []
# for key in set_name:
#     # print(key)
#     rows.append([key])

# print(rows)

# with open('med_name.csv','w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerow(headers)
#     f_csv.writerows(rows)


def get_med_data(med_name, data):
    # dict
    # key is the numbering of county
    # {year: {numbering: {'DR': num, 'name': str}}}

    output_data = {}

    for in1 in range(len(data)):
        if data[in1][1] == np.NaN:
            print("ERROER!")
        if data[in1][2] == np.NaN:
            print("ERROER!")
        if data[in1][5] == np.NaN:
            print("ERROER!")
        if data[in1][7] == np.NaN:
            print("ERROER!")
        if data[in1][6] == np.NaN:
            print("ERROER!")
        if data[in1][0] == np.NaN:
            print("ERROER!")

        if data[in1][0] not in output_data.keys():
            if data[in1][6] == med_name:
                uD = {data[in1][5]: {"DR": data[in1][7],
                                     "name": data[in1][1]+"_"+data[in1][2]}}
                output_data.update({data[in1][0]: uD})
        else:
            if data[in1][6] == med_name:
                _uD = {data[in1][5]: {"DR": data[in1][7],
                                      "name": data[in1][1]+"_"+data[in1][2]}}
                output_data[data[in1][0]].update(_uD)
                # print(uD)

    return output_data


# test_data = get_med_data("Heroin", data_list)
# print(test_data)

for key in set_name:
    part_data = get_med_data(key, data_list)

    # for in2 in range(len(key)):
    #     if key[in2] == '/':
    #         # print(key[in2])
    #         key[in2] = '_'
    key = str(key)
    key = key.replace('/', '_')
    # print(key)

    str_ = key + ".txt"
    str_ = "data/" + str_
    with open(str_, "w") as f:
        f.write(str(part_data))

# Read test
with open('data/Heroin.txt', 'r') as f:
    a = f.read()
    dict_name = eval(a)
    # print(dict_name)


# # save
# dict_name = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
# f = open('temp.txt', 'w')
# f.write(str(dict_name))
# f.close()

# # read
# f = open('temp.txt', 'r')
# a = f.read()
# dict_name = eval(a)
# print(dict_name)

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
            if process_data[2] == key:
                num = process_data[5]
                break

        CN_dict.update({key: num})

    # print(CN_dict)
    CN_all.update({N: CN_dict})


def printCN(state_name, data_list):
    out = []

    for i in range(len(data_list)):
        if state_name == data_list[i][1]:
            # print(data_list[i][2])
            out.append(data_list[i][2])

    out = set(out)
    return out


CN_VA = printCN("VA", data_list)
print(len(CN_VA))
if "AMELIA" in CN_VA:
    print("GOT!")

CN_PA = printCN("PA", data_list)
print(len(CN_PA))


def drawPic(name_state, name_county, name_med, CN_dict):
    # Read data
    filename = "data/" + name_med + ".txt"
    with open(filename, 'r') as f:
        temp = f.read()
        dict_Med = eval(temp)
        # print(dict_name)

    X = [i for i in range(2010, 2018)]
    Y = []

    for year in X:
        numbering = CN_dict[name_state][name_county]
        # print(numbering)
        if year not in dict_Med.keys():
            Y.append(0)
        else:
            num = dict_Med[year][numbering]["DR"]
            # print(num)
            Y.append(num)

    # print(Y)
    plt.figure()
    plt.plot(X, Y)
    pic_name = "Pic/" + \
        dict_Med[year][CN_dict[name_state][name_county]]["name"] + ".jpg"
    plt.savefig(pic_name)


drawPic("OH", "ADAMS", "Heroin", CN_all)
