from flask import Flask,request,redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


#@app.route("/")
#def index():
#    return "Hello World"

@app.route("/")
def index():
    return render_template('index.html', title= 'Signup')

@app.route("/login")
def login():
    return render_template('login.html', titile= 'Login')

@app.route("/signup")
def signup():
    return render_template('index.html', titile= 'Signup')

@app.route("/logout")
def logout():
    return render_template('index.html')


links= []

@app.route("/mylinks", methods=['POST', 'GET'])
def newlink():

    if request.method == 'POST':
        link= request.form['link']
        links.append(link)
    #username= request.form['username']
    return render_template('userpage.html', links=links)#username=username)


app.run()
