from flask import Flask, render_template, request
import sys
sys.path
sys.path.append(r"D:\oauth\oauth.py")
from oauth import Oauth

app = Flask(__name__)

@app.route("/")
def html():
    return render_template("index.html", discord_url=Oauth.discord_login_url)

@app.route("/")
def login():
    code = request.args.get("code")
    token = Oauth.get_access_token(code)
	session["token"] = token

	user = Oauth.get_user_json(at)
	user_name, user_id = user.get("username"), user.get("discriminator")

	return render_template("index.html", bruh=f"Success, logged in as {user_name}#{user_id}")

if __name__ == "__main__":
    app.run()