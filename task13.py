import json
import pprint
k=open("allCast.json")
m=json.load(k)
# print(m)
l=open("task5.json")
n=json.load(l)
# print(n)
def movie():
    list=[]
    dict={}
    list1=[]
    for i in m:
        # print(i)
        for j in n:
            # print(j)
            dict["cast"]=i
            # print(dict)
            list.append(dict)
        # print(list)
            list.append(j)
        # print(list)
    list1.append(list)
    file=open("allcast details.json","w")
    json.dump(list1,file,indent=2)
    return(n)
movie()