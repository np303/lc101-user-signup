from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/signup", methods=['GET'])
def user_signup():
    return render_template('signup.html')






app.run()