from flask import (Flask, render_template, url_for, flash, redirect, send_file)
from flask_mail import Mail
import json
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get('EMAIL_USER')
app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

@app.route("/")
def home():
    return render_template("home-copy.html")

@app.route("/projects")
def projects():

    return render_template("projects.html")

@app.route("/about")
def about():

    return render_template("about.html")

@app.route("/project")
def project():

    return render_template("project.html")


###contact page

@app.route("/contact")
def contact():

    return render_template('contact.html')

@app.route("/resume")
def resume():
    filename = "./static/images/angelo-garetto-RESUME.pdf"
    return send_file(filename,  as_attachment=True)




if __name__=="__main__":
    app.run(debug=True)