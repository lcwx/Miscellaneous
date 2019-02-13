import xlrd

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
print("length: ",len(dict_CA))

dict_AZ = preprocess("AZ")
print("length: ",len(dict_AZ))

dict_NM = preprocess("NM")
print("length: ",len(dict_NM))

dict_TX = preprocess("TX")
print("length: ",len(dict_TX))