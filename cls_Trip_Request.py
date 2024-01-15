import time,requests,json,mysql.connector, geocoder
from db_util import get_dataset, get_geo_dataset, insert_record, update_record
from geo_util import get_distance_duration, get_lonlat
from decimal import Decimal
from cls_Bid import Bid
from datetime import date

def get_distance_cost(distance, per_unit):
	_cost = round(Decimal(distance) * per_unit,2)
	return _cost
	
def get_duration_cost(duration, per_unit):
	_cost = round(Decimal(duration) * per_unit,2)
	return _cost

class Trip_Request:

	def __init__(self, rider_id=None, pickup=None, destination=None, trip_request_id=None):
	
		if trip_request_id == None: 
		
			self.rider_id = rider_id
			self.date = date.today()
			self.time = time.strftime("%H:%M:%S", time.localtime())
			self.start_lat, self.start_lon = get_lonlat(pickup)
			self.end_lat, self.end_lon = get_lonlat(destination)
			self.distance, self.duration = get_distance_duration(self.start_lat, self.start_lon,self.end_lat, self.end_lon)
			self.status = 1
		else:
			sql = "SELECT * FROM tbl_Trip_Request WHERE Request_ID=%s;"
			vals = (str(trip_request_id))
		
			myresult = get_dataset(sql,vals)
			
			for row in myresult:
				self.trip_request_id = row[0]
				self.rider_id = row[1]
				self.start_lat = row[2]
				self.start_lon = row[3]
				self.end_lat = row[4]
				self.end_lon = row[5]
				self.timestamp = row[6]
				self.distance = row[7]
				self.duration = row[8]
				self.status = row[9]
				
	def add_trip_request(self):

		sql = "INSERT INTO tbl_Trip_Request(Rider_ID, Start_Lat, Start_Lon, End_Lat, End_Lon, Est_Distance, Est_Duration, Status) Values(%s, %s, %s, %s, %s, %s, %s, %s)"
		vals = (self.rider_id, self.start_lat, self.start_lon, self.end_lat, self.end_lon, str(self.distance), str(self.duration), str(self.status))
		
		self.trip_request_id = insert_record(sql,vals)
				
	def pull_bids(self):
		
		radius = 50
		
		sql = "SELECT * FROM Active_Drivers WHERE (ST_Distance_Sphere(point(Active_Drivers.Location_Lon, Active_Drivers.Location_Lat), point(" + str(self.start_lon) + ", " + str(self.start_lat) + ")) * .000621371192) <= " + str(radius) + ";" 
		
		myresult = get_geo_dataset(sql)

		for row in myresult:
			driver_distance, driver_eta = get_distance_duration(str(row[1]), str(row[2]),self.start_lat, self.start_lon)
			p1 = Bid()
			p1.request_id = self.trip_request_id
			p1.driver_id = str(row[0])
			p1.per_mile = row[3]
			p1.per_min = row[4]
			p1.est_pickup = driver_eta
			p1.est_cost = get_distance_cost(self.distance, p1.per_mile) + get_duration_cost(self.duration, p1.per_min)
			p1.status = 1
			p1.add_bid()
	
	def accept_bid(self, bid_id):
		
		sql = "UPDATE tbl_Bids SET Status = %s WHERE Bid_ID=%s"
		vals = (2, bid_id)
		
		update_record(sql, vals)
	
	def get_bids(self):
	
		sql = "SELECT * FROM tbl_Bids WHERE Request_ID = %s"
		vals = (self.trip_request_id)
		
		myresult = get_dataset(sql, vals)
		
		for row in myresult:
			print(str(row[0]), str(row[2]), str(row[6]), str(row[7]))
	
	def update_trip_request(self, name, value):
	
		sql = "UPDATE tbl_Trip_Request SET " + name + " = %s WHERE Request_ID=%s"
		vals = (value, self.trip_id)
		
		update_record(sql, vals)
		
		
		
		
		
		
	
	
