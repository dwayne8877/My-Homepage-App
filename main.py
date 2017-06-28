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
    return render_template('userpage.html', title= 'Signup')


links= []

@app.route("/mylinks", methods=['POST', 'GET'])
def newlink():

    if request.method == 'POST':
        link= request.form['link']
        links.append(link)

    return render_template('userpage.html', links=links)


app.run()
