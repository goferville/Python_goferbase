
import urllib.request, time, os, re, csv


def fetchGF(googleticker):
    url = "http://www.google.com/finance?&q="
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    k=re.search(b'id="ref_(.*?)">(.*?)<', respData)
    if k:
        tmp=k.group(2)
        q=tmp.decode().replace(',','')
    else:
        q="Nothing found for: "+googleticker
    return q
print(fetchGF('aapl'))
