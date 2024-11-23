from django.test import TestCase
from contact.models import Contact
from datetime import datetime

class ContactModelTest(TestCase):
    def setUp(self):
        self.obj = Contact(
            name='Cleber Fonseca',
            email='profcleberfonseca@gmail.com',
            phone='53-12345-6789',
            message='Olá, estou entrando em contato'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_created_at(self):
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Cleber Fonseca', str(self.obj))