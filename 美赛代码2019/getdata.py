import xlrd

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


def total_data(med_name, data_list):
    # file_name = "data/"+ med_name + ".txt"
    # with open(file_name,"r") as f:
        # temp = f.read()
        # _dict = eval(temp)

    # Year = [2010.0,2011.0,2012.0,2013.0,2014.0,2015.0,2016.0,2017.0]
    Year = [float(i) for i in range(2010, 2018)]
    StateName = ["VA", "OH", "PA", "KY", "WV"]
    output_data = {}
    _data_list = {}
    for year in Year:
        temp_list = []
        for j in range(len(data_list)):
            # print(year)
            # print(data_list[j][0])
            if data_list[j][0] == year:
                temp_list.append(data_list[j])

        _data_list.update({year: temp_list})

    # print(_data_list)
    for key in _data_list:
        output_data.update({key: {}})
        datalist = _data_list[key]
        # print(data_list)
        State_Name = StateName.copy()
        for i in range(len(datalist)):
            if (med_name == datalist[i][6]) and (datalist[i][1] == State_Name[0]):
                # print("!")
                output_data[key].update({State_Name[0]: datalist[i][9]})
                State_Name.remove(State_Name[0])
                if len(State_Name) == 0:
                    break

    print(output_data)
    return output_data


total_data("Heroin", data_list)
