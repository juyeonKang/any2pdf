#!/usr/bin/python3

import base64
import sys
from urllib import request
from json import dumps

# 인자로 받은 파일 이름 읽어와서 열고 base64 encoding하기
FileName = sys.argv[1]
f = open(FileName,"rb").read()
Encode_f = str(base64.encodestring(f))

# json 생성(아직은 utf-8로 인코딩해야하는지 모르겠답)
dic = {"Parameters":[{"Name":"File","fileValue":{"Name":FileName,"Data":Encode_f}},{"Name":"PdfVersion","Value":"1.7"}]}
json = dumps(dic)

# url 생성
url = "https://v2.convertapi.com/ppt/to/pdf?Secret=syvSb4otJcH6y4v3&PdfVersion=1.7"

# POST로 request하기

#...근데 결과를 어떻게 받지..? 

