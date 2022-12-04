from django.test import TestCase
from django.test import Client

from yard_capacity.models import Yardtracks, Testyard, create

class CatalogTestCase(TestCase):

    def test_stringify(self):
        self.print_state("Starting test_stringify()")
        yard = Testyard.objects.get(id=1)
        result = str(yard)
        self.assertIn(f"{yard.sbdv_name.id}", result)

        self.print_state("Finished test_stringify()")

    def test_listing(self):
        self.print_state("Starting test_listing()")

        response = self.client.get('/yard_capacity/list_tracks_api/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(response.context["yard"]))

        self.print_state("Finished test_listing()")