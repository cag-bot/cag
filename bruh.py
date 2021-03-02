from flask import Flask
app = Flask(__name__)

@app.route('/')
def html():
    return "<h1>herro woruld</h1>"