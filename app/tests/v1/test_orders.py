import json
import unittest
from unittest import TestCase
from app import create_app

from app.api.v1.views import SingleOrder, Orders, Createmeal
class TestMeals(TestCase):
    '''Test the orders.'''
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.order_data = {
            "name":"Biriani",
            "description":"Chicken Biriani",
            "price":450
        }

    def test_get_all_meals(self):
        ''' Test to get all meals '''

        response = self.client.get(
             "/api/v1/orders", content_type='application/json')

        data = json.loads(response.data.decode('utf-8'))
        print(data)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_place_new_order(self):
        ''' Test to place an order '''

        order_data = {
            "name":"Biriani",
            "description":"Chicken Biriani",
            "price":850
        }

        response = self.client.post(
            "/api/v1/orders",
            data=json.dumps(order_data),
            headers={"content-type":"application/json"}
        )

        response_data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data['message'], "Dish order placed")
    def test_get_single_order(self):
        ''' Test to get single order '''
        
        res = self.client.post(
            "/api/v1/orders",
            data=json.dumps(self.order_data),
            headers={"content-type":"application/json"}
        )
        response = self.client.get(
                "/api/v1/orders/1", content_type='application/json')

        self.assertEqual(response.content_type, 'application/json')
        print(res, response)
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.status_code, 404)

    def test_invalid_meal_description(self):
        ''' Test invalid food description '''

        order_data = {
            "name":"Valimeal",
            "description":"****",
            "price":20
        }

        response = self.client.post(
            "/api/v1/orders",
            data=json.dumps(order_data),
            headers={"content-type":"application/json"}
        )

        response_data = json.loads(response.data.decode('utf-8'))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['message'], "Enter valid food description")
        self.assertNotEqual(response.status_code, 200)
    

    def test_delete_order_not_found(self):
        ''' Test to delete order'''

        response = self.client.post(
            "/api/v1/orders",
            data=json.dumps(self.order_data),
            headers={"content-type":"application/json"}
        )
        response = self.client.delete(
            "/api/v1/orders/1",
            headers={"content-type":"application/json"}
        )
        self.assertEqual(response.status_code, 200)

        self.assertNotEqual(response.status_code, 404)

    def tearDown(self):
        self.app_context.pop()