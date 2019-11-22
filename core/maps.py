# importing required libraries
import json
import random
import urllib.parse as parse

import urllib3


#  TODO Use leaflet
#  https://github.com/zaragoza-sedeelectronica/zaragoza-sedeelectronica.github.io/blob/master/rest/ejemplos/lineaAutobus.html

def getDistance(source, dest):

    # Take source as input
    source = getCoordinates(parse.quote(source+",zaragoza,spain"))

    # Take destination as input
    dest = getCoordinates(parse.quote(dest+",zaragoza,spain"))

    # url variable store url
    url = query('http://router.project-osrm.org/route/v1/driving/'+source+';'+dest+'?overview=false')

    if 'routes' not in url:
        return random.random()*1000, source, dest

    dist = 0.1
    for d in url['routes']:
        dist += d['distance']
    print(dist)
    return dist, source, dest

def getCoordinates(address):
    r = query('https://nominatim.openstreetmap.org/search?q='+address+'&polygon=1&addressdetails=1&format=json')
    if 0 not in r:
        return address
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