#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
------------------------------------
File Name:    Baidu_face
Author:    Mrtutu
Date:    2018/3/13
Description:
------------------------------------

"""

import requests
import base64
import cv2

cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("face1.jpg", frame)
        break
cap.release()
cv2.destroyAllWindows()

access_token = '24.3e1522524a295abf5d7db804f1ce0d5e.2592000.1523203768.282335-10893296'

request_url = "https://aip.baidubce.com/rest/2.0/face/v1/detect"

f = open('face1.jpg', 'rb').read()
img = base64.b64encode(f)

request_url = request_url+'?access_token='+ access_token

param = {
    "face_fields":"age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities",
    "image":img,
    "max_face_num":5
}

header = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
r = requests.post(request_url, data=param, headers=header)

s = str(r.json()['result'][0]['qualities']['type']['human'])
print('置信度为：'+ s)