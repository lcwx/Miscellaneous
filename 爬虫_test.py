from selenium import webdriver
import csv

url = "http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"

print("###########################")
driver = webdriver.PhantomJS()
print("682847128746128")
# csv_file = open("playerlist.csv", "w", newline="")
# # print("@@@@@@@@@@@@@@@")
# writer = csv.writer(csv_file)
# writer.writerow(["标题", "播放数", "链接"])

# while url != "javascript:void(0)":
#     driver.get(url)

#     # print("hciewcierhiveihvirevibvi")
#     driver.switch_to.frame("contentFrame")
#     # print("@@@@@@@@@@@@@@@@@@@@@@@@")

#     data = driver.find_element_by_id(
#         "m-pl-container").find_elements_by_tag_name("li")

#     print("####################################")
#     # print("ijdwnidj")
#     for i in range(len(data)):
#         nb = data[i].find_element_by_class_name("nb").text
#         if '万' in nb and int(nb.split("万")[0]) > 500:
#             msk = data[i].find_element_by_css_selector("a.msk")

#             writer.writerow([msk.get_attribute("title"),
#                              nb, msk.get_attribute("href")])

#     url = driver.find_element_by_css_selector(
#         "a.zbtn.znxt").get_attribute("href")

# csv_file.close()
