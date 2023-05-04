from flask import Flask, render_template, request 
app = Flask(__name__)

@app.route('/')
def hello_barbie():
    return render_template ("index.html")

@app.route('/reels')
def hola_que_tal():
        name = request.args.get("username")
        lastname = request.args.get("lastname")

        return render_template ("/reels.html",name=name,lastname=lastname)    