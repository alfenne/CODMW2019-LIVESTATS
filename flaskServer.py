from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json
import random
import time
import urllib.parse
from datetime import datetime
from bs4 import BeautifulSoup

gamertag = urllib.parse.quote("FenTech2")

app = Flask(__name__)
CORS(app)
port = '5000'
DATA = [{'date': '01-22-2020', 'deaths': 0, 'cases': 1}, {'date': '01-23-2020', 'deaths': 0, 'cases': 1}, {'date': '01-24-2020', 'deaths': 0, 'cases': 2}, {'date': '01-25-2020', 'deaths': 0, 'cases': 2}, {'date': '01-26-2020', 'deaths': 0, 'cases': 5}, {'date': '01-27-2020', 'deaths': 0, 'cases': 5}, {'date': '01-28-2020', 'deaths': 0, 'cases': 5}, {'date': '01-29-2020', 'deaths': 0, 'cases': 5}, {'date': '01-30-2020', 'deaths': 0, 'cases': 5}, {'date': '01-31-2020', 'deaths': 0, 'cases': 6}, {'date': '02-01-2020', 'deaths': 0, 'cases': 8}, {'date': '02-02-2020', 'deaths': 0, 'cases': 8}, {'date': '02-03-2020', 'deaths': 0, 'cases': 11}, {'date': '02-04-2020', 'deaths': 0, 'cases': 11}, {'date': '02-05-2020', 'deaths': 0, 'cases': 12}, {'date': '02-06-2020', 'deaths': 0, 'cases': 12}, {'date': '02-07-2020', 'deaths': 0, 'cases': 12}, {'date': '02-08-2020', 'deaths': 0, 'cases': 12}, {'date': '02-09-2020', 'deaths': 0, 'cases': 12}, {'date': '02-10-2020', 'deaths': 0, 'cases': 12}, {'date': '02-11-2020', 'deaths': 0, 'cases': 13}, {'date': '02-12-2020', 'deaths': 0, 'cases': 13}, {'date': '02-13-2020', 'deaths': 0, 'cases': 15}, {'date': '02-14-2020', 'deaths': 0, 'cases': 15}, {'date': '02-15-2020', 'deaths': 0, 'cases': 15}, {'date': '02-16-2020', 'deaths': 0, 'cases': 15}, {'date': '02-17-2020', 'deaths': 0, 'cases': 15}, {'date': '02-18-2020', 'deaths': 0, 'cases': 15}, {'date': '02-19-2020', 'deaths': 0, 'cases': 15}, {'date': '02-20-2020', 'deaths': 0, 'cases': 15}, {'date': '02-21-2020', 'deaths': 0, 'cases': 35}, {'date': '02-22-2020', 'deaths': 0, 'cases': 35}, {'date': '02-23-2020', 'deaths': 0, 'cases': 35}, {'date': '02-24-2020', 'deaths': 0, 'cases': 53}, {'date': '02-25-2020', 'deaths': 0, 'cases': 53}, {'date': '02-26-2020', 'deaths': 0, 'cases': 59}, {'date': '02-27-2020', 'deaths': 0, 'cases': 60}, {'date': '02-28-2020', 'deaths': 0, 'cases': 62}, {'date': '02-29-2020', 'deaths': 1, 'cases': 70}, {'date': '03-01-2020', 'deaths': 1, 'cases': 76}, {'date': '03-02-2020', 'deaths': 6, 'cases': 101}, {'date': '03-03-2020', 'deaths': 7, 'cases': 122}, {'date': '03-04-2020', 'deaths': 11, 'cases': 153}, {'date': '03-05-2020', 'deaths': 12, 'cases': 221}, {'date': '03-06-2020', 'deaths': 14, 'cases': 278}, {'date': '03-07-2020', 'deaths': 17, 'cases': 417}, {'date': '03-08-2020', 'deaths': 21, 'cases': 537}, {'date': '03-09-2020', 'deaths': 22, 'cases': 605}, {'date': '03-10-2020', 'deaths': 28, 'cases': 959}, {'date': '03-11-2020', 'deaths': 36, 'cases': 1281}, {'date': '03-12-2020', 'deaths': 40, 'cases': 1663}, {'date': '03-13-2020', 'deaths': 47, 'cases': 2179}, {'date': '03-14-2020', 'deaths': 54, 'cases': 2726}, {'date': '03-15-2020', 'deaths': 63, 'cases': 3499}, {'date': '03-16-2020', 'deaths': 85, 'cases': 4632}, {'date': '03-17-2020', 'deaths': 108, 'cases': 6421}, {'date': '03-18-2020', 'deaths': 118, 'cases': 7786}, {'date': '03-19-2020', 'deaths': 200, 'cases': 13680}, {'date': '03-20-2020', 'deaths': 244, 'cases': 19101}, {'date': '03-21-2020', 'deaths': 307, 'cases': 25493}, {'date': '03-22-2020', 'deaths': 417, 'cases': 33276}]
STATE_POPS = {'US-AL': 4903185, 'US-AK': 731545, 'US-AZ': 7278717, 'US-AR': 3017804, 'US-CA': 39512223, 'US-CO': 5758736, 'US-CT': 3565287, 'US-DE': 973764, 'US-DC': 705749, 'US-FL': 21477737, 'US-GA': 10617423, 'US-HI': 1415872, 'US-ID': 1787065, 'US-IL': 12671821, 'US-IN': 6732219, 'US-IA': 3155070, 'US-KS': 2913314, 'US-KY': 4467673, 'US-LA': 4648794, 'US-ME': 1344212, 'US-MD': 6045680, 'US-MA': 6892503, 'US-MI': 9986857, 'US-MN': 5639632, 'US-MS': 2976149, 'US-MO': 6137428, 'US-MT': 1068778, 'US-NE': 1934408, 'US-NV': 3080156, 'US-NH': 1359711, 'US-NJ': 8882190, 'US-NM': 2096829, 'US-NY': 19453561, 'US-NC': 10488084, 'US-ND': 762062, 'US-OH': 11689100, 'US-OK': 3956971, 'US-OR': 4217737, 'US-PA': 12801989, 'US-RI': 1059361, 'US-SC': 5148714, 'US-SD': 884659, 'US-TN': 6829174, 'US-TX': 28995881, 'US-UT': 3205958, 'US-VT': 623989, 'US-VA': 8535519, 'US-WA': 7614893, 'US-WV': 1792147, 'US-WI': 5822434, 'US-WY': 578759}

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

        statsDict = {}

        kdSpread = jsonData['weekly']['all']['kd_ratio']
        scorePerMinute = jsonData['weekly']['all']['score_per_minute']
        scorePerGame = jsonData['weekly']['all']['score_per_game']
        wlRatio = jsonData['weekly']['all']['wl_ratio']
        longestStreak = jsonData['weekly']['all']['longest_streak']
        try:
            killsPerMinute = jsonData['weekly']['all']['kills'] / (jsonData['weekly']['all']['time_played'] / 60)
            killsPerGame = jsonData['weekly']['all']['kills'] / jsonData['weekly']['all']['matches_played']

        except:
            killsPerMinute = 0
            killsPerGame = 0
        accuracy = jsonData['weekly']['all']['accuracy']
        atKdSpread = jsonData['lifetime']['all']['kd_ratio']

        statsDict['kdSpread'] = kdSpread
        statsDict['scorePerMinute'] = scorePerMinute
        statsDict['scorePerGame'] = scorePerGame
        statsDict['wlRatio'] = wlRatio
        statsDict['longestStreak'] = longestStreak
        statsDict['killsPerGame'] = killsPerGame
        statsDict['killsPerMinute'] = killsPerMinute
        statsDict['accuracy'] = accuracy
        statsDict['atKdSpread'] = atKdSpread

        for key in statsDict:
            if statsDict[key] is None:
                statsDict[key] = 0

        return jsonify(statsDict)
    
    except:
        return "error"

def getCoronaStats():

    response = requests.get("https://www.worldometers.info/coronavirus/country/us/")
    soup = BeautifulSoup(response.text, 'html.parser')

    nums = soup.select("[class~=maincounter-number] > span")

    return (int(nums[1].get_text().replace(",","")), int(nums[0].get_text().replace(",","")))

app.run(port=port)


