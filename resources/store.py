import uuid
from flask import request
from db import stores

from flask_smorest import Blueprint,abort
from flask.views import MethodView

blp = Blueprint( "stores",__name__,description = "operations on stores")

@blp.route('/store/<string:store_id>')
class Store (MethodView):
    def get (self,store_id):
        try :
                return stores[store_id]
        except KeyError :             
                abort(404,message='Store not found')

    def delete (self,store_id):
        try :
            temp_store = stores[store_id]
            del stores[store_id]
            return {'message': 'Store Silindi','Deleted store':temp_store}
        except :
            abort(404,message='Store not found')

@blp.route('/store')
class StoreList (MethodView):
    def get(self):
        return {'stores' : list(stores.values())}
    
    def post(self):
        data = request.get_json()
        if 'name' not in data :           
           abort(400,message='name parametresini girin')
        for store in stores.values():
             if  data['name'] == store['name']  :
                 abort(400,message='bu isimli store mevcut')

        new_store = { 'name' :data['name'] , 'items' : []  }
        store_id  = uuid.uuid4().hex
        new_store = {**data,'id':store_id}
        stores[store_id] = new_store
        return new_store,201