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
    if len(username) < int(3) or len(username) > int(20):
        username = ''
        name_error = 'Enter valid username'
    else:
        if ' ' in username:
            name_error = 'Enter valid username'
            username = ''

    if len(password) < int(3) or len(password) > int(20):
        pass_error = "That's not a valid password"
        password = '' 
    else:
        if ' ' in password:
            pass_error = "That's not a valid password"
            password = ''
    if password != verify:
        ver_error = 'passwords do not match' 
        verify= ''
    while len(email) > int(0):
        if len(email) < int(3) or len(email) > int(20):
            email_error= 'Email not valid'
            email= ''
    
        else:
            if not '@' in email:
                email_error = 'Email not valid'
                email= ''
            else:
                if not '.' in email:     
                    email_error = 'Email not valid'
                    email= ''
                else:
                    if ' ' in email:
                        email_error= 'Email not valid'
                        email = ''    
    
        if not email_error:
            break
    if not name_error and not pass_error and not ver_error and not email_error:  
        
        return redirect('/welcome?username='  + username)     
    else:
         return render_template('index.html', name_error=
            name_error, username=username, pass_error=pass_error, password=password,ver_error=ver_error, verify=verify, email_error=email_error, email=email)

@app.route('/welcome')
def welcome():
    username =request.args.get('username')
    return render_template('welcome.html', username = username)







app.run()