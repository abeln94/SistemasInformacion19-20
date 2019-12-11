# importing required libraries
import json
import time
import urllib.parse as parse
from math import sin, cos, sqrt, atan2, radians

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

    distCar = 0
    for d in url['routes']:
        distCar += d['distance']
    print(distCar)
    distBus = getLinearDistance(source, dest) * 0.5
    print(distBus)
    return distCar, distBus, source, dest


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


def getLinearDistance(a, b):
    # approximate radius of earth in m
    R = 6373000

    lat1 = radians(float(a.split(',')[0]))
    lon1 = radians(float(a.split(',')[1]))
    lat2 = radians(float(b.split(',')[0]))
    lon2 = radians(float(b.split(',')[1]))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c
