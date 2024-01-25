import time,requests,json,mysql.connector, geocoder
from db_util import get_dataset, get_geo_dataset, insert_record, update_record, get_record, get_proc
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
	


def bid_exists(driver_id, trip_request_id):

	sql = "SELECT EXISTS(SELECT tbl_Bids.Bid_ID FROM tbl_Bids WHERE tbl_Bids.Driver_ID=%s AND tbl_Bids.Request_ID=%s)"
	vals = (driver_id, trip_request_id)
	
	myresult = get_record(sql,vals)
	
	return myresult[0]

def driver_status(driver_id):

	sql = "SELECT Status FROM tbl_Driver_Sessions WHERE Driver_ID=%s"
	vals = (driver_id)
	
	myresult = get_record(sql,vals)
	
	return myresult[0]

def get_active_trip_requests():
	
	sql = "SELECT * FROM tbl_Trip_Request WHERE Status=%s"
	vals = (1)
	
	myresult = get_dataset(sql,vals)
	
	return myresult
	
	
#########################################################
#		GO Mobility System Service Sim          #
#							#
#		System service that handles request	#
#		between the Rider and Driver		#
#########################################################

####Check for Trip Requests

while True: 
	sql = "proc_Get_Drivers"
	_radius = 5
	_maxbids = 5
		
	radius = 1
	found_bids = 0

	while radius <= _radius and found_bids < _maxbids: 
		
		open_trip_requests = get_proc(sql,radius)
		
		found_bids = len(open_trip_requests)
		radius +=1

	if len(open_trip_requests) > 0:
		for row in open_trip_requests:
			if bid_exists(row[5], row[0]) == 0:
				driver_distance, driver_eta = get_distance_duration(str(row[6]), str(row[7]),str(row[3]), str(row[4]))
				if driver_distance <= row[10]:
					p1 = Bid()
					p1.request_id = str(row[0])
					p1.driver_id = str(row[5])
					p1.per_mile = row[8]	
					p1.per_min = row[9]
					p1.est_pickup = driver_eta
					p1.est_cost = get_distance_cost(str(row[1]), p1.per_mile) + get_duration_cost(str(row[3]), p1.per_min)
					p1.status = 1
					p1.add_bid()
		






	
