from flask import Flask, request
from flask_restful import Resource

from models import orders


class Orders(Resource):

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


