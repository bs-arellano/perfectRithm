from flask import Flask, redirect, url_for, request, render_template, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
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
    if 'loggedin' in session:
        data = Database.select_user_by_id(session['id'])
        return render_template('profile.html',data=data)
    else:
        return redirect(url_for('login'))


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_email = request.form['login_email']
        password = request.form['login_password']
        user = Database.select_user_by_email(user_email)
        print(user)
        if user:
            password_hash = user[3]
            print(generate_password_hash(password))
            print(password_hash)
            if check_password_hash(password_hash,password):
                session['loggedin']=True
                session['id']=user[0]
                session['username']=user[1]
                return redirect(url_for('index'))
            else:
                flash('Incorrect username/password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect username/password')
    return render_template('login.html')

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        username = request.form['reg_name']
        email = request.form['reg_email']
        password = request.form['reg_password']
        Database.reg_user(username,email,generate_password_hash(password,"sha256"))
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))
