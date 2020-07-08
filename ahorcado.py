class Juego(object):
    
    
    def __init__(self):
        self.palabras = ["GATO","PERRO","DINOSAURIO","RINOCERONTE","AVESTRUZ"]
        self.palabra = ""
        self.intentos = 6
        self.letras = []
        self.resultado = ""
        self.palabra_usuario = []
        self.jugador = ""
    
    def elegir_palabra(self,pos):
        try:
            palabra = self.palabras[pos]
            self.set_palabra(palabra)
        except:
            while pos > len(self.palabras)-1:
                pos = pos-len(self.palabras)
                
            palabra = self.palabras[pos]
            self.set_palabra(palabra)
    
    def set_palabra(self,palabra):
        self.palabra = palabra
        self.set_palabra_usuario(palabra)
    
    def set_jugador(self,jugador):
        self.jugador = jugador
    
        
    def set_palabra_usuario(self,palabra):
        self.palabra_usuario = [ "_" for i in range(len(palabra))]
        
    

    def completar_palabra(self,letra):
        
        index = self.palabra.find(letra)
        while index !=-1:
            self.palabra_usuario[index] = letra
            index = self.palabra.find(letra,index+1,len(self.palabra))


    def validar_letra(self,letra):
        if letra in self.palabra:
            return True
        else:
            return False
        
    def bienvenida(self,nombre):
        nombre = nombre.capitalize()
        self.jugador = nombre
        return ("Hola {}".format(nombre))

    
    def gano(self):
        palabra_usuario = "".join(self.palabra_usuario)
        if self.palabra == palabra_usuario:
            return True
        else:
            return False

  
    def jugar(self,letra):
        self.letras.append(letra)
        if self.validar_letra(letra):
            self.completar_palabra(letra)
            if self.gano():
                self.resultado = "ganador"
        else:
            self.intentos -=1
        
        if self.intentos == 0:
            self.resultado = "perdedor"
        

        

               


                

