from flask import Flask,request
from db import stores,items
import uuid
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
def get_stores():
    return {'stores' : list(stores.values())}

@app.get('/item')
def get_items():
    return {'items' : list(items.values())}

@app.post('/store')
def create_store() :
    data = request.get_json()
    new_store = { 'name' :data['name'] , 'items' : []  }
    store_id  = uuid.uuid4().hex
    new_store = {**data,'id':store_id}
    stores[store_id] = new_store
    return new_store,201

@app.post('/item')
def create_item():
    data = request.get_json()
    if data ['store_id'] not in stores :
          return {'message': 'Store not found'},404
    item_id = uuid.uuid4().hex
    new_item = {**data,'id':item_id}
    items[item_id] = new_item
    return new_item,201

    


@app.get('/store/<string:store_id>')
def get_store (store_id):
    try :
            return stores[store_id]
    except KeyError :

        return {'message': 'Store not found'},404





        
@app.get('/item/<string:item_id>')
def get_item_in_store (item_id):
    try :
        
            return items[item_id]
    except KeyError :
        return {'message': 'Store not found'},404
