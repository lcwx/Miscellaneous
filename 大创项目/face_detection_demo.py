# encoding:utf-8
import urllib.request

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/' + \
    'token?grant_type=client_credentials&client_id=' + \
    'RHRpebbdKKyeMwGbrgFgZobB&client_secret=mjtUvxV7p3Ou9tk8rafKBgnQfuHteN6S'
request = urllib.request.Request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
content = content.decode("utf-8")
content = eval(content)
# if (content):
#     print(content.keys())

'''
人脸检测与属性分析
'''

request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

import base64

with open("test.jpg", "rb") as f:
    # print("###############################")
    # print(f.read())
    ls_f = base64.b64encode(f.read())
    # print(ls_f)
# print(type(ls_f))

image = ls_f
# params = "{\"image\":,\"image_type\": \"FACE_TOKEN\", \"face_field\": \"faceshape, facetype\"}"
params = {"image": image,"image_type":"BASE64","face_field":"faceshape,facetype"}
# print(params)
# params = str(params)
params = urllib.parse.urlencode(params).encode('utf-8')
# params = "{\"image\":\"https://raw.githubusercontent.com/xcmyz/Netural-Language-Process/master/chatbot_AIML/chatbot.JPG\",\"image_type\":\"URL\"}"
# print(params["image"])

# access_token = '[调用鉴权接口获取的token]'
access_token = content["access_token"]
# print("udfhsdfkfhsdkfhksdjhksdhfiuhwiehsklfcsdb")
# access_token = access_token.encode("utf-8")
# print(access_token)
# print("ghcsdifisdhfouhsdohfodshfodsf")
request_url = request_url + "?access_token=" + access_token
request = urllib.request.Request(url=request_url, data=params)
# print("#################################")
request.add_header('Content-Type', 'application/json')
# print("#####################")
# print(type(request))
response = urllib.request.urlopen(request)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
content_ = response.read()
content_ = content_.decode("utf-8")
content_ = eval(content_)
# print(format(content_))
if content_:
    print(content_)


# from aip import AipFace
# import base64
# # import cv2
# from urllib.parse import urlencode

# with open("test.JPG", "rb") as f:
#     ls_f = base64.b64encode(f.read())
#     ls_f = urlencode(ls_f)
# # print(type(ls_f))
# print(ls_f)
# # im = cv2.imread("test.JPG")


# APP_ID = '14913576'
# API_KEY = 'RHRpebbdKKyeMwGbrgFgZobB'
# SECRET_KEY = 'mjtUvxV7p3Ou9tk8rafKBgnQfuHteN6S'

# client = AipFace(APP_ID, API_KEY, SECRET_KEY)


# # image = "取决于image_type参数，传入BASE64字符串或URL字符串或FACE_TOKEN字符串"
# image = str(ls_f)

# imageType = "BASE64"

# """ 调用人脸检测 """
# out = client.detect(image, imageType)
# print(out)

# # """ 如果有可选参数 """
# # options = {}
# # options["face_field"] = "age"
# # options["max_face_num"] = 2
# # options["face_type"] = "LIVE"

# # """ 带参数调用人脸检测 """
# # client.detect(image, imageType, options)
