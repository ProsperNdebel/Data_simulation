
import unittest
from flask import Flask
from app import home, plot_data, simulate_data, pick_data_type, app, fetch_forex_data


class TestApp(unittest.TestCase):

    def setUp(self):
        # Creating a test Flask application
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_route(self):
        # Testing the home route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_plot_data_route(self):
        # Testing the plot_data route
        response = self.client.get('/plot_data')
        self.assertEqual(response.status_code, 200)

    def test_simulate_data_route(self):
        # Testing the simulate_data route
        response = self.client.get('/simulate_data')
        self.assertEqual(response.status_code, 200)

    def test_pick_data_type_route(self):
        # Testing the pick_data_type route
        response = self.client.get('/pick_data_type')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
