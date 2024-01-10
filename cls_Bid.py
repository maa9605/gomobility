from db_util import get_dataset, insert_record
from cls_Trip import Trip
class Bid:

	def __init__(self, trip_request_id, driver_id, est_pickup, est_cost, status):
		
		self.trip_request_id = trip_request_id
		self.driver_id = driver_id
		self.est_pickup = est_pickup
		self.est_cost = est_cost
		self.status = status
		
		
	def add_bid(self):
	
		sql = "INSERT INTO tbl_Bids(Driver_Id, Request_ID, Est_Pickup_Time, Est_Cost, Status) Values(%s, %s, %s, %s, %s)"
		vals = (self.driver_id, self.trip_request_id, str(self.est_pickup), str(self.est_cost), str(self.status))
		
		self.bid_id = insert_record(sql,vals)
		
	
