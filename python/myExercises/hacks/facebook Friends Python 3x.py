import urllib.request
import json
#copie o formato no exemplo e pegue o access_token
#em https://developers.facebook.com/tools/explorer
url = 'https://graph.facebook.com/me/friends?access_token=CAAAAAITEghMBAJeZC1soK034zIi6TLjvfpOjmog7mGqIrkha8m2rQ57EPYkqsFGqC9p7vmq7RrKYHgEyme7eOPB9HsfKo5JE9NbDljKo9OgqTHvFrVZCBtO8BMtpPvsblyvXVudwJv5yI6UkZBqDxEDfa5giWEZD'
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
for amigo in data['data']:
  print (amigo['name'])
