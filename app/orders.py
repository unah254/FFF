from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from models import orders


class Orders(Resource):
    """ Create Request parsing interface for price """

    parser = reqparse.RequestParser()
    parser.add_argument(
        'price',
        type=float,
        required=True,
        help="This field cannot be left blank"
    )



    """ Get specific order method """

    def get(self, order_id):
        if next(filter(lambda x: x['order_id'] == order_id, orders), None):
            return {'order': Orders}, 200 if Orders else 404

        """ Place a new Order method """
    def post(self, order_id):
        order = {
            'order_id': 5,
            'name': 'Queen Latifa',
            'dish': 'Mac cheese',
            'price': 1250.00,
            'address': 'Gigiri'
        }
        orders.append(order)
        return order, 201

        #Upadate status of a specific order method 
    def put(self, order_id):

        data = Orders.parser.parse_args()

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

        


