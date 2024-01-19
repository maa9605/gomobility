import time, geocoder
from datetime import date
from cls_Trip_Request import Trip_Request
from cls_Trip import Trip
from geo_util import get_distance_duration, get_lonlat

#val = input("Pickup Location: ")
#val2 = input("Where are you going: ")
val="1514 Mohave Drive Colton CA"
#val = "4775 Irwindale Ave Irwindale CA"
#val2="435 E Hospitality Lane San Bernardino CA"
#val2="762 E 29th Street San Bernardino CA"
val2="333 E Columbia Avenue Pomona CA"
#val2="333 E Columbia Avenue Pomona CA"

#Rider Requests Ride
p1 = Trip_Request()
p1.rider_id = 1
p1.date = date.today()
p1.time = time.strftime("%H:%M:%S", time.localtime())
p1.start_lat, p1.start_lon = get_lonlat(val)
p1.end_lat, p1.end_lon = get_lonlat(val2)
p1.distance, p1.duration = get_distance_duration(p1.start_lat, p1.start_lon,p1.end_lat, p1.end_lon)
p1.status = 1
p1.add_trip_request()
print("Trip Request Created")

#System Automatically Receive Bids
print("Searching for Drivers")
bids_amt, message = p1.pull_bids(10,5)

if bids_amt > 0:
	print(message)
	bids = p1.get_bids("Est_Cost")
	
	for i in bids:
		print(bids[bids.index(i)].bid_id, bids[bids.index(i)].est_cost, bids[bids.index(i)].est_pickup_time)

	accepted_bid = input("Please choose a bid to accept: ")

	#Rider Selects Bid
	p1.accept_bid(accepted_bid)

	#Driver Confims Bid and Trip is created
	print("Driver is confirming...")
	p2 = Trip()
	p2.add_trip(accepted_bid)
	p2.update_trip("Status", 1)

	print("Driver has confirmed, please wait for driver to arrive")
	#Driver Confirms Pickup of Rider
	response = "No"
	while(response != "Yes"):
		response = input("Has Driver Arrived: type Yes or No  ")
		
	p2.begin_trip()
	print("Your trip has begun")

	#Driver Confirms Pickup of Rider
	response = "No"
	while(response != "Yes"):
		response = input("Have you arrived at your destination?")

	#Driver Ends Ride Calculates totals and then processes CC
	p2.end_trip(p1.end_lat, p1.end_lon)

else:
	print(message)




