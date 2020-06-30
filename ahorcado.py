class Juego(object):
    
    
    def __init__(self):
        self.palabra = "gato"
    
    def validar_letra(self,letra):
        if letra in self.palabra:
            return True
        else:
            return False
    
    
                



   
