from flask import Flask, render_template, redirect, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/welcome')
def welcome():
    user_name = request.args.get['user_name']
    template = jinja_env.get_template('user_name.html')

    return template.render('welcome.html', user_name=user_name)


@app.route('/user_signup', methods=['POST'])
def user_info():

        user_name = request.form['user_name']
        password = request.form['password']
        password_verify = request.form['password_verify']
        email = request.form['email']

        


        user_name_error = ''
        password_error = ''
        verify_password_error = ''
        email_error = ''

        if len(user_name) <= 0:
                user_name_error = 'Please enter a valid user name.'
                user_name = ''

        if len(password) <=0:
                password_error = 'Please enter a valid password.'
                password = ''
        
        if len(password_verify) <=0:
                verify_password_error = 'Please enter a valid password.'
                password_verify = ''

        if len(user_name) < 3 or len(user_name) > 20:
                user_name_error = "Please use a user name between 3 and 20 letters."
                user_name = ''

        if len(password) < 3 or len(password) >20:
                password_error = "Please enter a password between 3 and 20 characters."
                password = ''

        if len(password_verify) < 3 or len(password_verify) >20:
                verify_password_error = "Please enter a password between 3 and 20 characters."
                password_verify = ''

        if password_verify != password:
                verify_password_error = "Passwords dont match!"
                password = ''
                password_verify = ''

        if ' ' in user_name:
                user_name_error = "Please enter a valid user name."
                user_name = ''
        
        if ' ' in password:
                password_error = 'Please enter a valid password'
                password = ''

        if ' ' in password_verify:
                verify_password_error = "Please enter a valid password."
                password_verify = ''

        
        if len(email) > 0:
                if '@' not in email and '.' not in email or ' ' in email:
                        email_error = 'Thats not a valid email.'
                        email = ''
                elif len(email) < 3 and len(email) > 20:
                        email_error = "Thats not a valid email."
                        email = ''


        if not user_name_error and not password_error and not verify_password_error and not email_error:
                template = jinja_env.get_template('welcome.html')
                return template.render(user_name=user_name)
        else:
                template = jinja_env.get_template('user_name.html')
                return template.render(user_name_error=user_name_error, user_name=user_name, password=password, password_verify=password_verify, email=email,
                password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)

@app.route ('/')
def index():
    template = jinja_env.get_template('user_name.html')
    return template.render()

app.run()

    