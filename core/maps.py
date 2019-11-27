# importing required libraries
import json
import time
import urllib.parse as parse

import urllib3

manager = urllib3.PoolManager(headers={
    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36'})


class TooManyRequests(Exception):
    pass


#  TODO Use leaflet
#  https://github.com/zaragoza-sedeelectronica/zaragoza-sedeelectronica.github.io/blob/master/rest/ejemplos/lineaAutobus.html

def getDistance(source, dest):
    # Take source as input
    source = getCoordinates(parse.quote(source + ",zaragoza,spain"))

    # Take destination as input
    dest = getCoordinates(parse.quote(dest + ",zaragoza,spain"))

    # url variable store url
    url = query('http://router.project-osrm.org/route/v1/driving/' + source + ';' + dest + '?overview=false')

    dist = 0.1
    for d in url['routes']:
        dist += d['distance']
    print(dist)
    return dist, source, dest


def getCoordinates(address):
    r = query('https://nominatim.openstreetmap.org/search?q=' + address + '&polygon=1&addressdetails=1&format=json')
    return r[0]['lat'] + ',' + r[0]['lon']


def query(url):
    time.sleep(0.1)
    r = manager.request('GET', url)

    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(url)
    print("---")
    print(r.data)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # json method of response object
    # return json format result
    x = json.loads(r.data.decode('utf-8'))

    if x == {'message': "Too Many Requests"}:
        raise TooManyRequests

    return x
