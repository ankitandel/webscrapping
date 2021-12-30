from bs4 import BeautifulSoup
import requests
import json
def scrape_movie_details(movie_url):
    page=requests.get(movie_url)
    soup=BeautifulSoup(page.text,"html.parser")
    title_div=soup.find("ul",class_="content-meta info")
    sub_title_div=title_div.find_all("li",class_="meta-row clearfix")

    movie_dic={}
    name=soup.find("h1",class_="scoreboard__title").get_text()
    movie_dic.update({"Movie Name":name})
    for i in sub_title_div:
        key=i.find("div",class_="meta-label subtle").get_text()
        # print(key)
        value=(i.find("div",class_="meta-value").text.replace(" ","").replace("\n","").strip())
        # print(value)
        movie_dic.update({key:value})
    with open("task4.json","w")as file:
        json.dump(movie_dic,file,indent=2)

scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")

