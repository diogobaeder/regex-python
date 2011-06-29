import re
from unittest2 import TestCase

from nose.tools import istest


class RegexTest(TestCase):
    @istest
    def duas_letras(self):
        self.assertIsNotNone(re.search('[ab]', 'a'))
        self.assertIsNotNone(re.search('[ab]', 'b'))

    @istest
    def duas_letras_seguidas_por_outra(self):
        self.assertIsNotNone(re.search('[ab]d', 'ad'))
        self.assertIsNotNone(re.search('[ab]d', 'bd'))

    @istest
    def tres_letras_seguidas_por_outra(self):
        self.assertIsNotNone(re.search('[abc]d', 'ad'))
        self.assertIsNotNone(re.search('[abc]d', 'bd'))
        self.assertIsNotNone(re.search('[abc]d', 'cd'))

    @istest
    def intervalo(self):
        self.assertIsNotNone(re.search('[a-c]', 'a'))
        self.assertIsNotNone(re.search('[a-c]', 'b'))
        self.assertIsNotNone(re.search('[a-c]', 'c'))

    @istest
    def dois_intervalos(self):
        self.assertIsNotNone(re.search('[a-cA-D]', 'a'))
        self.assertIsNotNone(re.search('[a-cA-D]', 'b'))
        self.assertIsNotNone(re.search('[a-cA-D]', 'c'))
        self.assertIsNotNone(re.search('[a-cA-D]', 'A'))
        self.assertIsNotNone(re.search('[a-cA-D]', 'B'))
        self.assertIsNotNone(re.search('[a-cA-D]', 'C'))
        self.assertIsNotNone(re.search('[a-cA-D]', 'D'))

        self.assertIsNone(re.search('[a-cA-D]', 'd'))

    @istest
    def intervalo_de_numeros(self):
        self.assertIsNotNone(re.search('[0-2]', '0'))
        self.assertIsNotNone(re.search('[0-2]', '1'))
        self.assertIsNotNone(re.search('[0-2]', '2'))

        self.assertIsNone(re.search('[0-2]', '3'))

    @istest
    def conjuntos_pre_definidos_numeros(self):
        self.assertIsNotNone(re.search(r'\d', '1'))
        self.assertIsNotNone(re.search(r'\d', '4'))
        self.assertIsNotNone(re.search(r'\d', '5'))

    @istest
    def conjuntos_pre_definidos_numeros_seguidos_por_letras(self):
        self.assertIsNotNone(re.search(r'\da', '1a'))
        self.assertIsNotNone(re.search(r'\da', '4a'))
        self.assertIsNotNone(re.search(r'\da', '5a'))

    @istest
    def conjuntos_pre_definidos_numeros_e_letras(self):
        self.assertIsNotNone(re.search(r'[\da]', '1'))
        self.assertIsNotNone(re.search(r'[\da]', '4'))
        self.assertIsNotNone(re.search(r'[\da]', '5'))
        self.assertIsNotNone(re.search(r'[\da]', 'a'))

    @istest
    def conjuntos_pre_definidos_caracteres_em_branco(self):
        self.assertIsNotNone(re.search(r'\s', ' '))
        self.assertIsNotNone(re.search(r'\s', '\t'))
        self.assertIsNotNone(re.search(r'\s', '\r'))
        self.assertIsNotNone(re.search(r'\s', '\n'))
        self.assertIsNotNone(re.search(r'\s', '\f'))

    @istest
    def conjuntos_pre_definidos_caracteres_em_branco_seguidos_por_letras(self):
        self.assertIsNotNone(re.search(r'\sa', ' a'))
        self.assertIsNotNone(re.search(r'\sa', '\ta'))
        self.assertIsNotNone(re.search(r'\sa', '\na'))

    @istest
    def conjuntos_pre_definidos_caracteres_em_branco_e_letras(self):
        self.assertIsNotNone(re.search(r'[\sa]', 'a'))
        self.assertIsNotNone(re.search(r'[\sa]', '\t'))
        self.assertIsNotNone(re.search(r'[\sa]', '\n'))

    @istest
    def conjuntos_pre_definidos_letras_e_numeros(self):
        self.assertIsNotNone(re.search(r'\w', 'a'))
        self.assertIsNotNone(re.search(r'\w', 'B'))
        self.assertIsNotNone(re.search(r'\w', '9'))

    @istest
    def conjuntos_pre_definidos_letras_e_numeros_seguidos_por_letras(self):
        self.assertIsNotNone(re.search(r'\wp', 'ap'))
        self.assertIsNotNone(re.search(r'\wp', 'Bp'))
        self.assertIsNotNone(re.search(r'\wp', '9p'))

    @istest
    def conjuntos_pre_definidos_quase_todos(self):
        self.assertIsNotNone(re.search('.', 'a'))
        self.assertIsNotNone(re.search('.', 'B'))
        self.assertIsNotNone(re.search('.', '9'))
        self.assertIsNotNone(re.search('.', '$'))
        self.assertIsNotNone(re.search('.', '\t'))
        self.assertIsNotNone(re.search('.', ' '))

        self.assertIsNone(re.search('.', '\n'))
