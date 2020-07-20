import unittest
from ahorcado import Juego


class AhorcadoTest(unittest.TestCase):
    def setUp(self):
        self.juego = Juego()
        

    def test_palabra_gato_probarletra_A(self):
        self.juego.set_palabra("gato")
        letra = "a"
        resultado = self.juego.validar_letra(letra)
        self.assertEqual(True,resultado)
    

    def test_ingreso_gato_juego_ganador_perfecto(self):
        letras_seleccionadas=["a","g","t","o"]
        self.juego.set_palabra("gato")
        self.probar_letras(letras_seleccionadas)
        resultado = self.juego.resultado
        self.assertEqual("ganador",resultado) 
    
    def test_ingreso_gato_perdedor(self):
        letras_seleccionadas=["p","r","u","e","s","i","l"]
        self.juego.set_palabra("gato")
        self.probar_letras(letras_seleccionadas)
        resultado = self.juego.resultado
        self.assertEqual("perdedor",resultado) 

    def test_ingreso_gato_juego_ganador_parcial(self):
        letras_seleccionadas=["a","r","g","t","e","o"]
        self.juego.set_palabra("gato")
        self.probar_letras(letras_seleccionadas)
        resultado = self.juego.resultado
        self.assertEqual("ganador",resultado)

    def test_ingreso_gato_juego_perdedor_parcial(self):
        letras_seleccionadas=["a","r","g"]
        self.juego.set_palabra("gato")
        self.probar_letras(letras_seleccionadas)
        resultado = self.juego.resultado
        self.assertEqual("",resultado) 

    def probar_letras(self,letras_seleccionadas):
        for letra in letras_seleccionadas:
            self.juego.jugar(letra)
    
    def test_completar_palabra(self):
        letras_seleccionadas = ["g","t"]
        self.juego.set_palabra("gato")
        self.probar_letras(letras_seleccionadas)
        palabra_completada = self.juego.palabra_usuario
        self.assertEqual (["g","_","t","_"],palabra_completada)

    def test_completar_palabra_completa(self):
        letras_seleccionadas = ["g","t","a"]
        self.juego.set_palabra("gata")
        self.probar_letras(letras_seleccionadas)
        palabra_completada = self.juego.palabra_usuario
        self.assertEqual (["g","a","t","a"],palabra_completada)
    
    def test_intentos_disponibles_6(self):
        letras_seleccionadas = ["g","t"]
        self.juego.set_palabra("gato")
        self.probar_letras(letras_seleccionadas)
        intentos = self.juego.intentos
        self.assertEqual (6,intentos)
    
    def test_intentos_disponibles_5(self):
        letras_seleccionadas = ["g","t","w"]
        self.juego.set_palabra("gato")
        self.probar_letras(letras_seleccionadas)
        intentos = self.juego.intentos
        self.assertEqual (5,intentos)
    
    def test_letras_disponibles_5(self):
        letras_seleccionadas = ["g","t","w"]
        self.juego.set_palabra("gato")
        self.probar_letras(letras_seleccionadas)
        letras = self.juego.letras
        self.assertEqual (letras_seleccionadas,letras)
    
    def tests_elegir_palabra_6(self):
        self.juego.elegir_palabra(6)
        palabra = self.juego.palabra
        self.assertEqual("PERRO",palabra)
    
   # def tests_elegir_palabra_9(self):
       # self.juego.elegir_palabra(9)
        #palabra = self.juego.palabra
        #self.assertEqual("AVESTRUZ",palabra)
   
