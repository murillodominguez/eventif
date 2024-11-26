from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r

class ContactPostValid(TestCase):
    def setUp(self):
        data = dict(name="Cleber Fonseca",
                    email='profcleberfonseca@gmail.com', phone='53-12345-6789', message="Olá, estou entrando em contato")
        self.client.post(r('contact:new'), data)
        self.email = mail.outbox[0]

    def test_contact_email_subject(self):
        expect = 'Novo contato recebido!'
        self.assertEqual(expect, self.email.subject)

    def test_contact_email_from(self):
        expect = 'contato@eventif.com.br'
        self.assertEqual(expect, self.email.from_email)

    def test_contact_email_to(self):
        expect = ['contato@eventif.com.br', 'profcleberfonseca@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_contact_email_body(self):
        contents = (
            'Cleber Fonseca', 'profcleberfonseca@gmail.com', '53-12345-6789', 'Olá, estou entrando em contato'
        )
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)