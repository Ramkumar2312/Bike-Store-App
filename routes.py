from flask import render_template,request,url_for,jsonify,redirect,flash
from bikestore import  app,db,bcrypt
from bikestore.models import Bike_order,Bike_inventory
# dictionary defined globally

@app.route("/")
def home():
    return render_template("home.html")


# 1 . add bikes
@app.route("/details/add",methods=['GET','POST'])
def bike_details_add():
    if request.method == 'POST':
        bike_name = request.form['bike_name']
        bike_model = request.form['bike_model']
        bike_chassis_number = request.form['bike_chassis_no']
        bike_price = request.form['bike_price']
        bike_count = request.form['bike_count']


        bike = Bike_inventory(bike_name=bike_name,bike_model=bike_model,bike_chassis_number=bike_chassis_number, \
                          base_price=bike_price,bike_count=bike_count)

        db.session.add(bike)
        db.session.commit()

        return redirect(url_for('bike_details_display'))
    return render_template("bike_details_add.html")

# 2 . Display all bike details
@app.route("/details/display", methods=['GET','POST'])
def bike_details_display():
    bike = Bike_inventory.query.all()

    return render_template('bike_details_display.html', bikedata=bike)


# 3. select bike details to update
@app.route("/details/update/<bikeid>", methods=['PUT', 'GET','POST'])
def bike_details_update(bikeid):
    bike = Bike_inventory.query.filter_by(id=bikeid).first()
    if request.method == 'POST':
        bike.bike_name = request.form['bikename']
        bike.bike_model = request.form['bikemodel']
        bike.bike_chassis_number = request.form['bikechassisno']
        bike.bike_price = request.form['baseprice']
        bike.bike_count = request.form['bikecount']

        db.session.commit()

        return redirect(url_for('bike_details_display'))

    return render_template('bike_details_update.html',bike=bike)


# 4. Delete bike details
@app.route("/details/delete/<bikeid>", methods=['POST'])
def bike_details_delete(bikeid):
    bike = Bike_inventory.query.filter_by(id=bikeid).first()
    db.session.delete(bike)
    db.session.commit()

    return redirect(url_for('bike_details_display'))


# 1. Create order with customer name and phone number
@app.route("/order/create", methods=['GET','POST'])
def order_create():
    if request.method == 'POST':
        order_bike_name = request.form['bikename']
        order_downpayment = request.form['downpayment']
        order_count = request.form['ordercount']

        order = Bike_order(order_bike_name=order_bike_name,order_downpayment=order_downpayment,order_count=order_count)

        db.session.add(order)
        db.session.commit()
        flash('order created successfully')
        return redirect(url_for('order_display'))

    return render_template('order_create.html')


# 2. Display order details
@app.route("/order/display", methods=['GET','POST'])
def order_display():
    order = Bike_order.query.all()

    return render_template('order_display.html', orders=order)




# 3. Update order , cancel, return
@app.route("/order/delete/<id>", methods=['GET','POST'])
def order_delete(id):
    order = Bike_order.query.filter_by(id=id).first()
    db.session.delete(order)
    db.session.commit()

    return redirect(url_for('order_display'))

'''
add home route link in all apps


'''




'''

bike.base_price = 33000
    db.session.commit()
    
'''


'''
Bike store 

Bike inventory 
    add bikes 
    update bike details
    delete bikes 
    fetch all bike details 
    fetch a single bike details 
    
Bike order 
    create order for customer
    update the status of the order 
        based on inventory availability
        order bike to factory
    cancel the order 
    return order 
    create order with customer name , number.
    
    
customer login
    username, password, mobile number 

admin login 
    username , password 
    
'''




