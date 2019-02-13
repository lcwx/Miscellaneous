import xlrd
import numpy as np
import matplotlib.pyplot as plt

book = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
for sheet in book.sheets():
    print(sheet.name)

sheet_new = book.sheet_by_name("Data")
print("nrows:", sheet_new.nrows)

# {county: {year: num}}
# dataset = {}
numbering_list = []
numbering_dict = {}

for i in range(sheet_new.nrows):
    process_data = sheet_new.row_values(i)
    if process_data[1] == "PA":
        if process_data[5] not in numbering_list:
            numbering_list.append(process_data[5])
            numbering_dict.update({process_data[5]: process_data[2]})

print(numbering_list)

# data_set = {year: {county: number}}
data_set = {}


def drawPic(year):
    dataSet = {year: {}}

    y = str(year)
    name = "part2_data/" + y + ".xlsx"
    book = xlrd.open_workbook(name)
    sheet = book.sheet_by_name("Sheet1")

    index = 0
    P_D = sheet.row_values(1)
    if year >= 13:
        name_F = "Percent; SCHOOL ENROLLMENT - Population" + \
            " 3 years and over enrolled in school - College or graduate school"
        for i in range(len(P_D)):
            if P_D[i] == name_F:
                index = i
                # print(index)

    else:
        name_F = "Percent; SCHOOL ENROLLMENT - College or graduate school"
        for i in range(len(P_D)):
            if P_D[i] == name_F:
                index = i
                # print(index)

    for i in range(2, sheet.nrows):
        process_data = sheet.row_values(i)
        # print(process_data[0])
        N = int(process_data[0])
        N = str(N)
        if N in numbering_list:
            dataSet[year].update({N: process_data[index]})

    return dataSet


for year in range(10, 17):
    data_set.update(drawPic(year))

# print(data_set)


def draw(numbering):
    # for nI in n?umbering_list:

    y = []
    # y_np= np.array(y)
    # m = y_np.mean()
    # print(m)


    years = [year for year in range(10, 17)]
    for year in years:
        y.append(data_set[year][numbering])

    y_np= np.array(y)
    m = y_np.mean()
    print(m)

    plt.figure()
    plt.plot(years, y)
    plt.savefig("SP2/" + numbering_dict[numbering] + ".jpg")


def D():
    for numB in numbering_list:
        draw(numB)


D()
