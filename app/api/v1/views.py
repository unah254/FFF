from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from app.api.v1.models import orders


class Orders(Resource):
   

    def get(self):
       """ Get all orders method """
       return {'order': orders}

class Order(Resource):
    """ Create Request parsing interface for price """

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )
    
    def get(self, order_id):
        """ Get a specific Order method """
        order = next(filter(lambda x: x['order_id'] == order_id, orders), None)
        return {'order': order}, 200 if order else 404

        
    def post(self, order_id):
        """ Place a new Order method """
        order = {
            'order_id': 5,
            'name': 'Queen Latifa',
            'dish': 'Mac cheese',
            'price': 1250.00,
            'address': 'Gigiri'
        }
        orders.append(order)
        return order, 201

        
    def put(self, order_id):
        '''Upadate status of a specific order method'''

        data = Order.parser.parse_args()

        order = next(filter(lambda x: x['order_id'] == order_id, orders), None)
        if order is None:
            order = {
                'order_id': order_id,
                'name': data['name'],
                'type': data['type'],
                'price': data['price'],
                'address': data['address']
            }
            orders.append(order)
        else:
            order.update(data)
        return order

       

    def delete(self, order_id):
        """ delete an order method"""
        global orders
        orders = list(filter(lambda x: x['order_id'] != order_id, orders))
        return {'message': 'Deleted'}, 200

        


