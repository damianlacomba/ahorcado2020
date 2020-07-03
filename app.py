from flask import Flask, render_template,flash, request,g,redirect,url_for,session
from ahorcado import Juego


app = Flask(__name__)
app.secret_key = 'any random string'

juego = Juego()

@app.before_request
def before_request_user():
    if "user" in session:
        print(session["user"])
    else:
        redirect(url_for("index"))



@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST" and request.form['user']!="":
        user = request.form['user']
        session["user"] = user
        session["words"] = []
        """print(user)
        global juego
        juego = Juego()
        juego.set_jugador(user)
        print(juego.jugador)
        juego.set_palabra("HAMACA")"""
        return redirect(url_for("play"))
    return render_template('index.html')



@app.route("/jugar",methods=["POST","GET"])
def play():
    juego = Juego()
    juego.set_jugador(session["user"])
    juego.set_palabra("DINOSAURIO")

    if "words" in session:
        print(session["words"])
        for word in session["words"]:
            juego.jugar(word)
    session["resultado"] = juego.resultado
    return render_template("juego.html", juego = juego)

@app.route('/jugar/<letra>')
def seleccionar_letra(letra):
    if session["resultado"]=="":
        temp = session["words"]
        temp.append(letra)
        session["words"] = temp
        print(session["words"])
    return redirect(url_for("play"))

@app.route('/resetear')
def reset():
    session["words"]=[]
    return redirect(url_for("play"))


  
