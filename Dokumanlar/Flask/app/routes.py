# from app import app
from flask import Blueprint,request,render_template,redirect,url_for,flash

web_bp = Blueprint('web',__name__)
@web_bp.route("/")
def selam():
    # print(app.secret_key)
    user = {"username":"Ali","pass":"1234"}
    return render_template("index.html",title="",username=user["username"])