from django.test import TestCase, Client


class NoteMethodTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_mainpage(self):
        response = self.client.get('')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
