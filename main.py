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
        varify_password = request.form['password_verify']
        email = request.form['email']

        


        user_name_error = ''
        password_error = ''
        varify_password_error = ''
        email_error = ''

        if len(user_name) <= 0:
                user_name_error = 'Please enter a valid user name.'
                user_name = ''

        if not user_name_error:
                template = jinja_env.get_template('welcome.html')
                return template.render(user_name=user_name)
        else:
                template = jinja_env.get_template('user_name.html')
                return template.render('user_name.html', user_name_error=user_name_error, user_name=user_name)

@app.route ('/')
def index():
    template = jinja_env.get_template('user_name.html')
    return template.render()

app.run()

    