from geopy.geocoders import Nominatim
from math import radians, cos, sin, asin, sqrt

def get_lonlat(address):

	loc = Nominatim(user_agent="Geopy Library")
	getLoc = loc.geocode(address)

	lat = (getLoc.latitude)
	lon = (getLoc.longitude)
	return lat,lon

	#print(getLoc.latitude)
	#print(getLoc.longitude)

def get_distance(start_lat, end_lat,start_lon,end_lon):

	r = 6371
	lon1 = radians(start_lon)
	lon2 = radians(end_lon)
	lat1 = radians(start_lat)
	lat2 = radians(end_lat)

	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2

	c = 2 * asin(sqrt(a))
	return(c*r)



val=input("whats the pickup address:")
start_lat,start_lon = get_lonlat(val)
val1=input("whats the destination:")
end_lat,end_lon = get_lonlat(val1)

print(round(get_distance(start_lat, end_lat, start_lon, end_lon),2))




