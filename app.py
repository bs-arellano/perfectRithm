import psycopg2
from flask import Flask, redirect, url_for, request, render_template

db_user = 'postgres'
db_password = 'hyperpro16'

app = Flask(__name__)
conn = None


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/game")
def game():
    return render_template('game.html')


@app.route("/maps")
def maps():
    return render_template('maps.html')


@app.route("/leaderboard")
def leaderboard():
    return render_template('leaderboard.html')


@app.route("/profile")
def profile():
    return render_template('profile.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['user']
        password = request.form['password']
        try:
            conn = psycopg2.connect(
                f"dbname=Perfect_Rithm user={db_user} password={db_password}")
            cur = conn.cursor()
            cur.execute(
                f'SELECT username, password FROM usuario WHERE usermane == "{username}"')
            user = cur.fetchone()
            cur.close()
            if (username == user[1] and password == user[3]):
                return redirect(url_for("/"))
            else:
                return redirect(url_for("login"))
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
