import json
def analyse_movies_directors():
    directors=open("task5.json")
    list=json.load(directors)
    print(list)

    list1=[]
    dic={}
    for i in list:
        if (i["Director:"])not in list1:
            list1.append(i["Director:"])
            print(list)
            dic={}
            list2=[]
            for g in list1:
                i=0
                count=0
                while i<len(list):
                    if g==list[i]["Director:"]:
                        count=count+1
                    i=i+1
                dic.update({g:count})
            list2.append(dic)
    with open("task7.json","w")as f:
        json.dump(list2,f,indent=2)
analyse_movies_directors()