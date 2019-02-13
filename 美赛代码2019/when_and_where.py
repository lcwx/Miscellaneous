import xlrd
# import xlwt
# import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt
# from geopy.geocoders import Nominatim
# from geopy.geocoders import Baidu


book = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
for sheet in book.sheets():
    print(sheet.name)

sheet_new = book.sheet_by_name("Data")
print("nrows:", sheet_new.nrows)

# {county: {year: num}}
dataset = {}

for i in range(sheet_new.nrows):
    process_data = sheet_new.row_values(i)
    # print(process_data)
    if process_data[1] == "VA" and process_data[6] == "Heroin":
        if process_data[2] not in dataset:
            dataset.update(
                {process_data[2]: {process_data[0]: process_data[7]}})
        else:
            dataset[process_data[2]].update({process_data[0]: process_data[7]})

# for key in dataset:
    # print(dataset[key])

county_list = []
data_set = []
for key in dataset:
    county_list.append(key)
    year_data = []
    for year in range(2010, 2018):
        year = float(year)
        if year in dataset[key]:
            year_data.append(dataset[key][year])
        else:
            year_data.append(0)
    data_set.append(year_data)

# for c_n in county_list:


def drawPic(county_name):
    reg = linear_model.LinearRegression()
    # reg.fit()

    plt.figure()
    plt.xlabel("Year")
    plt.ylabel("Drug Reports")
    plt.title(county_name)

    index = 0
    for ind in range(len(county_list)):
        if county_list[ind] == county_name:
            index = ind
            break
    Y = data_set[index]
    X = [year for year in range(2010, 2018)]

    # d_s = []
    # for i in range(len(X)):
    #     pair = [X[i],Y[i]]
    #     d_s.append(pair)
    x_ = []
    for i in range(len(X)):
        x_.append([X[i]])
    reg.fit(x_, Y)
    y_ = reg.predict(x_)
    # D_C_N = []
    ifS = False

    OO = ""

    if reg.predict([[2019]])[0] > 36:
        # print(county_name)
        # D_C_N.append(county_name)
        if Y[7] <= 36:
            ifS = True
            OO = "2019"

    if reg.predict([[2019]])[0] <= 36 and reg.predict([[2020]])[0] > 36:
        # print(county_name)
        # D_C_N.append(county_name)
        if Y[7] <= 36:
            ifS = True
            OO = "2020"

    plt.plot(X, Y)
    plt.plot(X, y_)

    pic_name = "CCN/" + county_name + ".jpg"
    picname = county_name + OO + ".jpg"
    plt.savefig(pic_name)
    if ifS:
        plt.savefig(picname)


# drawPic("STAUNTON CITY")
for cn in county_list:
    drawPic(cn)
