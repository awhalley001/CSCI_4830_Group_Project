from django.test import TestCase

class HomeTestCase(TestCase):
    def test_home(self):
        response = self.client.get('/yard_capacity/home/')
        self.assertEqual(200, response.status_code)

        response = self.client.get('/yard_capacity/list_tracks_api/')
        self.assertEqual(200, response.status_code)

        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
