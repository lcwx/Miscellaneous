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
            # print(temp_l)
            output_data.append(temp_l)

    return output_data


output_data = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print(sepP(output_data))


# from geopy.geocoders import Nominatim
# import urllib
# import xlrd
# import xlwt
# from urllib.request import urlopen
# import json
# state = 'Virginia'
# data = xlrd.open_workbook('MCM_NFLIS_Data.xlsx')
# table = data.sheets()[2]
# nrows = table.nrows
# address_list = []
# num_list = []
# count = 0
# # print(table.row(10)[1].value)
# for i in range(nrows):
#     # print(i)
#     if table.row(i)[2].value not in address_list:
#         address_list.append(table.row(i)[2].value)
#         num_list.append(table.row(i)[8].value)
# f = xlwt.Workbook(encoding='utf-8')
# sheet1 = f.add_sheet('学生', cell_overwrite_ok=True)
# for j in range(len(address_list)):
#     try:
#         geolocator = Nominatim()
#         location = geolocator.geocode(address_list[j])
#         if state not in location:
#             address_list[j] = address_list[j]+','+state+',USA'
#             location = geolocator.geocode(address_list[j])
#         # print(location.address)
#         #print((location.latitude, location.longitude))
#     except:
#         count = count+1
#         continue
#     else:
#         sheet1.write(j, 1, location.address)
#         sheet1.write(j, 2, location.latitude)
#         sheet1.write(j, 3, location.longitude)
#         sheet1.write(j, 4, num_list[j])
#     print(j)
# f.save("res.xls")
