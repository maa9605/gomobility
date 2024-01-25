import time
from db_util import get_dataset, get_geo_dataset, insert_record, update_record, get_record, get_proc
from geo_util import get_distance_duration, get_lonlat
from cls_Trip import Trip
from cls_Bid import Bid
from datetime import date

def get_accepted_bids(driver_id):

	sql = "SELECT * FROM tbl_Bids WHERE Driver_ID=%s AND Status=2"
	vals = driver_id
	
	myresult = get_dataset(sql,(vals,))
	
	return myresult



#################################################
#     Go Mobility - Drier Client App Sim     	#
#						#
#	This code simulates what the 		#
#	Driver app would do 			#
#################################################

#get driver info

driver = 1
driver_status = 1

#while driver is online check for available confirmed rides
while driver_status == 1:

	accepted_bids = get_accepted_bids(driver)
	
	if len(accepted_bids) > 0:
		for row in accepted_bids:
			p1 = Bid()
			p1.set_bid(row[0])
			
			print(p1.bid_id, p1.est_cost,p1.est_pickup_time)
			
			confirmed_bid = input("Please choose a bid to confirm: ")

			#Rider Selects Bid
			p1.confirm_bid()
			driver_status = 3

#Driver Confims Bid and Trip is created
p2 = Trip()
p2.add_trip(confirmed_bid)
p2.update_trip("Status", 1)
print("Trip Confirmed!")
response = "No"
while(response != "Yes"):
	response = input("Have you Arrived: type Yes or No  ")

p2.begin_trip()
print("Trip has begun")
response = "No"
while(response != "Yes"):
	response = input("Have you arrived at your destination?")

#Driver Ends Ride Calculates totals and then processes CC
p2.end_trip(34.097470, -117.935500)




