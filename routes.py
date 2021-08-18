from flask import render_template,request,url_for,jsonify,redirect
from bikestore import  app,db,bcrypt
from bikestore.models import Bike_order,Bike_inventory
# dictionary defined globally
bike_details = {}
bike_list = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/name/<name>")
def display_name(name):
    return f"Name from url {name}"

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/details" , methods=['GET','POST'])
def details():
    # global bike_details
    # bike_details[request.form['bike_name']] = request.form['bike_price']
    #bike_list.append(bike_details)
    return render_template("bike_details_add.html")

@app.route("/bikedetails")
def bikedetails():
    bikes = Bike_inventory.query.all()
    for bike in bikes:
      bike_details[bike.bike_name] = {"Bike_name ": bike.bike_name,
                                      "Bike_price ": bike.base_price,
                                      "Bike_chassis_no":bike.bike_chassis_number,
                                      "Bike_model": bike.bike_model,
                                      "Bike_count": bike.bike_count,
                                     }

    return jsonify(bike_details)


@app.route("/deletebike/<name>", methods=['DELETE'])
def delete_bike(name):
    if name in bike_details.keys():
        bike_details.pop(name)
        return jsonify(f"Bike details of {name} deleted")
    else:
        return "Invalid bike name"


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
    print(id)
    bike = Bike_inventory.query.filter_by(id = bikeid).first()
    if request.method == 'POST':
        bike.bike_name = request.form['bikename']
        bike.bike_model = request.form['bikemodel']
        bike.bike_chassis_number = request.form['bikechassisno']
        bike.bike_price = request.form['baseprice']
        bike.bike_count = request.form['bikecount']

        db.session.commit()

        return redirect(url_for('bike_details_display'))

    return render_template('bike_details_update.html',bike=bike)




# 4. Pass selected value to update page
@app.route("/details/update/getvalue", methods=['PUT', 'POST'])
def update_bike_values():
    bike = Bike_inventory.query.filter_by(id=request.form['bikevalue']).first()

    return render_template('bike_details_update.html',bikedata=bike)


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




