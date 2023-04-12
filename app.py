from flask import Flask,request
from db import stores,items
app = Flask(__name__)

# stores = [

#     {

# 'name' : 'My store',
# 'items':  { 
               
#                'name' : 'My item',
#                'my price' : 15.99

#           }

#     }
# ]

@app.get('/store')
def hello():
    return {'stores' : stores}

@app.post('/store')
def create_store() :
    data = request.get_json()
    new_store = { 'name' :data['name'] , 'items' : []  }
    stores.append (new_store)
    return new_store,201

@app.post('/store/<string:name>/item')
def create_item(name):
    data = request.get_json()
    for store in stores :
        if store['name'] == name :
            new_item = { 'name' :data['name'] , 'price' : data['price']  }
            store['items'].append(new_item)
            return new_item ,201
    
    return {'message': 'Store not found'},404


@app.get('/store/<string:name>')
def get_store (name):
    for store in stores :
        if store['name'] == name :
            return store
    return {'message': 'Store not found'},404

        
@app.get('/store/<string:name>/item')
def get_item_in_store (name):
    for store in stores :
        if store['name'] == name :
            return {'items': store['items']}
    return {'message': 'Store not found'},404