from db_util import get_dataset, insert_record
from cls_Trip import Trip
class Bid:

	def get_bid(bid_id):
	
		sql = "SELECT * FROM tbl_Bids WHERE Bid_ID=%s;"
			
		vals = (str(trip_request_id))
		
		myresult = get_dataset(sql,vals)
			
		for row in myresult:
			
			self.driver_id = row[2]
			self.request_id = row[3]
			self.per_mile = row[4]
			self.per_min = row[5]
			self.est_cost = row[6]
			self.est_pickup_time = row[7]
			self.status = row[8]
		
	def add_bid(self):
	
		sql = "INSERT INTO tbl_Bids(Driver_Id, Request_ID, Per_Mile, Per_Min, Est_Pickup_Time, Est_Cost, Status) Values(%s, %s, %s, %s, %s, %s, %s)"
		vals = (self.driver_id, self.request_id, self.per_mile, self.per_min, str(self.est_pickup), str(self.est_cost), str(self.status))
		
		self.bid_id = insert_record(sql,vals)
		
	def update_bid(self, name, value):
	
		sql = "UPDATE tbl_Bids SET " + name + " = %s WHERE Bid_ID=%s"
		vals = (value, self.bid_id)
		
		update_record(sql, vals)
		
	def accept_bid(self, bid_id):
	
		pass
		

	
		
		
	
