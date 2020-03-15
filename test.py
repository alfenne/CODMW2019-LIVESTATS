import requests
import json

url = "https://services9.arcgis.com/N9p5hsImWXAccRNI/arcgis/rest/services/Z7biAeD8PAkqgmWhxG2A/FeatureServer/1/query?f=json&where=Confirmed%20%3E%200&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&orderByFields=Confirmed%20DESC&outSR=102100&resultOffset=0&resultRecordCount=10000&cacheHint=true&quantizationParameters=%7B%22mode%22%3A%22view%22%2C%22originPosition%22%3A%22upperLeft%22%2C%22tolerance%22%3A515.985125%2C%22extent%22%3A%7B%22xmin%22%3A-180%2C%22ymin%22%3A-90%2C%22xmax%22%3A180%2C%22ymax%22%3A90%2C%22spatialReference%22%3A%7B%22wkid%22%3A4326%2C%22latestWkid%22%3A4326%7D%7D%7D"

headers = {
    'Origin': "https://www.arcgis.com",
    'Referer': "https://www.arcgis.com/apps/opsdashboard/index.html",
    'Sec-Fetch-Dest': "empty",
    'cache-control': "no-cache",
    'Postman-Token': "99896d3d-66e1-4baf-96ce-78dd9fdc5130"
    }

response = requests.request("GET", url, headers=headers)

data = response.json()

deaths = sum([death['attributes']['Deaths'] for death in data['features']])
cases = sum(case['attributes']['Confirmed'] for case in data['features'])

print(deaths)
print(cases)