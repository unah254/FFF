from flask import Flask
from flask_restful import Resource, Api, reqparse

from .validators import Validators


orders = []

class Mealorder:
    
    def __init__(self,name=None,price=None,description=None, status="Pending"):
        self.id=len(orders)+1
        self.name=name
        self.price=price
        self.description=description
        self.status=status
        
    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            status=self.status
        )

    def get_id(self, order_id):
        for order in orders:
            if order.id == order_id:
                return order

class Createmeal(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
    'name',
    type=str,
    required=True,
    help="This field cannot be left blank"
    )

    parser.add_argument(
    'description',
    type=str,
    required=True,
    help="This field cannot be left blank"
    )

    parser.add_argument(
        'price',
        type=int,
        required=True,
        help="This field cannot be left blank!" 
    )

    def post(self):
        ''' place new order'''
        data = Createmeal.parser.parse_args()


        name = data['name']
        description = data['description']
        price = data['price']

        if not Validators().valid_food_name(name):
            return {'message': 'Enter valid name'}, 400
        if not Validators().valid_food_description(description):
            return {'message': 'Enter valid food description'}, 400

        order = Mealorder(name, price, description)

        orders.append(order)

        return {"message":"Dish order placed"}, 201
   
class Orders(Resource):

    def get(self):
        ''' get all orders '''

        return {'orders': [order.serialize() for order in orders]}, 200

class SingleOrder(Resource):
    
    def get(self, id):
        ''' get a specific order '''
        
        order = Mealorder().get_id(id)

        if order:
            return {"order":order.serialize()}
        
        return {'message':"Not found"}, 404
        
    def put(self, id):
        ''' Update order status '''
        order = Mealorder().get_id(id)

        if order:
            if order.status == "Pending":
                order.status = "Accepted"
                return {'message':'Order accepted'}, 200

            if order.status == "Accepted":
                order.status = "Completed"

                return {'message':'Order completed'}, 200

        return {'message':"Not found"}, 404

    def delete(self, id):
        ''' Delete a single order '''

        order = Mealorder().get_id(order_id=id)
        if order:
            orders.remove(order)
            return {'message':"Deleted"}, 200
        return {'message':"Not found"}, 404
  



        


