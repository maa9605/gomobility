import time
from geo_util import get_distance_duration, get_lonlat
from db_util import get_dataset, insert_record, update_record
from cls_Trip_Request import Trip_Request
from cls_Trip import Trip
from datetime import date

def trip_status(trip_request_id, status):

	sql = "SELECT * FROM tbl_Trips WHERE Trip_Request_ID =%s AND Status=%s"
	vals = trip_request_id, status
	
	myresult = get_dataset(sql,vals)
	
	return myresult


#################################################
#     Go Mobility - Rider Client App Sim     	#
#						#
#	This code simulates what the 		#
#	Rider app would do 			#
#################################################


##### TEST CASES ###########
#val = input("Pickup Location: ")
#val2 = input("Where are you going: ")
#val="1514 Mohave Drive Colton CA"
#val = "4775 Irwindale Ave Irwindale CA"
val="435 E Hospitality Lane San Bernardino CA"
val2 = "4775 Irwindale Ave Irwindale CA"
#val2="762 E 29th Street San Bernardino CA"
#val2="333 E Columbia Avenue Pomona CA"
#val2="333 E Columbia Avenue Pomona CA"

#Rider Requests Ride
p1 = Trip_Request()
p1.rider_id = 2
p1.date = date.today()
p1.time = time.strftime("%H:%M:%S", time.localtime())
p1.start_lat, p1.start_lon = get_lonlat(val)
p1.end_lat, p1.end_lon = get_lonlat(val2)
p1.distance, p1.duration = get_distance_duration(p1.start_lat, p1.start_lon,p1.end_lat, p1.end_lon)
p1.status = 1
p1.add_trip_request()
print("Trip Request Created")

#App Waits then gets auto generated bids from system
time.sleep(1)
bids = p1.get_bids("Est_Cost")
for i in bids:
	print(bids[bids.index(i)].bid_id, bids[bids.index(i)].est_cost, bids[bids.index(i)].est_pickup_time)
	
#Rider chooses bid to accept
accepted_bid = input("Please choose a bid to accept: ")

#Rider Selects Bid
p1.accept_bid(accepted_bid)

time.sleep(2)

count = 0
while len(trip_status(p1.trip_request_id, 1)) == 0:

	print("Waiting for Driver to Confirm " + str(count))
	count +=1
	time.sleep(10)
	
print("Driver Has Confirmed, your driver will arrive shortly")

count = 0
while len(trip_status(p1.trip_request_id, 2)) == 0:

	print("Waiting for Driver to Arrive " + str(count))
	count +=1
	time.sleep(10)
	
print("Your Driver Has Arrived")

#Ride Ends
print("Your Ride has Ended")


