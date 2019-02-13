import xlrd
from geopy.geocoders import Nominatim


StateName = {"VA": "Virginia", "OH": "Ohio",
             "PA": "Pennsylvania", "KY": "Kentucky", "WV": "West Virginia"}

book = xlrd.open_workbook("MCM_NFLIS_Data.xlsx")
# for sheet in book.sheets():
#     print(sheet.name)

sheet_new = book.sheet_by_name("Data")
# print("nrows:", sheet_new.nrows)

name = []
for i in range(1, sheet_new.nrows):
    process_data = sheet_new.row_values(i)
    string = process_data[2] + ", " + StateName[process_data[1]] + ", " + "USA"
    if string not in name:
        name.append(string)


# Read test
with open('LL.txt', 'r') as f:
    a = f.read()
    name_dict = eval(a)
    print(len(name_dict))
    # print(dict_name)


cnt = 0
# name_dict = {}
# print(name)
for N in name:
    if N not in name_dict:
        geolocator = Nominatim()
        location = geolocator.geocode(N)
        la = location.latitude
        lo = location.longitude
        # print(la)
        # print(lo)
        print((la, lo))
        name_dict.update({N: (la, lo)})
        with open("LL.txt", "w") as f:
            f.write(str(name_dict))
        cnt = cnt + 1
        if cnt > 1000:
            break

# with open("LL.txt", "w") as f:
#     f.write(str(name_dict))

# print(name_dict)