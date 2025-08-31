from flask_ngrok import run_with_ngrok
from flask import Flask

app = Flask(__name__)
run_with_ngrok(app) 

@app.route("/")
def home():
    return "Flask is working on Colab with ngrok!"

app.run()
