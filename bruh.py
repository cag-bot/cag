from flask import Flask, render_template
import sys
sys.path
sys.path.append(r"D:\oauth\oauth.py")
from oauth import Oauth

app = Flask(__name__)

@app.route("/")
def html():
    return render_template("index.html", discord_url=Oauth.discord_login_url)

@app.route("/login")
def login():
    return "poop"
if __name__ == "__main__":
    app.run()