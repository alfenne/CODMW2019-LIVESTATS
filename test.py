import requests
import json
import time
from datetime import datetime

PREV_DATA = [{'date': '01-22-2020', 'deathRate': 3.0631}, {'date': '01-23-2020', 'deathRate': 2.7565}, {'date': '01-24-2020', 'deathRate': 2.763}, {'date': '01-25-2020', 'deathRate': 2.9207}, {'date': '01-26-2020', 'deathRate': 2.644}, {'date': '01-27-2020', 'deathRate': 2.8015}, {'date': '01-28-2020', 'deathRate': 2.3485}, {'date': '01-29-2020', 'deathRate': 2.1573}, {'date': '01-30-2020', 'deathRate': 2.0765}, {'date': '01-31-2020', 'deathRate': 2.1461}, {'date': '02-01-2020', 'deathRate': 2.1515}, {'date': '02-02-2020', 'deathRate': 2.1564}, {'date': '02-03-2020', 'deathRate': 2.1427}, {'date': '02-04-2020', 'deathRate': 2.0593}, {'date': '02-05-2020', 'deathRate': 2.0408}, {'date': '02-06-2020', 'deathRate': 2.0572}, {'date': '02-07-2020', 'deathRate': 2.0906}, {'date': '02-08-2020', 'deathRate': 2.1713}, {'date': '02-09-2020', 'deathRate': 2.2565}, {'date': '02-10-2020', 'deathRate': 2.3689}, {'date': '02-11-2020', 'deathRate': 2.4842}, {'date': '02-12-2020', 'deathRate': 2.4722}, {'date': '02-13-2020', 'deathRate': 2.271}, {'date': '02-14-2020', 'deathRate': 2.277}, {'date': '02-15-2020', 'deathRate': 2.4134}, {'date': '02-16-2020', 'deathRate': 2.485}, {'date': '02-17-2020', 'deathRate': 2.5498}, {'date': '02-18-2020', 'deathRate': 2.6711}, {'date': '02-19-2020', 'deathRate': 2.8054}, {'date': '02-20-2020', 'deathRate': 2.9489}, {'date': '02-21-2020', 'deathRate': 2.9293}, {'date': '02-22-2020', 'deathRate': 3.1273}, {'date': '02-23-2020', 'deathRate': 3.1259}, {'date': '02-24-2020', 'deathRate': 3.304}, {'date': '02-25-2020', 'deathRate': 3.3675}, {'date': '02-26-2020', 'deathRate': 3.4031}, {'date': '02-27-2020', 'deathRate': 3.4004}, {'date': '02-28-2020', 'deathRate': 3.414}, {'date': '02-29-2020', 'deathRate': 3.4193}, {'date': '03-01-2020', 'deathRate': 3.3903}, {'date': '03-02-2020', 'deathRate': 3.416}, {'date': '03-03-2020', 'deathRate': 3.4036}, {'date': '03-04-2020', 'deathRate': 3.4208}, {'date': '03-05-2020', 'deathRate': 3.4203}, {'date': '03-06-2020', 'deathRate': 3.3988}, {'date': '03-07-2020', 'deathRate': 3.3618}, {'date': '03-08-2020', 'deathRate': 3.4625}, {'date': '03-09-2020', 'deathRate': 3.5182}, {'date': '03-10-2020', 'deathRate': 3.5941}, {'date': '03-11-2020', 'deathRate': 3.6666}, {'date': '03-12-2020', 'deathRate': 3.6776}, {'date': '03-13-2020', 'deathRate': 3.7219}, {'date': '03-14-2020', 'deathRate': 3.7278}, {'date': '03-15-2020', 'deathRate': 3.846}, {'date': '03-16-2020', 'deathRate': 3.9252}]
currDate = datetime.now().strftime("%m-%d-%Y")
foundData = False

for day in PREV_DATA:
    date = day['date']
    if currDate == date:
        foundData = True


