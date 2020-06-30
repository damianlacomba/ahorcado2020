import unittest

from ahorcado import Juego


class AhorcadoTest(unittest.TestCase):
    def setUp(self):
        self.juego = Juego()

    def test_letras_correctas(self):
        self.assertEqual("ganador", self.juego.jugar())

   
