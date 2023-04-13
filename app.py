from flask import Flask,request

from flask_smorest import Api
from resources.store import blp as Storedblp
from resources.items import blp as Itemblp

app = Flask(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api= Api(app)

api.register_blueprint(Storedblp)
api.register_blueprint(Itemblp)

















# # stores = [

# #     {

# # 'name' : 'My store',
# # 'items':  { 
               
# #                'name' : 'My item',
# #                'my price' : 15.99

# #           }

# #     }
# # ]

# @app.get('/store')
# def get_stores():
#     return {'stores' : list(stores.values())}

# @app.get('/item')
# def get_items():
#     return {'items' : list(items.values())}

# @app.post('/store')
# def create_store() :
#     data = request.get_json()
#     if 'name' not in data :
#          return {'message': 'name parametresini girin'}
#     for store in stores.values():
#         if  data['name'] == store['name']  :
#             return {'message': 'bu isimli store mevcut'}

#     new_store = { 'name' :data['name'] , 'items' : []  }
#     store_id  = uuid.uuid4().hex
#     new_store = {**data,'id':store_id}
#     stores[store_id] = new_store
#     return new_store,201

# @app.post('/item')
# def create_item():
#     data = request.get_json()
#     if ('price' not in data or 'store_id' not in data  or 'name' not in data ) :
#         return {'message':'Message lütfen name ,storeid , price giriniz'}
    
#     for item in items.values():
#         if (data['name'] == item['name'] and  data['store_id'] == item['store_id'] ):
#             return {'message':'bu items var'}

#     if data ['store_id'] not in stores :
#           return {'message': 'Store not found'},404
#     item_id = uuid.uuid4().hex
#     new_item = {**data,'id':item_id}
#     items[item_id] = new_item
#     return new_item,201

    


# @app.get('/store/<string:store_id>')
# def get_store (store_id):
#     try :
#             return stores[store_id]
#     except KeyError :

#         return {'message': 'Store not found'},404





        
# @app.get('/item/<string:item_id>')
# def get_item_in_store (item_id):
#     try :
        
#             return items[item_id]
#     except KeyError :
#         return {'message': 'Store not found'},404


# @app.delete('/item/<string:item_id>')
# def delete_item(item_id):
#     try :
#          del items[item_id]
#          return {'message': 'Silindi'}
#     except :
#           return {'message': 'bu item yok'}


# @app.delete('/store/<string:store_id>')
# def delete_store(store_id):
#     try :
#          del stores[store_id]
#          return {'message': 'Silindi'}
#     except :
#           return {'message': 'bu item yok'}






# @app.put('/item/<string:item_id>')
# def update_item(item_id):
#     data = request.get_json()
#     if ('price' not in data or   'name' not in data ) :
#         return {'message':'Message lütfen name  , price giriniz'}
#     try : 
#         item = items[item_id]
#         item |= data
#         return item,200

#     except KeyError : 
#         return {'message':'item bulunamadı'}




#     for item in items.values():
#         if (data['name'] == item['name'] and  data['store_id'] == item['store_id'] ):
#             return {'message':'bu items var'}

    
