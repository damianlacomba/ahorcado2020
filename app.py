from flask import Flask, render_template,flash, request,g,redirect,url_for,session
from ahorcado import Juego


app = Flask(__name__)
app.secret_key = 'any random string'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




@app.route("/",methods=["POST","GET"])
def index():
    if "user" in session:
        session.pop("user")
    else:
        if request.method == "POST" and request.form['user']!="":
            user = request.form['user']
            session["user"] = user
            session["words"] = []
            session["juegos"] = 0
        
            return redirect(url_for("play"))
    return render_template('index.html')



@app.route("/jugar",methods=["POST","GET"])
def play():
    if "user"  not in session:
        return redirect(url_for("index")) 
    else:
        print(session["user"])
        juego = Juego()
        juego.set_jugador(session["user"])
        juego.elegir_palabra(session["juegos"])

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
    session["juegos"] +=1 
    return redirect(url_for("play"))

@app.route('/nuevojuego')
def nuevojuego():
    return redirect(url_for("index"))
  
