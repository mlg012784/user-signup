from flask import Flask, request, redirect, render_template
import cgi 
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_form():
    return render_template('index.html')

@app.route("/", methods= ['POST'])
def index():
    username= request.form['username']
    password= request.form['password']
    verify= request.form['verify']
    email= request.form['email']
    name_error =''
    pass_error= ''
    ver_error= ''
    email_error= ''

    for i in username:
        if i.isalpha == False:
            name_error = 'Enter valid username'

    
    
#if len(username) < 3 or len(username) > 20:
        









    return render_template('index.html')


app.run()