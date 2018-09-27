from flask import Flask
from flask_restful import Resource, Api, reqparse
# imported module to validate the inputs
from .validators import Validators

# list to store orders
orders = []


class Mealorder:
    '''meal order class to initialize orders and display in json'''
    def __init__(self, name=None, price=None, description=None, status="Pending"):
        '''create an instance of meal order'''
        self.id = len(orders)+1
        self.name = name
        self.price = price
        self.description = description
        self.status = status

    def serialize(self):
        '''to get created data and display in json format'''
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            description=self.description,
            status=self.status
        )

    def get_id(self, order_id):
        '''display specific order id'''
        for order in orders:
            if order.id == order_id:
                return order


class Createmeal(Resource):
    '''to get input from user and create a new order'''
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

        return {"message": "Dish order placed"}, 201


class Orders(Resource):

    def get(self):
        ''' get all orders '''

        return {'orders': [order.serialize() for order in orders]}, 200


class UpdateStatus(Resource):
    '''class to create status arguments'''
    parser = reqparse.RequestParser()
    parser.add_argument(
        'status',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )


class SingleOrder(Resource):
    '''class to get, update and delete specific order'''

    def get(self, id):
        ''' get a specific order '''

        order = Mealorder().get_id(id)

        if order:
            return {"order": order.serialize()}

        return {'message': "Not found"}, 404

    def put(self, id):
        ''' Update order status '''

        order = Mealorder().get_id(id)
        data = UpdateStatus.parser.parse_args()
        status = data['status']
        if order:
            if status == "Accepted":
                order.status = "Accepted"
                return {'message': 'Order accepted'}, 200

            elif status == "Completed":
                order.status = "Completed"

                return {'message': 'Order completed'}, 200

            elif status == "Declined":
                order.status = "Declined"

                return {'message': 'Order declined'}, 202
                
            elif status == "Pending" or status == "":
                return {'message': 'Please update the order status to either Accepted or Completed'}, 400

        else:
            return {'message': "Not found"}, 404


    def delete(self, id):
        ''' Delete a single order '''

        order = Mealorder().get_id(id)
        if order:
            orders.remove(order)
            return {'message': "Deleted"}, 200
        return {'message': "Not found"}, 404
