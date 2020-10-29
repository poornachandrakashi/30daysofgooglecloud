import requests
import time
from bs4 import BeautifulSoup
import fileinput
import json
import concurrent.futures
biglist=[]

url =['https://google.qwiklabs.com/public_profiles/52fe0424-18fd-4092-b843-74ed8cb3ffe3',
'https://google.qwiklabs.com/public_profiles/fbd643b1-6d03-48aa-a198-ee6cc1a7c480',
'https://google.qwiklabs.com/public_profiles/ef03e379-25b9-4253-bab1-fdbb31c09422',
'https://www.qwiklabs.com/public_profiles/35f08d39-e615-4a99-ae92-8e5e99e22b63',
'https://www.qwiklabs.com/public_profiles/8c8a556f-243d-46b5-a9a8-0a96e739edbc',
'https://google.qwiklabs.com/public_profiles/bc46dbd7-491b-4268-a8c8-bc93623c61cb',
'https://google.qwiklabs.com/public_profiles/9cfd3da9-c42e-48e6-9d72-248c57aefea0',
'https://www.qwiklabs.com/public_profiles/9ec6a96a-7531-48f8-94cb-55e7bb549080',
'https://google.qwiklabs.com/public_profiles/c6eff4f8-6420-4237-adfc-342e9e3fc810',
'https://google.qwiklabs.com/public_profiles/c8fab27b-75fb-4466-94c8-8c58665f7299',
'https://www.qwiklabs.com/public_profiles/dc7a11e4-6082-48c4-a026-1b6c5cddcd7e',
'https://google.qwiklabs.com/public_profiles/135efd24-dd52-47e2-ad4e-9736f86ec0ab',
'https://www.qwiklabs.com/public_profiles/698247bc-a4d0-4125-9c39-f9cacab270b7',
'https://google.qwiklabs.com/public_profiles/9066b48f-86ea-486f-9674-f965d454f897',
'https://google.qwiklabs.com/public_profiles/c4dcfba4-b3c8-4c4f-a8e2-89e9e99b7a63',
'https://www.qwiklabs.com/public_profiles/3da12567-ceff-470e-b038-1df5a59410ab',
'https://www.qwiklabs.com/public_profiles/e2d4bdbc-c3db-47cf-8810-9431c9489a2f',
'https://www.qwiklabs.com/public_profiles/8cfbcf80-de0e-40e7-b721-67903fecf127',
'https://google.qwiklabs.com/public_profiles/10dfa346-a03a-4047-8a2a-2550c39e8441',
'https://www.qwiklabs.com/public_profiles/94f95a09-3c39-49bc-866a-b5572dfee796',
'https://www.qwiklabs.com/public_profiles/71574ae7-99c9-419e-a6be-1f0e77be16b7',
'https://google.qwiklabs.com/public_profiles/6efca9b3-5127-460e-8f73-5e586620c1d9',
'https://www.qwiklabs.com/public_profiles/4ad9010e-07e8-48bf-ad95-197080361905',
'https://www.qwiklabs.com/public_profiles/efc42f1c-67d7-4075-96ba-744594f8aab0',
'https://google.qwiklabs.com/public_profiles/fdfb64f0-bfc5-4118-bd68-e0db731dd1b7',
'https://www.qwiklabs.com/public_profiles/5ced2470-1c6a-4b71-825d-6109c674b0be',
'https://google.qwiklabs.com/public_profiles/c875c2e8-0fe8-4337-85d4-219161c9cd51',
'https://www.qwiklabs.com/public_profiles/7e31647c-bcd8-489a-8072-e11609303922',
'https://google.qwiklabs.com/public_profiles/a4768e3f-a42a-4fd8-adf7-b6913f5e9203',
'https://google.qwiklabs.com/public_profiles/b2129487-a64d-41a1-ad12-bea3efe93fb1',
'https://www.qwiklabs.com/public_profiles/72c269cd-b9f7-4577-8935-fe15ec3b1a15',
'https://www.qwiklabs.com/public_profiles/c709535e-f431-4695-a01b-8a7c9fc9eeb7',
'https://www.qwiklabs.com/public_profiles/11600392-9c85-4cd0-b112-f4886abd09f0',
'https://google.qwiklabs.com/public_profiles/da26458e-d9eb-4b43-8ca2-18edf973f743',
'https://www.qwiklabs.com/public_profiles/dcb5e591-b351-4827-99fa-e270c708b127',
'https://www.qwiklabs.com/public_profiles/368db6dd-a76c-4c91-96cf-8d7c28d9123b',
'https://google.qwiklabs.com/public_profiles/0813c527-291e-42db-a0dc-5bff7efc6324',
'https://www.qwiklabs.com/public_profiles/1899366c-4f9a-4dd1-917b-bf876937e15e',
'https://www.qwiklabs.com/public_profiles/5a7aff7f-5c17-4583-9aae-1ff27d36db53',
'https://www.qwiklabs.com/public_profiles/a7c227a7-83f1-4c24-9840-43877b64a3c1',
'https://www.qwiklabs.com/public_profiles/2e9f0d13-4015-4e87-b72a-f0ad26e68acb',
'https://www.qwiklabs.com/public_profiles/216f1759-7ae0-4a84-89f1-e2afd6a6525b',
'https://www.qwiklabs.com/public_profiles/5b8b4242-b9a5-4070-95f6-04aa12bc136f',
'https://www.qwiklabs.com/public_profiles/dd1d8396-f84f-4daf-8350-44935a33db38',
'https://google.qwiklabs.com/public_profiles/d749922d-ae24-43ec-9112-e9aa15be98e6',
'https://google.qwiklabs.com/public_profiles/8bc90472-814d-4fc2-968d-4d18036dd31a',
'https://www.qwiklabs.com/public_profiles/4668b25a-0c1d-44e1-8452-7f34e4624fcc',
'https://www.qwiklabs.com/public_profiles/1920eb64-0c95-495a-8c75-6ff955bad459',
'https://www.qwiklabs.com/public_profiles/08f6e85f-52fa-42fc-9bca-3f317bf24b87',
'https://google.qwiklabs.com/public_profiles/b9fe88da-6f33-452f-b5eb-e033f9e2ae09',
'https://google.qwiklabs.com/public_profiles/2e137432-c22e-4a28-8b91-9a305ec1b344',
'https://www.qwiklabs.com/public_profiles/9952071c-4db2-45c5-b1fb-820710dccc22',
'https://www.qwiklabs.com/public_profiles/0b7d9990-0bdd-4f66-9905-53182e340241',
'https://www.qwiklabs.com/public_profiles/352202e6-7e87-49a4-a928-52549ff4fa59',
'https://www.qwiklabs.com/public_profiles/d8081279-89fe-4973-af75-8f9e8c07fe1c',
'https://google-run.qwiklabs.com/public_profiles/7d2adf0d-0970-4e96-9d62-0365fa31a995',
'https://google.qwiklabs.com/public_profiles/22b6299c-c1b7-418c-a0d8-20ea1377b8c9',
'https://www.qwiklabs.com/public_profiles/4c6fd16e-2f6e-4c66-be9c-9f39d315e383',
'https://google.qwiklabs.com/public_profiles/5f0e95d3-9fdf-4227-a843-23a9b76302cc',
'https://www.qwiklabs.com/public_profiles/d9b28fa3-f3c7-4bca-b4ae-e1610f1997e8',
'https://google.qwiklabs.com/public_profiles/e079201c-5bda-4178-8bb9-cee00b9c07b9',
'https://google.qwiklabs.com/public_profiles/fb30cb76-18bb-4237-b953-293d7b59a1f6',
'https://run.qwiklabs.com/public_profiles/e3075a35-3440-408f-b124-7d98939379bf',
'https://www.qwiklabs.com/public_profiles/72a0191a-4611-4266-9630-5ac8c390d5c6',
'https://google.qwiklabs.com/public_profiles/3211425e-1057-4f6a-9a13-405ffc5c06df',
'https://google.qwiklabs.com/public_profiles/6461bde2-5770-4213-8504-79c07e0ee153',
'https://google.qwiklabs.com/public_profiles/2709705a-e18d-475a-a339-fce020893f41',
'https://google.qwiklabs.com/public_profiles/2f8f3bf3-12d6-474c-b9e9-cc9d6ee742b9',
'https://google.qwiklabs.com/public_profiles/605dc0aa-7bfb-4a2a-a5bc-9e0ee0014c9a',
'https://google.qwiklabs.com/public_profiles/253e864c-b888-4102-ba7f-37ef725b95e6',
'https://www.qwiklabs.com/public_profiles/105eb966-4086-4f78-8523-06421b7e3177',
'https://google.qwiklabs.com/public_profiles/163470b9-85bd-42da-a3ae-433115bf18ad',
'https://www.qwiklabs.com/public_profiles/af4a691c-4338-44f1-a611-705f6d595e31',
'https://www.qwiklabs.com/public_profiles/eee35ea0-0bdb-4d1d-874c-1e3d30fab8ad',
'https://www.qwiklabs.com/public_profiles/a77d5b83-37e3-4470-974b-0b0ea26cb120',
'https://google.qwiklabs.com/public_profiles/5643b7b1-48f0-4ebe-9f4f-1cb18c1267dd',
'https://www.qwiklabs.com/public_profiles/fc44a287-5550-48b3-a90e-a695cf15fa9b',
'https://google.qwiklabs.com/public_profiles/789dc16a-62df-4489-96ba-f8a0139cdfc8',
'https://google.qwiklabs.com/public_profiles/1ee2650a-3fab-4c70-98e9-052d9602e083',
'https://google.qwiklabs.com/public_profiles/5d26f3ed-7b78-4a3b-9fb7-247fa9aa2c5f',
'https://google.qwiklabs.com/public_profiles/c90ffd78-b10d-49ce-8549-40b34aee3d72',
'https://google.qwiklabs.com/public_profiles/00099757-9c0e-4769-9db8-b870e1bee6ef',
'https://www.qwiklabs.com/public_profiles/f43d02e8-93e0-4cd4-a08d-78b915dfb948',
'https://www.qwiklabs.com/public_profiles/1c4e09e2-f2b2-4e8b-a814-a5da034ef0f7',
'https://www.qwiklabs.com/public_profiles/9b7e451b-0989-4685-a057-eaf470c58f2e',
'https://google.qwiklabs.com/public_profiles/5876aaaa-49f1-425b-a366-2f412e776941',
'https://www.qwiklabs.com/public_profiles/76cc9598-3d1f-45a9-b633-22d67f616449',
'https://www.qwiklabs.com/public_profiles/70828dd3-c95d-49fa-b69a-6e53f402ec53',
'https://www.qwiklabs.com/public_profiles/0797bf0a-a668-4dcd-806d-48ef1ee40fb2',
'https://run.qwiklabs.com/public_profiles/beb22182-5e55-49de-b504-dace23ad5953',
'https://google.qwiklabs.com/public_profiles/2a3b0d2b-7611-405c-956d-f0b4dc0a57ff',
'https://google.qwiklabs.com/public_profiles/879ec4b3-6f7b-4260-b029-7aff88f3395e',
'https://google.qwiklabs.com/public_profiles/697ce78f-10f0-408f-ab5d-26f619512d6c',
'https://www.qwiklabs.com/public_profiles/0826618a-0310-4a9e-8dee-b3f257f8e4f8',
'https://www.qwiklabs.com/public_profiles/8e530b43-41bb-473e-a82a-61a4659b930f',
'https://google.qwiklabs.com/public_profiles/30de4bcf-1f17-4442-a724-7bcc39c94df5',
'https://google.qwiklabs.com/public_profiles/5997edd9-5d4d-4803-b265-7493d8f05985',
'https://google.qwiklabs.com/public_profiles/11536aaa-db6e-4f17-a520-2f083825bddd',
'https://google.qwiklabs.com/public_profiles/65c49ea5-bf58-4def-96ec-fb0394d17753',
'https://google.qwiklabs.com/public_profiles/4663aa19-69aa-44ca-aec7-8516189fd708',
'https://google.qwiklabs.com/public_profiles/572852db-bd11-4b02-88c1-40895562f5dc',
'https://www.qwiklabs.com/public_profiles/30302156-b63c-46bb-a863-3ea2cd821e26',
'https://google.qwiklabs.com/public_profiles/edb75c86-38c5-4036-8e7a-13b7da148e74',
'https://google.qwiklabs.com/public_profiles/1ae7b685-ca2b-44c1-b8c8-3cecf637d3d3',
'https://google.qwiklabs.com/public_profiles/17fd40e3-abb8-49cc-9aac-f4ca667bca0e',
'https://google.qwiklabs.com/public_profiles/83f912c8-f1b6-4bdb-b263-eb075c5e7a80',
'https://google.qwiklabs.com/public_profiles/9a0985b3-f397-40fa-8d12-bbdadc596556',
'https://www.qwiklabs.com/public_profiles/9e741de2-f4de-4d89-b98c-fe4f3049176e',
'https://www.qwiklabs.com/public_profiles/f82c59a3-909a-44d4-aa24-d7a1f9750220',
'https://google.qwiklabs.com/public_profiles/4ca8e347-11c0-43ad-82a4-142f9ac919f9',
'https://google-run.qwiklabs.com/public_profiles/5f1f6295-66e5-4ad8-9a0f-66a0eea852f6',
'https://www.qwiklabs.com/public_profiles/d0fde330-d5f0-499f-bd6e-70002971cebc',
'https://www.qwiklabs.com/public_profiles/cf9928f0-c0c3-423a-a966-8cedcc89330a',
'https://www.qwiklabs.com/public_profiles/239d34ac-086d-4517-838b-e87596cefa4b',
'https://google.qwiklabs.com/public_profiles/82ae158c-ca6c-4164-b1f7-11cf41e8b2e7',
'https://google.qwiklabs.com/public_profiles/3f5c1124-8611-4214-8294-ca2b00854125',
'https://www.qwiklabs.com/public_profiles/baa53b0f-735b-47f7-a42b-f4e2c851564d']

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
    'Perform Foundational Data, ML, and AI Tasks in Google Cloud',
    'Insights from Data with BigQuery',
    'Engineer Data in Google Cloud',
    'Integrate with Machine Learning APIs',
    'Explore Machine Learning Models with Explainable AI'
    ]

def data_scraping (url):
    start_thread(url)

def data_gathering(link):
    tempdic = {}
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    track1completed = []
    track2completed = []
    profile = soup.findAll('div', attrs = {'class':'public-profile__hero'})[0]
    dp = profile.img['src']
    name = profile.h1.text
    tempdic['name'] = name.strip()
    tempdic['dp'] = dp
    quests = soup.findAll('ql-badge')
    for quest in quests:
        allquest = json.loads(quest.get('badge'))['title']
        if allquest in track1:
            track1completed.append(allquest)
        if allquest in track2:
            track2completed.append(allquest)
    tempdic['track1'] = track1completed
    tempdic['track2'] = track2completed
    tempdic['qcomplete_no'] = len(track1completed) + len(track2completed)
    if tempdic['qcomplete_no']!=0:
        print(len(biglist)," ",tempdic['name']," ",tempdic['qcomplete_no']," ",tempdic['track1']," ",tempdic['track2'])
        biglist.append(tempdic)
        print("data saved")
    else:
        print("no badges")

def data_saving (biglist):
    res = sorted(biglist, key = lambda x: x['qcomplete_no'], reverse=True)
    with open("my.json","w") as f:
        json.dump(res,f)
    f.close()
    print(res)

def start_thread(url2):
    threads = 10
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(data_gathering, url2)
    data_saving (biglist)

def main(url):
    data_scraping (url)

if __name__ == '__main__':
    #t0 = time.time()
    main(url)
    #t1 = time.time()
    #print(f"{t1-t0} seconds to download {len(url2)} profile.")
    #print("number of people started",len(biglist))
