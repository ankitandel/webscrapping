from task1 import*
num=scrape_top_list()
import json
def group_by_year(movie):
    # print(scrape_top_list)
    years=[]
    for i in movie:
        year=i["Year"]
        
        if year not in years:
            years.append(year)
            print(years)
    movie_dic={i:[]for i in years}
    for i in movie:
        year=i["Year"]
        for z in movie_dic:
            if str(z)==str(year):
                movie_dic[z].append(i)
    with open("Ankita.json","w")as u:
        json.dump(movie_dic,u ,indent=4)
    return movie_dic
group_by_year(num)











