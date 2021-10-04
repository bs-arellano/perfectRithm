from flask import Flask, redirect, url_for, request, render_template, session
import Database

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fd6a3c8acb37fbb9e89778cd0f4db563dd1e9b4d'


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/game/<song>")
def game(song):
    data = Database.select_song(song)
    if data is not None:
        return render_template('game.html',data=data)
    else:
        return redirect(url_for('maps'))


@app.route("/maps", methods=['POST', 'GET'])
def maps():
    if request.method=='GET':
        data = Database.consultar_canciones()
    if request.method=='POST':
        data = Database.consultar_cancion(request.form['m_name'])
    return render_template('maps.html', data = data)


@app.route("/leaderboard", methods=['POST', 'GET'])
def leaderboard():
    if request.method=='GET':
        data = Database.consultar_usuarios()
    if request.method=='POST':
        data = Database.consultar_usuario(request.form['u_name'])
    return render_template('leaderboard.html', data=data)

@app.route("/profile")
def profile():
    return render_template('profile.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    if request.method == 'POST':
        return redirect(url_for("index"))
