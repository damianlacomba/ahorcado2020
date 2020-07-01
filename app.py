from flask import Flask, render_template,flash, request,g,redirect,url_for
from ahorcado import Juego


app = Flask(__name__)
app.debug = True





@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST" and request.form['user']!="":
        user = request.form['user']
        print(user)
        global juego
        juego = Juego()
        juego.set_jugador(user)
        print(juego.jugador)
        juego.set_palabra("HAMACA")
        return redirect(url_for("play"))
    return render_template('index.html')

@app.route("/jugar")
def play():
    
    return render_template("juego.html", juego = juego)

@app.route('/jugar/<letra>')
def seleccionar_letra(letra):
    print(juego.letras)
    print(letra)
    juego.jugar(letra)
    print(juego.letras)
    print(juego.palabra_usuario)
    return redirect(url_for("play"))
    

"""@app.route('/')
def home():
    global juego
    juego = Juego()
    juego.set_palabra("AVION")
    print(juego.letras)
    return render_template('ahorcado.html', juego=juego)

@app.route('/<letra>')
def seleccionar_letra(letra):
    print(juego.letras)
    print(letra)
    juego.jugar(letra)
    return render_template('ahorcado.html', juego = juego)"""
  
