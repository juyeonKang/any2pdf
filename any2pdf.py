#!/usr/bin/python3

import base64
import sys
from urllib import request
from json import dumps,loads

# 인자로 받은 파일 이름 읽어와서 열고 base64 encoding하기
FileName = sys.argv[1]
fname = FileName.split('.')[0]
fform = FileName.split('.')[1]
f = open(FileName,"rb").read()
Encode_f = base64.encodestring(f)

# json 생성(아직은 utf-8로 인코딩해야하는지 모르겠답)
dic = {
    "Parameters":[
        {
            "Name":"File",
            "fileValue":{
                "Name":FileName,
                "Data": "%s"
            }
        },
        {
            "Name":"PdfVersion",
            "Value":"1.7"
        }
    ]
}
data = dumps(dic).encode('ascii') % Encode_f 

# url 생성
url = "https://v2.convertapi.com/" + fform + "/to/pdf?Secret=syvSb4otJcH6y4v3&PdfVersion=1.7"

# request header
headers = {'Content-type' : 'application/json'}

# POST로 request하고, response 받기
req = request.Request(url, data=data, headers=headers)
res = request.urlopen(req)

# response로 받은 pdf 데이터 디코딩해서 파일로 저장
tmp = res.read().decode('utf-8')
data = loads(tmp)
encoded = data['Files'][0]['FileData'].encode('utf-8')
decoded = base64.decodestring(encoded)

f = open(fname+".pdf", 'wb')
f.write(decoded)
f.close()


