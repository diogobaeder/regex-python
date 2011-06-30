import re
from unittest2 import TestCase

from nose.tools import istest


class RegexTest(TestCase):
    @istest
    def duas_letras(self):
        self.assertIsNone(re.search('[^ab]', 'a'))
        self.assertIsNone(re.search('[^ab]', 'b'))

        self.assertIsNotNone(re.search('[^ab]', 'c'))

    @istest
    def duas_letras_seguidas_por_outra(self):
        self.assertIsNone(re.search('[^ab]d', 'ad'))
        self.assertIsNone(re.search('[^ab]d', 'bd'))

        self.assertIsNotNone(re.search('[^ab]d', 'cd'))

    @istest
    def tres_letras_seguidas_por_outra(self):
        self.assertIsNone(re.search('[^abc]d', 'ad'))
        self.assertIsNone(re.search('[^abc]d', 'bd'))
        self.assertIsNone(re.search('[^abc]d', 'cd'))

        self.assertIsNotNone(re.search('[^abc]d', ' d'))

    @istest
    def conjuntos_pre_definidos_nao_numeros(self):
        self.assertIsNone(re.search(r'\D', '1'))
        self.assertIsNone(re.search(r'\D', '4'))
        self.assertIsNone(re.search(r'\D', '5'))

        self.assertIsNotNone(re.search(r'\D', ' '))

    @istest
    def conjuntos_pre_definidos_nao_numeros_seguidos_por_letras(self):
        self.assertIsNone(re.search(r'\Da', '1a'))
        self.assertIsNone(re.search(r'\Da', '4a'))
        self.assertIsNone(re.search(r'\Da', '5a'))

        self.assertIsNotNone(re.search(r'\Da', '$a'))

    @istest
    def conjuntos_pre_definidos_nao_numeros_e_letras(self):
        self.assertIsNone(re.search(r'[^\da]', '1'))
        self.assertIsNone(re.search(r'[^\da]', '4'))
        self.assertIsNone(re.search(r'[^\da]', '5'))
        self.assertIsNone(re.search(r'[^\da]', 'a'))

        self.assertIsNotNone(re.search(r'[^\da]', 'A'))

    @istest
    def conjuntos_pre_definidos_caracteres_nao_brancos(self):
        self.assertIsNone(re.search(r'\S', ' '))
        self.assertIsNone(re.search(r'\S', '\t'))
        self.assertIsNone(re.search(r'\S', '\n'))
        self.assertIsNone(re.search(r'\S', '\r'))
        self.assertIsNone(re.search(r'\S', '\f'))

        self.assertIsNotNone(re.search(r'\S', 'A'))

    @istest
    def conjuntos_pre_definidos_caracteres_nao_brancos_seguidos_por_letras(self):
        self.assertIsNone(re.search(r'\Sa', ' a'))
        self.assertIsNone(re.search(r'\Sa', '\ta'))
        self.assertIsNone(re.search(r'\Sa', '\na'))

        self.assertIsNotNone(re.search(r'\Sa', '9a'))

    @istest
    def conjuntos_pre_definidos_caracteres_nao_brancos_e_letras(self):
        self.assertIsNone(re.search(r'[^\sa]', ' '))
        self.assertIsNone(re.search(r'[^\sa]', '\t'))
        self.assertIsNone(re.search(r'[^\sa]', '\n'))
        self.assertIsNone(re.search(r'[^\sa]', 'a'))

        self.assertIsNotNone(re.search(r'[^\sa]', 'Z'))

    @istest
    def conjuntos_pre_definidos_nao_letras_nem_numeros(self):
        self.assertIsNone(re.search(r'\W', 'a'))
        self.assertIsNone(re.search(r'\W', 'B'))
        self.assertIsNone(re.search(r'\W', '9'))

        self.assertIsNotNone(re.search(r'\W', ' '))

    @istest
    def conjuntos_pre_definidos_nao_letras_nem_numeros_seguidos_por_letras(self):
        self.assertIsNone(re.search(r'\Wp', 'ap'))
        self.assertIsNone(re.search(r'\Wp', 'Bp'))
        self.assertIsNone(re.search(r'\Wp', '9p'))

        self.assertIsNotNone(re.search(r'\Wp', '$p'))
