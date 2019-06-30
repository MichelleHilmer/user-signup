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
    return render_template('welcome.html', user_name = user_name)


@app.route('/user', methods=['POST'])
def user_info():

        user_name = request.form['user_name']
        password = request.form['password']
        varify_password = request.form['password_verify']
        email = request.form['email']

        template = jinja_eva.get_template('welcome.html')
        return template.render(user_name=user_name)


        #if ' ' in user_name:
                #error = "Please enter valid user name."
                #return redirect("/?error=" + error)

        #if user_name.length < 3 or user_name.length > 20:
                #error = "Please make user_name between 3 and 20 characters."
    

        #return redirect('/welcome')

@app.route ('/')
def index():
    template = jinja_env.get_template('user_name.html')
    return template.render()

app.run()

    