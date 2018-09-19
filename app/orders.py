from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from . import models


class Orders(Resource):
    """ Create Request parsing interface for price """

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )

    def get(self):
       """ Get specific order method """
       return {'order': models.orders}

        
    def post(self, order_id):
        """ Place a new Order method """
        order = {
            'order_id': 5,
            'name': 'Queen Latifa',
            'dish': 'Mac cheese',
            'price': 1250.00,
            'address': 'Gigiri'
        }
        models.orders.append(order)
        return order, 201

        
    def put(self, order_id):
        '''Upadate status of a specific order method'''

        data = Orders.parser.parse_args()

        order = next(filter(lambda x: x['order_id'] == order_id, models.orders), None)
        if order is None:
            order = {
                'order_id': order_id,
                'name': data['name'],
                'type': data['type'],
                'price': data['price'],
                'address': data['address']
            }
            models.orders.append(order)
        else:
            order.update(data)
        return order

        


