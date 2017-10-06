import json
import  urllib.request
url='https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22gilbert%2C%20az%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
# need to convert 'b byte data to string with: .decode('utf-8')
weather=urllib.request.urlopen(url).read().decode('utf-8')
print(weather)
# to parse json weather
js_prsed=json.loads(weather)
#reference after parsed
print(js_prsed['query']['results']['channel']['wind']['speed'])

#forecast
url='https://query.yahooapis.com/v1/public/yql?q=select%20*%20from' \
    '%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from' \
    '%20geo.places(1)%20where%20text%3D%22gilbert%2C%20az%22)&format=json&env' \
    '=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'
# get json string back
weather=urllib.request.urlopen(url).read().decode('utf-8')
print('forecast:')
print(weather)
# to parse json weather
js_prsed=json.loads(weather)
print(js_prsed['query']['results']['channel']['title'])