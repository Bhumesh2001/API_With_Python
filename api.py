

import json,requests
from pprint import pprint

r = requests.get('https://saral.navgurukul.org/api/courses')
with open("courses.json","w") as l:
    json.dump(r.json(),l,indent=4)
with open("courses.json","r") as m:
    j = json.load(m)
    c = 0
    for i in j:
        for k in j[i]:
            c+=1
            print(c,k["name"])
d = {}
with open("courses.json","r") as m:
    j = json.load(m)
    c = 0
    for i in j:
        for k in j[i]:
            c+=1
            d.update({c:k["id"]})
print()
n = int(input("select your course : "))
if n in d:
    for j in d:
        if n == j:
            rs = requests.get("http://saral.navgurukul.org/api/courses/"+d[j]+"/exercises")
            print("id = ",d[j])
else:
    print("your course number does not exist")


d ={}
d1 = {}
r = requests.get("http://saral.navgurukul.org/api/courses/74/exercises").json()
with open("slug.json","w") as su:
    json.dump(r,su,indent=6)
with open("slug.json","r") as obj1:
    l = json.load(obj1)
    b = 0
    for j in l:
        for i in l[j]:
            b += 1
            d.update({b:i["slug"]})
            print(b,".",i["id"])
n = int(input("enter your id number: "))
if n in d:
    for j in d:
        if n == j:
            print("slug = ",d[j])
else:
    print("your id does not exist")


Q.5

import requests,json
from pprint import pprint
url = "http://saral.navgurukul.org/api/courses"
re = requests.get(url)
b=re.json()
list1=[]
list2=[]
for i in b:
    k=1
    for j in b[i]:
        hh=str(k)+". "+j["name"]
        k+=1
        list1.append(hh)
        list2.append(j["id"])
        print(hh)
pp = int(input("enter input - select your course    :     "))
pp = -1
ids = list2[pp]
req = requests.get("http://saral.navgurukul.org/api/courses/"+ids+"/exercises")
w = req.text
war = json.loads(w)
data_d = war["data"]
num = 1
list3 = []
for j in data_d:
    int_slugs="http://saral.navgurukul.org/api/courses/"+(ids)+"/exercise/getBySlug?slug="+j['slug']
    v = str(num)
    dr= v+"."+j['name']
    num=int(num)
    print (dr)
    dict = {v:int_slugs}
    list3.append(dict)
    j=j['childExercises']
    num1=1
    for k in j:
        z=str(num)+'.'+str(num1)
        print('          '+z, k['name']  )
        float_slugs="http://saral.navgurukul.org/api/courses/"+(ids)+"/exercise/getBySlug?slug="+k['slug']
        dic={z:float_slugs}
        list3.append(dic)
        num1+=1
    num+=1
k = (input("enter the question no    :  "))
for h in (list3):
    for j,f in h.items():
        if str(j) == k:
            s = requests.get(f).text
            d = json.loads(s)
            hh = d["content"]
            bb = json.loads(hh)
            for u in bb:
                print(json.loads(u)["value"])
