from flask import Flask, render_template,flash
from ahorcado import Juego


app = Flask(__name__)
app.debug = True
##juego = Juego()


def set_guiones (palabra,letras):
    guiones = ["_" for i in range(len(juego.palabra))]
    print(letras)
    for letra in letras:
        index = palabra.find(letra)
        while index !=-1:
            guiones[index] = letra
            index = palabra.find(letra,index+1,len(palabra))
            

    print(guiones)
    return guiones

@app.route('/')
def home():
    global juego
    juego = Juego()
    juego.set_palabra("AVION")
    return render_template('ahorcado.html', juego=juego)

@app.route('/<letra>')
def seleccionar_letra(letra):
    juego.jugar(letra)
    return render_template('ahorcado.html', juego = juego)
  
