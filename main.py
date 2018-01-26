from flask import Flask,request,redirect, render_template, session, flash
import cgi
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://My-Homepage-App:Moneys6249@localhost:8889/My-Homepage-App'
app.config['SQLALCHEMY_ECHO']= True
db = SQLAlchemy(app)
app.secret_key= '1a2b3c4d5e6f7g'

class UserLinks(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120))

    def __init__(self,name):
        self.name = name

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True)
    password = db.Column(db.String(120))

    def __init__(self, email, password):
        self.email = email
        self.password = password

@app.before_request
def require_login():
    allowed_routes= ['login', 'signup']
    if request.endpoint not in allowed_routes and 'email' not in session:
        return redirect('/login')


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['email']= email
            flash("Logged In")
            return redirect ('/')

        else:
            return '<h1>Error!</h1>'
    return render_template('login.html', title= 'Login')


@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify']
        existing_user = User.query.filter_by(email=email).first()

        if not existing_user:
            new_user = User(email, password)
            db.session.add(new_user)
            db.session.commit()
            session['email']= email
            return redirect ('/')
        else:
            return '<h1> Duplicate User</h1>'
    return render_template('signup.html', title= 'Signup')

@app.route("/logout")
def logout():
    del session['email']
    return render_template('Login.html')


@app.route("/", methods=['POST', 'GET'])
def newlink():

    if request.method == 'POST':
        link_add = request.form['link']
        #url_link = "http://www." + link + ".com"
        new_link = UserLinks(link_add)
        db.session.add(new_link)
        db.session.commit()

    links = UserLinks.query.all()
    return render_template('userpage.html', links=links)

@app.route('/delete-link', methods=['POST'])
def delete_link():

        link_id = int(request.form ['link-id'])
        link = UserLinks.query.get(link_id)
        db.session.delete(link)
        db.session.commit()

        return redirect('/')

if __name__ == '__main__':
    app.run()
