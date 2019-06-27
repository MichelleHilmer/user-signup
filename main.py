from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/welcome", methods=["POST" ,"GET"])
def welcome():
    user_name = request.form["user_name"]
    return render_template("welcome.html")


@app.route("/user", methods=["GET", "POST"])
def user_info():

        user_name = request.form["user_name"]
        password = request.form["password"]
        varify_password = request.form["varify_password"]
        email = request.form["email_optional"]

        #if ' ' in user_name:
                #error = "Please enter valid user name."
                #return redirect("/?error=" + error)

        #if user_name.length < 3 or user_name.length > 20:
                #error = "Please make user_name between 3 and 20 characters."
    

        return render_template("welcome.html", user_name=user_name)

@app.route ('/')
def index():
    return render_template("user_name.html")

app.run()

    