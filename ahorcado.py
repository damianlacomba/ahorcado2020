class Juego(object):
    
    
    def __init__(self):
        self.palabra = "gato"
        self.intentos = 7
    
    def validar_letra(self,letra):
        if letra in self.palabra:
            return True
        else:
            return False
    
    
                

    def jugar(self):   
        pal = ["_","_","_","_"]
        termino = False
        while self.intentos != 0 and termino == False:
            letra = self.elijeLetra()
            if self.validar_letra(letra):
                pos = self.palabra.find(letra)
                pal[pos] = letra
                print(" ".join(pal))
            else:
                self.intentos -= 1
            
            if "".join(pal)==self.palabra:
                termino = True
            else:
                termino = False

        if self.intentos != 0: 
            return "ganador"
        else:
            return "perdedor"       
            

    def elijeLetra(self):
        while True:
            print ('Adivina una letra:')
            letra = input()
            letra = letra.lower()
            if len(letra) != 1:
                print ('Introduce una sola letra.') 
            elif letra not in 'abcdefghijklmnopqrstuvwxyz':
                print ('Elije una letra.')
            else:
                return letra
                
                

   
