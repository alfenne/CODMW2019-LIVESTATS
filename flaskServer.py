from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json
import random
import time
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup

gamertag = urllib.parse.quote("import winner")

app = Flask(__name__)
CORS(app)
port = '5000'
DATA = [{'date': '01-22-2020', 'deathRate': 0.163}, {'date': '01-23-2020', 'deathRate': 0.1397}, {'date': '01-24-2020', 'deathRate': 0.1853}, {'date': '01-25-2020', 'deathRate': 0.2009}, {'date': '01-26-2020', 'deathRate': 0.2448}, {'date': '01-27-2020', 'deathRate': 0.3103}, {'date': '01-28-2020', 'deathRate': 0.3196}, {'date': '01-29-2020', 'deathRate': 0.3248}, {'date': '01-30-2020', 'deathRate': 0.3158}, {'date': '01-31-2020', 'deathRate': 0.3075}, {'date': '02-01-2020', 'deathRate': 0.8567}, {'date': '02-02-2020', 'deathRate': 1.2492}, {'date': '02-03-2020', 'deathRate': 1.497}, {'date': '02-04-2020', 'deathRate': 1.6484}, {'date': '02-05-2020', 'deathRate': 1.7484}, {'date': '02-06-2020', 'deathRate': 1.8215}, {'date': '02-07-2020', 'deathRate': 1.8816}, {'date': '02-08-2020', 'deathRate': 1.9392}, {'date': '02-09-2020', 'deathRate': 1.996}, {'date': '02-10-2020', 'deathRate': 2.0563}, {'date': '02-11-2020', 'deathRate': 2.1195}, {'date': '02-12-2020', 'deathRate': 2.1674}, {'date': '02-13-2020', 'deathRate': 2.1868}, {'date': '02-14-2020', 'deathRate': 2.2036}, {'date': '02-15-2020', 'deathRate': 2.2335}, {'date': '02-16-2020', 'deathRate': 2.2657}, {'date': '02-17-2020', 'deathRate': 2.2988}, {'date': '02-18-2020', 'deathRate': 2.3381}, {'date': '02-19-2020', 'deathRate': 2.383}, {'date': '02-20-2020', 'deathRate': 2.4327}, {'date': '02-21-2020', 'deathRate': 2.4776}, {'date': '02-22-2020', 'deathRate': 2.5322}, {'date': '02-23-2020', 'deathRate': 2.5794}, {'date': '02-24-2020', 'deathRate': 2.6357}, {'date': '02-25-2020', 'deathRate': 2.6914}, {'date': '02-26-2020', 'deathRate': 2.7462}, {'date': '02-27-2020', 'deathRate': 2.7959}, {'date': '02-28-2020', 'deathRate': 2.8441}, {'date': '02-29-2020', 'deathRate': 2.8888}, {'date': '03-01-2020', 'deathRate': 2.9283}, {'date': '03-02-2020', 'deathRate': 2.9691}, {'date': '03-03-2020', 'deathRate': 3.0062}, {'date': '03-04-2020', 'deathRate': 3.0418}, {'date': '03-05-2020', 'deathRate': 3.0753}, {'date': '03-06-2020', 'deathRate': 3.1071}, {'date': '03-07-2020', 'deathRate': 3.1344}, {'date': '03-08-2020', 'deathRate': 3.1706}, {'date': '03-09-2020', 'deathRate': 3.2077}, {'date': '03-10-2020', 'deathRate': 3.2396}, {'date': '03-11-2020', 'deathRate': 3.2758}, {'date': '03-12-2020', 'deathRate': 3.3087}, {'date': '03-13-2020', 'deathRate': 3.346}, {'date': '03-14-2020', 'deathRate': 3.3839}, {'date': '03-15-2020', 'deathRate': 3.4299}, {'date': '03-16-2020', 'deathRate': 3.481}, {'date': '03-17-2020', 'deathRate': 3.942}]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/getStats', methods=['GET'])
def getStats():
    try:

        requests.post("https://api.dreamteam.gg/games/cod/players/xbl/" + gamertag + "/update")
        time.sleep(5)
        response = requests.get("https://api.dreamteam.gg/games/cod/players/xbl/" + gamertag + "/stats")
        jsonData = json.loads(response.text)

        deaths,cases = getCoronaStats()

        statsDict = {}

        kdSpread = jsonData['weekly']['all']['kd_ratio']
        scorePerMinute = jsonData['weekly']['all']['score_per_minute']
        scorePerGame = jsonData['weekly']['all']['score_per_game']
        wlRatio = jsonData['weekly']['all']['wl_ratio']
        longestStreak = jsonData['weekly']['all']['longest_streak']
        killsPerGame = jsonData['weekly']['all']['kills'] / jsonData['weekly']['all']['matches_played']
        killsPerMinute = jsonData['weekly']['all']['kills'] / (jsonData['weekly']['all']['time_played'] / 60)
        accuracy = jsonData['weekly']['all']['accuracy']
        atKdSpread = jsonData['lifetime']['all']['kd_ratio']

        statsDict['kdSpread'] = kdSpread
        #statsDict['kdSpread'] = random.uniform(0, 1)
        statsDict['scorePerMinute'] = scorePerMinute
        statsDict['scorePerGame'] = scorePerGame
        statsDict['wlRatio'] = wlRatio
        statsDict['longestStreak'] = longestStreak
        statsDict['killsPerGame'] = killsPerGame
        statsDict['killsPerMinute'] = killsPerMinute
        statsDict['accuracy'] = accuracy
        statsDict['atKdSpread'] = atKdSpread

        statsDict['coronaDeaths'] = deaths
        statsDict['coronaCases'] = cases

        currDate = datetime.now().strftime("%m-%d-%Y")
        foundData = False

        currRate = round(((deaths / cases) * 100), 4)

        for day in DATA:
            date = day['date']
            if currDate == date:
                foundData = True
                day['deathRate'] = currRate

        if not foundData:
            DATA.append({"date":currDate,"deathRate":currRate})

        statsDict['timeSeriesData'] = DATA
        statsDict['currRate'] = currRate

        return jsonify(statsDict)
    
    except:
        return "error"

def getCoronaStats():

    response = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(response.text, 'html.parser')

    nums = soup.select("[class~=maincounter-number] > span")

    return (int(nums[1].get_text().replace(",","")), int(nums[0].get_text().replace(",","")))

app.run(port=port)


