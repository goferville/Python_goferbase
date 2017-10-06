"""
Example:
import json
weather = urllib2.urlopen('url')
wjson = weather.read()
wjdata = json.loads(wjson)
print wjdata['data']['current_condition'][0]['temp_C']
    What you get from the url is a json string.
And your can't parse it with index directly.
You should convert it to a dict by json.loads
and then you can parse it with index.
"""
import json
js=json.dumps({'name':'John', 'age':49})
print(js)
js=json.dumps({'name':'John', 'age':[49,50]})
print(js)
# print(js.name)
ar=json.loads(js)
print(ar)
print(ar['name'])
print(ar['age'][1])
weather_js={
 "query": {
  "count": 1,
  "created": "2017-10-06T08:25:26Z",
  "lang": "en-US",
  "results": {
   "channel": {
    "wind": {
     "chill": "63",
     "direction": "150",
     "speed": "11"
    }
   }
  }
 }
}
print(weather_js['query']['results']['channel']['wind']['speed'])
# weather_load=json.loads(weather_js)