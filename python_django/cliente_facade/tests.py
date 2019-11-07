from django.test import TestCase
from .models import Client

class ClientTest(TestCase):

    def setUp(self):
        Client.objects.create(name = "Teste")

    def test_client_create(self):
        client_teste = Client.objects.get(name="Teste")
        self.assertEqual(client_teste.get_name(), "Teste")
