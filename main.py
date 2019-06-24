from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/welcome", methods=["POST" ,"GET"])
def welcome():
    user_name = request.form["user_name"]
    return render_template("welcome.html")

@app.route("/email", methods=["GET"])
def email():
    return render_template("user_name.html")

@app.route("/var_pass", methods=["POST"])
def varify_password():
    return render_template("user_name.html")


@app.route("/password", methods=["POST"])
def password():
    return render_template("user_name.html")



@app.route("/user", methods=['GET'])
def user_name():
    user_name = request.form['user_name']

    if ' ' in user_name:
        error = "Please enter valid e-mail."

@app.route ('/')
def index():
    return render_template('user_name.html')

app.run()

    