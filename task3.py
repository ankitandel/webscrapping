from task2 import*
year=group_by_year(num)
import json
def group_by_decade(movie):
    moviedec={}
    list1=[]
    for index in movie:
        m=index%10
        decade=index-m
        if decade not in list1:
            list1.append(decade)
    # print(list)
    list1.sort()
    # print(list)
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movie:
            if x<=dec10 and x>=i:
                for v in movie[x]:
                    moviedec[i].append(v)
    with open("task3.json","w")as u:
        json.dump(moviedec,u,indent=4)
    return(moviedec)
group_by_decade(year)
