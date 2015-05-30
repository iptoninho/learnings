import urllib.request
import json

def save_image(friend):
  size = '/picture?width=200&height=200'
  url = 'https://graph.facebook.com/'+ friend['1675523278'] + size
  image = urllib.request.urlopen(url).read()
  f = open(friend['name'] + '.jpg', 'wb')
  f.write(image)
  f.close()
  print (friend['name'] + '.jpg impresso')
#get the token https://developers.facebook.com/tools/explorer
url = 'https://graph.facebook.com/me/friends?access_token=CAACEdEose0cBANBRZBTBw1xkRonp96xbwoukjprKN6atsc2cl5KTqX0jrJCtMFKe4cMgqf4PhcZCm0NuiMZA2XQWdlvJyZCRt7bFg2f6lCUtN2zKoB5j5q2pq0S9vHGoav7uhPZBAUulZAXJumCezPUZANFZBbNkNwjERogtwszCM2ZCpNXm6i4UWKpZBnz9OQqiMyezm8icG8lZCAadyrNx96c'
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

for friend in data['data']:
  save_image(friend)

