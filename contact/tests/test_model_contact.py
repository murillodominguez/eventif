from django.test import TestCase
from contact.models import Contact, send_response_notification_email
from datetime import datetime
from django.core import mail

class ContactModelTest(TestCase):
    def setUp(self):
        self.obj = Contact(
            name='Cleber Fonseca',
            email='profcleberfonseca@gmail.com',
            phone='53-12345-6789',
            message='Olá, estou entrando em contato',
            response='Resposta do contato'
        )
        self.obj.save()
        send_response_notification_email(Contact, self.obj)
        self.email = mail.outbox[0]

    def test_create(self):
        self.assertTrue(Contact.objects.exists())

    def test_sent_at(self):
        self.assertIsInstance(self.obj.sent_at, datetime)

    def test_str(self):
        self.assertEqual('Cleber Fonseca', str(self.obj))

    def test_subscription_email_subject(self):
        expect = 'Resposta do seu contato'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventif.com.br', 'profcleberfonseca@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = (
            'Cleber Fonseca',
            'profcleberfonseca@gmail.com',
            '53-12345-6789',
            'Olá, estou entrando em contato',
            'Resposta do contato'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)