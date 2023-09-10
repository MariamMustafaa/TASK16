from flask import Flask, render_template, request, redirect
from Model.database import Database

app = Flask(__name__)
database = Database()

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route("/protons")
def getProtons():
    #TODO
    pass

@app.route("/protons",methods="POST")
def addProton(protonName: str, protonAge: int, protonTrack: str):
    #TODO
    pass

@app.route("/hobbies",methods="POST")
def addHobby(hobbyTitle: str, imagePAth: str):
    #TODO
    pass

#Views the hobby title, image and protons who like it
@app.route("/hobbies/<hobbyTitle>")
def viewHobby(hobbyTitle: str):
    #TODO
    pass

@app.route("/hobbies/<hobbyTitle>/<protonName>")
def matchProtoHobby(hobbyTitle: str,protonName: str):
    #TODO
    pass

@app.route("/hobbies/<hobbyTitle>",methods="DELETE")
def deleteHobby(hobbyTitle: str):
    #TODO
    pass

@app.route("/protons/<protonName>",methods="DELETE")
def deleteProton(protonName: str):
    #TODO
    pass