import json
import requests

url = 'https://hs-consumer-api.espncricinfo.com/v1/edition/feed?edition=ww&page=1&records=10'
res = requests.get(url)
data = json.loads(res.text)

for news in data['results']:
  print(news)
  print('\n')