import requests
import json

url = "http://cricapi.com/api/matches?apikey=D18haZnedRZ3QijAQEJJV97U5r23"
try:
    r = requests.get(url)
except:
    print("Cant request the data, probably no internet connection")
    exit(1)

data = json.loads(r.text)

print("Enter name of the country")
teamName=input()
id=""
for item in data['matches']:
    if (item['team-1']==teamName.title() or item["team-2"]==teamName.title()):
        if item["matchStarted"]:
            id=item["unique_id"]
            break
        else:
            print("Match not started yet")
            exit(1)
else:
    print("Country not found")
    exit(1)

if id:
    try:
        r = requests.get("http://cricapi.com/api/cricketScore?apikey=D18haZnedRZ3QijAQEJJV97U5r23&unique_id="+str(id))
        score = json.loads(r.text)
    except:
        print("Cant load the data, probably wrong id")
        exit(1)
    

print(score['stat'])
print("Score:\t"+score['score'].replace("&amp;"," & "))

#print("Match Stared:\t"+str(score['matchStarted']))
#print(score["team-1"])
#print(score["team-2"])