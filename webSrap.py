from bs4 import  BeautifulSoup
import requests

url="https://www.cricbuzz.com/cricket-match/live-scores"

response=requests.get(url)

data =response.text

soup=BeautifulSoup(data,'html.parser')

blocks=soup.find_all("div",{"class":"cb-col cb-col-100 cb-lv-main"})

for block in blocks:
    #Shows the headline of the match
    headline_tag=block.find("h2")
    #the below if else statements is to avoid if any of the value in a certain tag is empty
    if headline_tag:
        headline=headline_tag.text
    else:
        pass

    title_tag=block.find("a",{"class":"text-hvr-underline text-bold"})

    if title_tag:
        title=title_tag.text
    else:
        pass
    match_no_tag=block.find("span",{"class":"text-gray"})

    if match_no_tag:
        match_no=match_no_tag.text
    else:
        pass



    print(headline,"\n",title,"\n",match_no,"\n")
