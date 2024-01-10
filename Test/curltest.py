from geopy.geocoders import Nominatim
import requests,json

def get_lonlat(address):

	loc = Nominatim(user_agent="Geopy Library")
	getLoc = loc.geocode(address)

	lat = (getLoc.latitude)
	lon = (getLoc.longitude)
	return lat,lon
	
val="1514 Mohave Drive Colton CA"
val2="435 E Hospitality Lane, San Bernardino CA"

start_lat,start_lon = get_lonlat(val)
end_lat,end_lon = get_lonlat(val2)

payload = {
    "origins": [{"latitude": start_lat, "longitude": start_lon}],
    "destinations": [{"latitude": end_lat, "longitude": end_lon}],
    "travelMode": "driving",
}

paramtr = {"key": "Alnl7OjP5Vk1MKEB_Oaof_Fe_OD7KJHkydKd4vMeaB9l9ZyUlEDLpdG-DK58eyvM"}

r = requests.post('https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix', data = json.dumps(payload), params = paramtr)

dt = json.loads(r.content)

travelDistance = dt['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']

travelDuration = dt['resourceSets'][0]['resources'][0]['results'][0]['travelDuration']

print(travelDistance)
print(travelDuration)

