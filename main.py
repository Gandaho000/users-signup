from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/", methods=['POST','GET'])
def validation():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    password_error = ''
    verify_password_error = ''
    email_error = ''


    
    if username == "" or len(username) < 3 or len(username) > 20 or " " in (username):
        username_error = "Enter A Valid Username. Username must be between 3 & 20 Characters. Must not contain a space."
        return  render_template('index.html', username_error = username_error, username=username, email = email)

    elif password == "" or len(username) < 3 or len(username) > 20 or " " in password:
        password_error = "Enter A Valid Password. Password must be between 3 and 20 characters. Must not contain a space."
        return  render_template('index.html', password_error = password_error)

    elif verify_password == "":
        verify_password_error = "Retype the password you typed above."
        return  render_template('index.html', verify_password_error = verify_password_error, username=username, email = email)
    
    elif email != "" and len(email) < 3 or email != "" and len(email) > 20 or email != "" and "@" not in (email) or email != "" and "." not in (email):
        email_error = "Enter A Valid Email"
        return  render_template('index.html', email_error = email_error, username=username, email = email)

    elif password != verify_password:
        password_match_error = "Your Passwords Don't Match. Type Again"
        return render_template('index.html', password_match_error = password_match_error, username=username, email=email)

    else:
        return  render_template('welcome.html', email_error = email_error, username=username, email = email)





app.run()