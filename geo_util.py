import requests
import json
import urllib.request
from geopy.geocoders import Nominatim

def get_lonlat(address):

	loc = Nominatim(user_agent="Geopy Library")
	getLoc = loc.geocode(address)

	lat = (getLoc.latitude)
	lon = (getLoc.longitude)
	return lat,lon

def get_distance_duration(start_lat, start_lon, end_lat, end_lon):

	# URL to the tomtom api
	apiURL      = "https://api.tomtom.com/routing/1/calculateRoute"
	# apiKey
	apiKey      = "eAhxGZstyLnRbCZ3PwEYPtuyvQs1JyHv"

	#[coordinates]
	sourceLat   = start_lat
	sourceLon   = start_lon
	destLat     = end_lat
	destLon     = end_lon

	tomtomURL = "%s/%s,%s:%s,%s/json?key=%s" % (apiURL,sourceLat,sourceLon,destLat,destLon,apiKey)

	getData = urllib.request.urlopen(tomtomURL).read()
	jsonTomTomString = json.loads(getData)

	Duration = jsonTomTomString['routes'][0]['summary']['travelTimeInSeconds']
	Distance = jsonTomTomString['routes'][0]['summary']['lengthInMeters']
	
	Distance = Distance/1609
	Duration = Duration/60
	
	return Distance, Duration
	
def get_distance(start_lat, start_lon, end_lat, end_lon):

	# URL to the tomtom api
	apiURL      = "https://api.tomtom.com/routing/1/calculateRoute"
	# apiKey
	apiKey      = "eAhxGZstyLnRbCZ3PwEYPtuyvQs1JyHv"

	#[coordinates]
	sourceLat   = start_lat
	sourceLon   = start_lon
	destLat     = end_lat
	destLon     = end_lon

	tomtomURL = "%s/%s,%s:%s,%s/json?key=%s" % (apiURL,sourceLat,sourceLon,destLat,destLon,apiKey)

	getData = urllib.request.urlopen(tomtomURL).read()
	jsonTomTomString = json.loads(getData)

	#Duration = jsonTomTomString['routes'][0]['summary']['travelTimeInSeconds']
	Distance = jsonTomTomString['routes'][0]['summary']['lengthInMeters']
	
	Distance = Distance/1609
	
	return Distance

def get_duration(start_lat, start_lon, end_lat, end_lon):

	# URL to the tomtom api
	apiURL      = "https://api.tomtom.com/routing/1/calculateRoute"
	# apiKey
	apiKey      = "eAhxGZstyLnRbCZ3PwEYPtuyvQs1JyHv"

	#[coordinates]
	sourceLat   = start_lat
	sourceLon   = start_lon
	destLat     = end_lat
	destLon     = end_lon

	tomtomURL = "%s/%s,%s:%s,%s/json?key=%s" % (apiURL,sourceLat,sourceLon,destLat,destLon,apiKey)

	getData = urllib.request.urlopen(tomtomURL).read()
	jsonTomTomString = json.loads(getData)

	Duration = jsonTomTomString['routes'][0]['summary']['travelTimeInSeconds']
	#Distance = jsonTomTomString['routes'][0]['summary']['lengthInMeters']
	
	Duration = Duration/60
	
	return Duration

