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

	def set_trip_request(self):
	
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
				
	def pull_bids(self, _radius, _maxbids):
	
		radius = 1
		found_bids = 0
		
		while radius <= _radius and found_bids < _maxbids: 
			sql = "SELECT * FROM Active_Drivers WHERE (ST_Distance_Sphere(point(Active_Drivers.Location_Lon, Active_Drivers.Location_Lat), point(" + str(self.start_lon) + ", " + str(self.start_lat) + ")) * .000621371192) <= " + str(radius) + ";" 
		
			myresult = get_geo_dataset(sql)
			
			found_bids = len(myresult)
			radius +=1
		
		if len(myresult) > 0:
		
			msg = str(len(myresult)) + " Bids Created for this Request"

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
				if driver_distance <= row[5]:
					p1.add_bid()
					
		else:
			msg = "No Drivers Found Near You"
		
		return len(myresult), msg
	
	def accept_bid(self, bid_id):
		
		sql = "UPDATE tbl_Bids SET Status = %s WHERE Bid_ID=%s"
		vals = (2, bid_id)
		
		update_record(sql, vals)
	
	def get_bids(self, _sort):
	
		sql = "SELECT * from tbl_Bids WHERE Request_ID=%s ORDER BY " + _sort + ";"
		vals = (self.trip_request_id)
		
		myresult = get_dataset(sql,vals)
	
		px = []
		for row in myresult:
			px.append(Bid())
			px[myresult.index(row)].set_bid(row[0])
			
		return px

	def update_trip_request(self, name, value):
	
		sql = "UPDATE tbl_Trip_Request SET " + name + " = %s WHERE Request_ID=%s"
		vals = (value, self.trip_id)
		
		update_record(sql, vals)
		
		
		
		
		
		
	
	
