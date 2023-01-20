from flask import Flask
from flask import render_template
from random import randint


app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return "Home"


@app.route("/about/<location>/")
def about_location(location):
    return "I am from %s." % location


@app.route("/skills/", defaults={"username": None})
@app.route("/skills/<string:username>")
def skills(username):
    return render_template("skills.html", username=username)


@app.route("/skills/<int:toeic_score>/")
def skills_toeic(toeic_score):
   return "My TOEIC score is %d / 90." % toeic_score


@app.route("/projects/", defaults={'amount': 0})
@app.route("/projects/<int:amount>")
def projects(amount):
    projects = ["Facebook", "Twitter", "Instagram", "Uber", "Grab"]
    random_number = randint(0, len(projects) - 1)
    project = projects[random_number]
    return render_template("projects.html", **locals())


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/about/")
def about():
    return render_template("about.html")
