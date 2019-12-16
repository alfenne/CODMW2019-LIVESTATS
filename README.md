# Call of Duty Modern Warfare (2019) Real-Time Stats

I have a Raspberry Pi with a 3.5" Adafruit TFT Display next to my TV running this application. While you are playing Call of Duty modern warfare you can view various personal stats change in near real-time. The stats are calculated on a rolling weekly basis meaning they are only from the last 7 days. The only stat is isn't rolling weekly is the "All-Time K/D Spread", that is your all-time career K/D Spread.

![Device Image](device.pdf)

The device is a touchscreen, touch anywhere on the device to move to the next stat. I have also created an iOS app to remotely control the device.

The stats the application provides is 
1) K/D Spread
2) Score (XP) Per Minute
3) Score (XP) Per Game
4) Game Win/Loss Ratio
5) Longest Streak
6) Average Kills Per Game
7) Average Kills Per Minute
8) Accuracy (% of shots on target)
9) All-Time K/D Spread


### Setup

1) Change the global variable on line 9 in flaskServer.py to your gamertag. My gamertag is 'import winner', sorry if this is confusing given the context

2) Be sure Python 3 is installed and referenced in your machines path

3) Install Flask and Flask CORS
```bash
pip3 install flask
```
```bash
pip3 install -U flask-cors
```

4) Start the flask server on port 5000
```bash
python3 flaskServer.py
```

5) In a browser of your choice, go to localhost:5000

6) Display this application in any way you'd like


