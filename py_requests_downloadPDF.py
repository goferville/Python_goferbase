import requests

url = 'https://bnsec.bluenile.com/bnsecure/certs/LD09642120/GIA?country=USA&language=en-us'
url = 'https://bnsec.bluenile.com/bnsecure/certs/LD10089587/GIA?country=USA&language=en-us'
response = requests.get(url)

with open('test1.pdf', 'wb') as f:
    f.write(response.content)