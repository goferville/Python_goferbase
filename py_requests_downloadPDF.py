import requests, csv, time

#url = 'https://bnsec.bluenile.com/bnsecure/certs/LD09642120/GIA?country=USA&language=en-us'



with open('di_list_2018.csv','r') as fr:
    csvReader = csv.reader(fr)
    i=1
    for row in csvReader:
        print(i)
        i+=1
        url='https://bnsec.bluenile.com/bnsecure/certs/'+row[1]+'/GIA?country=USA&language=en-us'
        print(url)
        response = requests.get(url)
        with open(row[1]+'.pdf', 'wb') as f:
            f.write(response.content)

        time.sleep(2)