from db_util import get_dataset, insert_record, update_record
import time,requests,json,geocoder
from decimal import Decimal
from datetime import date, timedelta, datetime

def get_dist(start_lat, start_lon, end_lat, end_lon):
	payload = {
    	"origins": [{"latitude": start_lat, "longitude": start_lon}],
    	"destinations": [{"latitude": end_lat, "longitude": end_lon}],
    	"travelMode": "driving",
	}

	paramtr = {"key": "Alnl7OjP5Vk1MKEB_Oaof_Fe_OD7KJHkydKd4vMeaB9l9ZyUlEDLpdG-DK58eyvM"}

	r = requests.post('https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix', data = json.dumps(payload), params = paramtr)

	dt = json.loads(r.content)
	
	Distance = dt['resourceSets'][0]['resources'][0]['results'][0]['travelDistance']

	#Duration = dt['resourceSets'][0]['resources'][0]['results'][0]['travelDuration']
	
	return Distance

def calc_duration(start, end):

	t1 = datetime.strptime(start, "%H:%M:%S")

	t2 = datetime.strptime(end, "%H:%M:%S")
	
	
	delta = t2 - t1
	
	dur = delta.total_seconds() / 60
	
	return dur

def get_current_location():
	g = geocoder.ip('me')
	return g.latlng

def get_trip_request(bid_id):

	sql = "SELECT Request_ID from Requests_Bids Where Bid_Id=%s;"
	
	vals = (bid_id)
	
	myresult = get_dataset(sql, vals)
	
	for row in myresult:
		trip_request_id = row[0]
	
	return trip_request_id
	
def get_per_min_mile(bid_id):

	sql = "SELECT Per_Mile, Per_Min from tbl_Bids Where Bid_Id=%s;"
	
	vals = (bid_id)
	
	myresult = get_dataset(sql, vals)
	
	for row in myresult:
		mile = row[0]
		min = row[1]
	
	return mile, min


class Trip:		
				
	def add_trip(self, bid_id):
	
		trip_request_id = get_trip_request(bid_id)
	
		sql = "INSERT INTO tbl_Trips(Trip_Request_Id, Bid_Id, Trip_Date) Values(%s, %s, %s)"
		vals = (trip_request_id, bid_id, date.today())
		
		self.trip_id = insert_record(sql,vals)
		self.bid_id = bid_id
		
	def update_trip(self, name, value):
	
		sql = "UPDATE tbl_Trips SET " + name + " = %s WHERE Trip_ID=%s"
		vals = (value, self.trip_id)
		
		update_record(sql, vals)
	
	def begin_trip(self):
		current_lat, current_lon = get_current_location()
		#self.start_time = "23:39:42"
		self.start_time = time.strftime("%H:%M:%S", time.localtime())
		self.start_lat = current_lat
		self.start_lon = current_lon
		self.status = 2
		self.update_trip("Start_Time", self.start_time)
		self.update_trip("Start_Lat", self.start_lat)
		self.update_trip("Start_Lon", self.start_lon)
		self.update_trip("Status", self.status)
		
	def end_trip(self, lat=None, lon=None):
		current_lat, current_lon = get_current_location()
		self.end_time = time.strftime("%H:%M:%S", time.localtime())
		self.end_lat = lat
		self.end_lon = lon
		self.status = 3
		print(self.start_time, self.end_time)
		self.actual_duration = calc_duration(self.start_time, self.end_time)
		self.actual_distance = get_dist(self.start_lat, self.start_lon, self.end_lat, self.end_lon)
		self.toll_cost = 0
		_mile, _min = get_per_min_mile(self.bid_id)
		print(Decimal(_min))
		self.total_cost = (Decimal(self.actual_duration) * Decimal(_min)) + (Decimal(self.actual_distance) * Decimal(_mile)) 
	
		self.update_trip("End_Time", self.end_time)
		self.update_trip("End_Lat", self.end_lat)
		self.update_trip("End_Lon", self.end_lon)
		self.update_trip("Actual_Distance", self.actual_distance)
		self.update_trip("Actual_Duration", self.actual_duration)
		self.update_trip("Toll_Cost", self.toll_cost)
		self.update_trip("Total_Cost", self.total_cost)
		self.update_trip("Status", self.status)
		
	
		
		
