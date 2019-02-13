import xlrd

book = xlrd.open_workbook("ProblemCData.xlsx")
for sheet in book.sheets():
    print(sheet.name)

sheet_new = book.sheet_by_name("msncodes")
print("nrows: ", sheet_new.nrows)

msn_dict = {}
for i in range(sheet_new.nrows):
    one_list = sheet_new.row_values(i)
    msn_dict.update({one_list[0]: one_list[2]})

def get_all_name(dictionary):

    list_all_name = []
    for key in dictionary:
        strL = dictionary[key]
        # print(strL)
        list_name = []
        list_temp = []
        for i in range(len(strL)):
            if strL[i] != " ":
                list_temp.append(strL[i])
                if i == (len(strL)-1):
                    # str_temp = str(list_temp)
                    str_temp = ""
                    for i in range(len(list_temp)):
                        str_temp = str_temp + list_temp[i]
                    list_name.append(str_temp)
                    break
            else:
                str_temp = ""
                for i in range(len(list_temp)):
                    str_temp = str_temp + list_temp[i]
                list_name.append(str_temp)
                list_temp.clear()
                if len(list_temp) != 0:
                    print("ERROR!")
        # print(list_name)
        for ele in list_name:
            list_all_name.append(ele)

    set_all_name = set(list_all_name)
    # print(set_all_name)
    # print("length all name: ", len(set_all_name))
    return set_all_name


list_all_name = []
for key in msn_dict:
    strL = msn_dict[key]
    # print(strL)
    list_name = []
    list_temp = []
    for i in range(len(strL)):
        if strL[i] != " ":
            list_temp.append(strL[i])
            if i == (len(strL)-1):
                # str_temp = str(list_temp)
                str_temp = ""
                for i in range(len(list_temp)):
                    str_temp = str_temp + list_temp[i]
                list_name.append(str_temp)
                break
        else:
            str_temp = ""
            for i in range(len(list_temp)):
                str_temp = str_temp + list_temp[i]
            list_name.append(str_temp)
            list_temp.clear()
            if len(list_temp) != 0:
                print("ERROR!")
    # print(list_name)
    for ele in list_name:
        list_all_name.append(ele)

set_all_name = set(list_all_name)
print(set_all_name)
print("length all name: ", len(set_all_name))


msn_dict = {}
for i in range(sheet_new.nrows):
    one_list = sheet_new.row_values(i)
    msn_dict.update({one_list[0]: one_list[2]})


def StringtoWords(strL):
    list_name = []
    list_temp = []
    for i in range(len(strL)):
        if strL[i] != " ":
            list_temp.append(strL[i])
            if i == (len(strL)-1):
                # str_temp = str(list_temp)
                str_temp = ""
                for i in range(len(list_temp)):
                    str_temp = str_temp + list_temp[i]
                list_name.append(str_temp)
                break
        else:
            str_temp = ""
            for i in range(len(list_temp)):
                str_temp = str_temp + list_temp[i]
            list_name.append(str_temp)
            list_temp.clear()
            if len(list_temp) != 0:
                print("ERROR!")

    return list_name

# print(StringtoWords("liuzhengxi is a students"))


def deleteKeyword(dictionary, keyword):
    copy_dict = dictionary.copy()
    for key in dictionary:
        str_input = dictionary[key]
        name_list = StringtoWords(str_input)
        if keyword in name_list:
            del copy_dict[key]

    return copy_dict


copy_dict = msn_dict.copy()
for key in msn_dict:
    str_input = msn_dict[key]
    name_list = StringtoWords(str_input)
    if "per" in name_list:
        del copy_dict[key]

# for key in copy_dict:
#     str_input = copy_dict[key]
#     name_list = StringtoWords(str_input)
#     print(name_list)

# print("length_copy: ", len(copy_dict))

copy_dict = deleteKeyword(copy_dict, "dollar")
copy_dict = deleteKeyword(copy_dict, "dollars")
copy_dict = deleteKeyword(copy_dict, "Dollars")
copy_dict = deleteKeyword(copy_dict, "kilowatthours")
copy_dict = deleteKeyword(copy_dict, "Btu")
copy_dict = deleteKeyword(copy_dict, "Percent")

print("length_copy: ", len(copy_dict))
dict_name = get_all_name(copy_dict)
print(dict_name)
