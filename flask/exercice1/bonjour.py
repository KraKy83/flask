from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route("/user/<username>")
def user_greeting(username):
    return f"Bonjour {username} !"

@app.route("/time")
def server_time():
    time_now = datetime.now().strftime('%H:%M:%S')
    return f"Le serveur indique l'heure {time_now}"

if __name__ == "__main__":
    app.run(debug=True)
