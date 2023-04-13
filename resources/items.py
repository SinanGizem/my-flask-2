import uuid
from flask import request
from flask_smorest import Blueprint,abort
from flask.views import MethodView
from db import items


blp = Blueprint( "items",__name__,description = "operations on items")

@blp.route('/item/<string:item_id>')
class Item (MethodView):
    
    def get (self,item_id):
     try :
          return items[item_id]
     except KeyError :
         abort(404,message='Store not found')

    def delete (self,item_id):
        try :
            del items[item_id]
            abort(400,message='İtem Silindi')
        except :
           abort(400,message='bu item yok')
   
    def put (self,item_id):
        data = request.get_json()
        if ('price' not in data or   'name' not in data ) :
            abort(400,message='Message lütfen name  , price giriniz')
        try : 
            item = items[item_id]
            item |= data
            return item,200

        except KeyError : 
            abort ( 400,message='item bulunamadı')


@blp.route('/item')
class ItemList (MethodView):

    def get (self):
         return {'items' : list(items.values())}
    def post (self):
        data = request.get_json()
        if ('price' not in data or 'store_id' not in data  or 'name' not in data ) :
            abort(400,'Message lütfen name ,storeid , price giriniz')
    
        for item in items.values():
            if (data['name'] == item['name'] and  data['store_id'] == item['store_id'] ):
                abort(400,'bu items var')

        item_id = uuid.uuid4().hex
        new_item = {**data,'id':item_id}
        items[item_id] = new_item
        return new_item,201