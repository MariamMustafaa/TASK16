from flask import Flask, render_template, request, redirect
from Model.database import Database

app = Flask(__name__)
database = Database()


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/protons")
def getProtons():
    return render_template("Proto.html", protons=database.protons)
    pass


@app.route("/protons/add", methods=["POST", "GET"])
def addProton():
    pr_name = request.form.get("p_name")
    pr_age = request.form.get("p_age")
    pr_track = request.form.get("p_track")
    database.registerProton(pr_name, pr_age, pr_track)
    return redirect("/protons")
    pass


@app.route("/hobbies")
def getHobbies():
    return render_template("hobbies.html", hobbies=database.hobbies)
    pass


@app.route("/hobbies", methods=["POST"])
def addHobby():
    # TODO
    pass


@app.route("/hobbies/<hobbyTitle>/<protonName>", methods=["POST"])
def matchProtoHobby(hobbyTitle: str):
    # TODO
    pass


@app.route("/hobbies/<hobbyTitle>/<protonName>", methods=["DELETE"])
def unmatchProtoHobby(hobbyTitle: str, protonName: str):
    # TODO
    pass

# Views the hobby title, image and protons who like it


@app.route("/hobbies/<hobbyTitle>")
def viewHobby(hobbyTitle: str):
    # TODO
    pass


@app.route("/hobbies/<hobbyTitle>", methods=["DELETE"])
def deleteHobby(hobbyTitle: str):
    # TODO
    pass


@app.route("/protons/<protonName>", methods=["DELETE"])
def deleteProton(protonName: str):
    # TODO
    pass
