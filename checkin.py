import os
import json
import requests

r = requests.session()
loginData = {"email":"","passwd":""}
loginRes = r.post("https://sockboom.lol/auth/login",data=loginData)

try:
    loginResJson = json.loads(loginRes.text)
    if loginResJson['ret'] == 1:
        print("success login")
except:
    print("fail login")
    raise

checkinRes = r.post('https://sockboom.lol/user/checkin')

try:
    checkinResJson = json.loads(checkinRes.text)
    assert checkinResJson['ret'] == 1
    print("success checkin")
    print(checkinResJson['msg'])
except:
    print("fail checkin")
    raise

logout = r.get("https://sockboom.lol/user/logout")
os.system ("pause") 