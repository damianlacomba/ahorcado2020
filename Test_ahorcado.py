import unittest

from ahorcado import Juego


class AhorcadoTest(unittest.TestCase):
    def setUp(self):
        self.juego = Juego()

    def test(self):
        letra="a"
        result= self.juego.validar_letra(letra)
        self.assertEqual(True, result)

   
