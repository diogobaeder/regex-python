import re
from unittest2 import TestCase

from nose.tools import istest


class RegexTest(TestCase):
    @istest
    def uma_letra(self):
        self.assertIsNotNone(re.search('a', 'a'))

    @istest
    def uma_letra_maiuscula(self):
        self.assertIsNotNone(re.search('A', 'A'))

    @istest
    def outra_letra(self):
        self.assertIsNotNone(re.search('b', 'b'))

    @istest
    def uma_letra_reservada(self):
        self.assertIsNotNone(re.search(r'\\', '\\'))

    @istest
    def outra_letra_reservada(self):
        self.assertIsNotNone(re.search(r'\$', '$'))

    @istest
    def varias_letras(self):
        self.assertIsNotNone(re.search('abcdefg', 'abcdefg'))