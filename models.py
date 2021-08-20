from bikestore import db

class Bike_inventory(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    bike_name = db.Column(db.String(80),nullable=False)
    bike_model = db.Column(db.String(20),nullable=False)
    bike_chassis_number = db.Column(db.Integer,unique=True,nullable=False)
    base_price = db.Column(db.Integer,nullable=False)
    bike_count = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"{self.bike_name},{self.bike_model},{self.bike_chassis_number},{self.base_price}"

class Bike_order(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    order_bike_name = db.Column(db.String(80),nullable=False)
    order_downpayment = db.Column(db.Integer,nullable=False)
    order_count = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"{self.id},{self.order_bike_name},{self.order_downpayment}"