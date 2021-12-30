from  task1 import scrape_top_list
import json
import requests
from bs4 import BeautifulSoup
import pprint
num=scrape_top_list()
def get_movie_list_detail(movie):
    i=0
    years=[]
    while i<len(movie):
        # print(i)
        # i=i+1
        # year=movie[i]["url"]
        year=movie[i]["Movie Url"]
        k=year
        # print(k)
        # i=i+1
        p=requests.get(k)
        # print(p)                                                                                                                                                                                                                  
        soup=BeautifulSoup(p.text,"html.parser")
        movie_detail=soup.find("ul",class_="content-meta info")      
        movie_find=movie_detail.find_all("li",class_="meta-row clearfix")
        # print(movie_find)
        data={}
        for k in movie_find:
        #     print(i)
            data[k.find("div",class_="meta-label subtle").text.strip()]=k.find("div",class_="meta-value").text.strip()
        years.append(data)
        i=i+1
        #     pprint.pprint(list)
        with open("task5.json","w") as f:
           json.dump(years,f,indent=4)
        pprint.pprint(years)
get_movie_list_detail(num)

