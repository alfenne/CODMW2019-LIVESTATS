from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json
import random
import time
import urllib.parse

gamertag = urllib.parse.quote("import winner")

app = Flask(__name__)
CORS(app)
port = '5000'

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

    
        return jsonify(statsDict)
    
    except:
        return "error"

def getCoronaStats():

    url = "https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Z7biAeD8PAkqgmWhxG2A/FeatureServer/1/query?f=json&where=Confirmed%20%3E%200&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20DESC&outSR=102100&resultOffset=0&resultRecordCount=10000&cacheHint=true&quantizationParameters=%7B%22mode%22%3A%22view%22%2C%22originPosition%22%3A%22upperLeft%22%2C%22tolerance%22%3A515.985125%2C%22extent%22%3A%7B%22xmin%22%3A-180%2C%22ymin%22%3A-90%2C%22xmax%22%3A180%2C%22ymax%22%3A90%2C%22spatialReference%22%3A%7B%22wkid%22%3A4326%2C%22latestWkid%22%3A4326%7D%7D%7D"

    headers = {
        'Origin': "https://www.arcgis.com",
        'Referer': "https://www.arcgis.com/apps/opsdashboard/index.html",
        'Sec-Fetch-Dest': "empty",
        'cache-control': "no-cache",
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()

    deaths = sum([death['attributes']['Deaths'] for death in data['features']])
    cases = sum(case['attributes']['Confirmed'] for case in data['features'])

    return (deaths, cases)

app.run(port=port)


