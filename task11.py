# import json
# def analyse_movies_language():
#     language_list=open("task5.json")
#     list=json.load(language_list)
#     print(list)
#     list1=[]
#     dic={}
#     for i in list:
#         a=i[ "Genre:"].split()
#         if (a)not in list1:
#             list1.append(a)
#             # print(list)
#             dic={}
#             list2=[]
#             for g in list1:
#                 i=0
#                 count=0
#                 while i<len(list):
#                     if g==list[i][ "Genre:"]:
#                         count=count+1
#                     i=i+1
#                 dic.update({g:count})
#             list2.append(dic)
#     with open("task11.json","w")as f:
#         json.dump(list2,f,indent=2)
# analyse_movies_language()

import json

file=open("task5.json","r")
var=json.load(file)

def get_lang_count(var):
    list1=[]
    list2=[]

    for i in var:
        file1=i["Genre:"].split()

        print(file1)
        for j in file1:
            if j[-1]==",":
                j=j[:-1]
        list2.append(j)
    for i in list2:
        if i not in list1:
            list1.append(i)

    dict={}
    for l in list1:
        count=0
        h=0
        while h <len(list2):
            if l==list2[h]:
                count+=1
            h+=1
        dict.update({l:count})

    with open("task11.json","w") as file:
        json.dump(dict,file,indent=4)

get_lang_count(var)