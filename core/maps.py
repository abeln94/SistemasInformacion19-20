# importing required libraries
import json
import urllib3

def getDistance():

    # Take source as input
    source = getCoordinates("plaza+san+francisco,zaragoza,spain")

    # Take destination as input
    dest = getCoordinates("campus+rio+ebro,zaragoza,spain")

    # url variable store url
    url = query('http://router.project-osrm.org/route/v1/driving/'+source+';'+dest+'?overview=false')

    dist = 0
    for d in url['routes']:
        dist += d['distance']
    print(dist)

def getCoordinates(address):
    r = query('https://nominatim.openstreetmap.org/search?q='+address+'&polygon=1&addressdetails=1&format=json')
    return r[0]['lat'] + ',' + r[0]['lon']

def query(url):
    r = urllib3.PoolManager(headers={'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'}).request('GET', url)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(r.data)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # json method of response object
    # return json format result
    x = json.loads(r.data.decode('utf-8'))

    return x