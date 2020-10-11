# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import fileinput
import json

biglist=[]
id = 1
quest = 0
url =[]
url2 =[]

track1=[
    'Getting Started: Create and Manage Cloud Resources',
    'Perform Foundational Infrastructure Tasks in Google Cloud',
    'Set up and Configure a Cloud Environment in Google Cloud',
    'Deploy and Manage Cloud Environments with Google Cloud',
    'Build and Secure Networks in Google Cloud',
    'Deploy to Kubernetes in Google Cloud'
    ]
track2 = [
    'Getting Started: Create and Manage Cloud Resources',
    'Integrate with Machine Learning APIs',
    'Perform Foundational Data, ML, and AI Tasks in Google Cloud',
    'Explore Machine Learning Models with Explainable AI',
    'Engineer Data in Google Cloud',
    'Insights from Data with BigQuery',
    'Google Cloud Essentials'
    ]
#get the url in list


with fileinput.input(files=('userurl.txt')) as f:
    for line in f:
        url.append(line.replace("\n", ""))
for ele in url:
    if ele.strip():
        url2.append(ele)
    # Connect to the URL

for link in url2:
    tempdic = {}
    response = requests.get(link)
    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")
    #print(soup.prettify())

    """
    title = soup.find('title')
    x = title.string.split(" |")
    #print(x[0])
    bigdic[id]['name'] = x[0]
    x=soup.find_all("p", "public-profile__hero__details l-mbm")
    y = x[0]
    z = ""
    for element in y:
        z += element
    tlabno = z.split("\n")
    bigdic[id]['noofquest'] = tlabno[4]
    """

    track1completed = []
    track2completed = []
    profile = soup.findAll('div', attrs = {'class':'public-profile__hero'})[0]
    dp = profile.img['src']
    name = profile.h1.text
    tempdic['name'] = name.strip()
    tempdic['dp'] = dp
    tempdic['qlabid'] = link
    quests = soup.findAll('div', attrs = {'class':'public-profile__badges'})
    for row in quests[0].findAll('div', attrs = {'class':'public-profile__badge'}):
        divs = row.findChildren("div" , recursive=False)
        if divs[1].text.strip() in track1:
            track1completed.append(divs[1].text.strip())
        if divs[1].text.strip() in track2:
            track2completed.append(divs[1].text.strip())
    tempdic['track1'] = track1completed
    tempdic['track2'] = track2completed
    tempdic['qcomplete_no'] = len(track1completed) + len(track2completed)
    print(id," ",tempdic['name']," ",tempdic['qcomplete_no']," ",tempdic['track1']," ",tempdic['track2'])
    id+=1
    biglist.append(tempdic)

print(biglist)

#print("The original dictionary : " + str(biglist))
print("\n")

res = sorted(biglist, key = lambda x: x['qcomplete_no'], reverse=True)
#print("The sorted dictionary by marks is : " + str(res))

with open('finallist.txt', 'w') as f:
    print(biglist, file=f)
with open('sortedfinallist.txt', 'w') as f:
    print(res, file=f)
with open("my.json","w") as f:
    json.dump(res,f)

f.close()
