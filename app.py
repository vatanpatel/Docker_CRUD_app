# Let us start with importing all the libraries.

import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS                                     
import yaml                                                     


app = Flask(__name__)                                           # Creating the app
db_config = yaml.load(open('database.yaml'))                    # Saving the database location from the database.yaml file 
app.config['SQLALCHEMY_DATABASE_URI'] = db_config['uri']        # Let's add the database to our app
db = SQLAlchemy(app)                                            # This will help us insert/query from the db
CORS(app)

# Let us define a class with class and instance variables

class Product(db.Model):                                        
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    brand_name = db.Column(db.String(255))
    regular_price_value  = db.Column(db.Numeric)
    offer_price_value = db.Column(db.Numeric)
    currency = db.Column(db.String(255))
    classification_l1 = db.Column(db.String(255))
    classification_l2 = db.Column(db.String(255))
    classification_l3 = db.Column(db.String(255))
    classification_l4 = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    
    def __init__(self, name, brand_name, regular_price_value, offer_price_value, currency, classification_l1, classification_l2, classification_l3, classification_l4, image_url):
        self.name = name
        self.brand_name = brand_name
        self.regular_price_value = regular_price_value
        self.offer_price_value = offer_price_value
        self.currency = currency
        self.classification_l1 = classification_l1
        self.classification_l2 = classification_l2
        self.classification_l3 = classification_l3
        self.classification_l4 = classification_l4
        self.image_url = image_url

    def __repr__(self):
        return '{} {} {} {} {} {} {} {} {} {} {}'.format(self.id, self.name, self.brand_name, self.regular_price_value, self.offer_price_value, self.currency, self.classification_l1,
                                               self.classification_l2, self.classification_l3, self.classification_l4, self.image_url)

# We would render the home.html file @ localhost:5000/ 
# We can edit the content of the home.html file to create any home page.

@app.route('/')
def index():
    return render_template('home.html')

# Now let us start defining methods @ localhost:5000/data
# We define two methods. GET and POST. 
# GET method would require no parameters and would return all the products from our table in the postgresql database.
# The POST method can be used to add product entris in the table. We will be able to input a json format dictionary @ localhost:5000/data and
# our application will add that entry to our database.

@app.route('/data', methods=['POST', 'GET'])
def data():
    
    # POST an entry to the database
    if request.method == 'POST':
        body = request.json
        name = body['name']
        brand_name = body['brand_name']
        regular_price_value = body['regular_price_value']
        offer_price_value = body['offer_price_value']
        currency = body['currency']
        classification_l1 = body['classification_l1']
        classification_l2 = body['classification_l2']
        classification_l3 = body['classification_l3']
        classification_l4 = body['classification_l4']
        image_url = body['image_url']

        data = Product(name, brand_name, regular_price_value, offer_price_value, currency,
                       classification_l1, classification_l2, classification_l3, classification_l4, image_url)
        db.session.add(data)
        db.session.commit()

        return jsonify({
            'status': 'Data is posted to PostgreSQL!',
            'name': name,
            'brand_name': brand_name,
            'regular_price_value': regular_price_value,
            'offer_price_value': offer_price_value,
            'currency': currency,
            'classification_l1': classification_l1,
            'classification_l2': classification_l2,
            'classification_l3': classification_l3,
            'classification_l4': classification_l4,
            'image_url': image_url
        })
    
    # GET all data from database sorted by id
    if request.method == 'GET':
        data = Product.query.order_by(Product.id).all()
        print(data)
        dataJson = []
        for i in np.arange(len(data)):
            dataDict = {
                'id': str(data[i]).split(' ')[0],
                'name': str(data[i]).split(' ')[1],
                'brand_name': str(data[i]).split(' ')[2],
                'regular_price_value': str(data[i]).split(' ')[3],
                'offer_price_value': str(data[i]).split(' ')[4],
                'currency': str(data[i]).split(' ')[5],
                'classification_l1': str(data[i]).split(' ')[6],
                'classification_l2': str(data[i]).split(' ')[7],
                'classification_l3': str(data[i]).split(' ')[8],
                'classification_l4': str(data[i]).split(' ')[9],
                'image_url': str(data[i]).split(' ')[10]
            }
            dataJson.append(dataDict)
        return jsonify(dataJson)

# Now we define 3 more methods @ LOCALHOST:5000/data/<string> 
# We will be able to query an entry using GET method with a specific id entered like: LOCALHOST:5000/data/100
# We will be able to update the data using PUT method. We will require a dictionary similar to POST method to update an entry using it's id. 
# The product with the specific id should be present in the table to update.
# We will also define a method to Delete entries using DELETE method and specifying the product id after /data/


@app.route('/data/<string:id>', methods=['GET', 'DELETE', 'PUT'])
def onedata(id):

    # GET a specific data by id
    if request.method == 'GET':
        data = Product.query.get(id)
        print(data)
        dataDict = {
            'id': str(data).split(' ')[0],
            'name': str(data).split(' ')[1],
            'brand_name': str(data).split(' ')[2],
            'regular_price_value': str(data).split(' ')[3],
            'offer_price_value': str(data).split(' ')[4],
            'currency': str(data).split(' ')[5],
            'classification_l1': str(data).split(' ')[6],
            'classification_l2': str(data).split(' ')[7],
            'classification_l3': str(data).split(' ')[8],
            'classification_l4': str(data).split(' ')[9],
            'image_url': str(data).split(' ')[10]

        }
        return jsonify(dataDict)
        
    # DELETE a data
    if request.method == 'DELETE':
        delData = Product.query.filter_by(id=id).first()
        db.session.delete(delData)
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is deleted from PostgreSQL!'})

    # UPDATE a data by id
    if request.method == 'PUT':
        body = request.json
        new_name = body['name']
        new_brand_name = body['brand_name']
        new_regular_price_value = body['regular_price_value']
        new_offer_price_value = body['offer_price_value']
        new_currency = body['currency']
        new_classification_l1 = body['classification_l1']
        new_classification_l2 = body['classification_l2']
        new_classification_l3 = body['classification_l3']
        new_classification_l4 = body['classification_l4']
        new_image_url = body['image_url']

        editData = Product.query.filter_by(id=id).first()
        editData.name = new_name
        editData.brand_name = new_brand_name
        editData.regular_price_value = new_regular_price_value
        editData.offer_price_value = new_offer_price_value
        editData.currency = new_currency
        editData.classification_l1 = new_classification_l1
        editData.classification_l2 = new_classification_l2
        editData.classification_l3 = new_classification_l3
        editData.classification_l4 = new_classification_l4
        editData.image_url = new_image_url
        db.session.commit()
        return jsonify({'status': 'Data '+id+' is updated from PostgreSQL!'})

# We host this locally at localhost:5000. This is where our container image will run.

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
