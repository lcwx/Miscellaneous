import xlrd
import xlwt
from geopy.geocoders import Nominatim
# from geopy.geocoders import Baidu


book = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
for sheet in book.sheets():
    print(sheet.name)

sheet_new = book.sheet_by_name("Data")
print("nrows:", sheet_new.nrows)


def func_Hu(state_name):
    output_data = {}

    med_list = ["Heroin", "Opium", "Codeine",
                "Morphine", "Opiates", "Thebaine"]
    for i in range(sheet_new.nrows):
        process_data = sheet_new.row_values(i)
        if (process_data[1] == state_name) and (process_data[6] not in med_list):
            if process_data[0] not in output_data.keys():
                output_data.update({process_data[0]: process_data[7]})
            else:
                output_data[process_data[0]
                            ] = output_data[process_data[0]] + process_data[7]

    print(output_data)
    return output_data


def func_He(state_name):
    output_data = {}

    med_list = ["Heroin"]
    for i in range(sheet_new.nrows):
        process_data = sheet_new.row_values(i)
        if (process_data[1] == state_name) and (process_data[6] in med_list):
            if process_data[0] not in output_data.keys():
                output_data.update({process_data[0]: process_data[7]})
            else:
                output_data[process_data[0]
                            ] = output_data[process_data[0]] + process_data[7]

    print(output_data)
    return output_data


StateName = {"VA": "Virginia", "OH": "Ohio",
             "PA": "Pennsylvania", "KY": "Kentucky", "WV": "West Virginia"}

geolocator = Nominatim()

# Read test
with open('LL.txt', 'r') as f:
    a = f.read()
    name_dict = eval(a)
    print(len(name_dict))
    # print(dict_name)


def getLL(state_name, county_name):
    str_name = county_name + ", " + StateName[state_name] + ", " + "USA"
    # location = geolocator.geocode(str_name)
    # la = location.latitude
    # lo = location.longitude
    la = name_dict[str_name][0]
    lo = name_dict[str_name][1]
    # print((la, lo))

    return (la, lo)


# func_Hu("VA")
# func_He("VA")
# print(getLL("WV", "BARBOUR"))

def getData(state_name, county_name, year, CM):
    if CM == "Hu":
        # Hu
        sum = 0
        med_list = ["Heroin", "Opium", "Codeine",
                    "Morphine", "Opiates", "Thebaine"]
        for i in range(sheet_new.nrows):
            process_data = sheet_new.row_values(i)
            T1 = (process_data[0] == year)
            T2 = (process_data[1] == state_name)
            T3 = (process_data[2] == county_name)
            if T1 and T2 and T3:
                if process_data[6] not in med_list:
                    sum = sum + process_data[7]

        # print(sum)
        return sum

    if CM == "He":
        # He
        sum = 0
        for i in range(sheet_new.nrows):
            process_data = sheet_new.row_values(i)
            T1 = (process_data[0] == year)
            T2 = (process_data[1] == state_name)
            T3 = (process_data[2] == county_name)
            if T1 and T2 and T3:
                if process_data[6] == "Heroin":
                    sum = sum + process_data[7]

        # print(sum)
        return sum


def end(year, CM, num):
    output_LL = {}
    output_N = {}

    cnt = 0
    # print(num)
    for i in range(sheet_new.nrows):
        process_data = sheet_new.row_values(i)
        if process_data[0] == year:
            str_name = process_data[1] + "_" + process_data[2]
            # print(str_name)
            if str_name in output_LL:
                pass
            else:
                output_LL.update(
                    {str_name: getLL(process_data[1], process_data[2])})
                cnt = cnt + 1
                # print(cnt)
                if cnt > num:
                    # print(cnt)
                    break

            if str_name in output_N:
                pass
            else:
                output_N.update(
                    {str_name: getData(process_data[1], process_data[2], year, CM)})

    # OL = output_LL.copy()
    # str_ = str(year) + ".txt"
    # str_ = "data_L" + "/" + str_
    # with open(str_, "w") as f:
    #     f.write(str(OL))

    # # Read test
    # with open('data/Heroin.txt', 'r') as f:
    #     a = f.read()
    #     dict_name = eval(a)
    #     # print(dict_name)

    return output_LL, output_N


def save(year, CM, num=10000000):
    # num = 10
    file = xlwt.Workbook(encoding='utf-8')
    sheet = file.add_sheet('Location_Num', cell_overwrite_ok=True)
    sheet.write(0, 0, "Latitude")
    sheet.write(0, 1, "Longitude")
    sheet.write(0, 2, "Data")

    output_LL, output_N = end(year, CM, num)
    # print(output_LL)
    # print(output_N)

    cnt = 1
    for key in output_N:
        # print(output_LL[key][0])
        # print(output_LL[key][1])
        # print(output_N[key])
        sheet.write(cnt, 0, output_LL[key][0])
        sheet.write(cnt, 1, output_LL[key][1])
        sheet.write(cnt, 2, output_N[key])
        cnt = cnt + 1

    name = "D/" + str(year) + CM + ".xls"
    file.save(name)


# save(2010.0, 30)
for N in ["He","Hu"]:
    for i in range(2010,2018):
        save(float(i), N)
