from flask import Flask,request,redirect
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

template_dir = os.path.join(os.path.dirname(__file__),'templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
autoescape= True)

#@app.route("/")
#def index():
#    return "Hello World"

@app.route("/")
def index():
    template = jinja_env.get_template('userpage.html')
    return template.render()

links= []

@app.route("/mylinks", methods=['POST', 'GET'])
def newlink():

    if request.method == 'POST':
        link= request.form['link']
        links.append(link)

    template = jinja_env.get_template('userpage.html')
    return template.render(links=links)


app.run()
