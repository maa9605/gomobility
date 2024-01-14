from cls_Trip_Request import Trip_Request
from cls_Trip import Trip

#val = input("Pickup Location: ")
#val2 = input("Where are you going: ")
val="1514 Mohave Drive Colton CA"
#val2 = "4775 Irwindale Ave Irwindale CA"
val2="435 E Hospitality Lane San Bernardino CA"
#val2="762 E 29th Street San Bernardino CA"
#val2="333 E Columbia Avenue Pomona CA"
#val2="333 E Columbia Avenue Pomona CA"

#Rider Requests Ride
p1 = Trip_Request(1,val,val2)
#p1 = Trip_Request(0,0,0,60)
p1.add_trip_request()
print("Trip Request Created")

#System Automatically Receive Bids
p1.pull_bids()
print("Bids Received")

p1.get_bids()

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
p2.end_trip(34.099174, -117.934244)




