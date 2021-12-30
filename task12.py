from task1 import scrape_top_list
from bs4 import BeautifulSoup
import json
import requests
import pprint
scrap= scrape_top_list()
def movie_cast(movie):
    list1=[]
    # dict={}
    for i in movie:
        year=i["Movie Url"]
        # print(year)
    # list=[]
        data=requests.get(year)
        soup=BeautifulSoup(data.text,"html.parser")
        main=soup.find_all("div",class_="panel-body content_body")
        sec=main[1].find("div",class_="castSection")
    # # print(main)
        all=sec.find_all("div",class_="cast-item")
        list=[]
        dict={}
    # # print(all)
        for i in all:
            list.append(i.find("span")["title"])
            # dict["cast"]=list
        list1.append(list)
        # pprint.pprint(list1)
        with open("allCast.json","w") as file:
            json.dump(list1,file,indent=4)
        # print(list1)
    return list1
movie_cast(scrap)