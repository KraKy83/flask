from flask import Flask, render_template
from time import strftime
app = Flask(__name__)

@app.route("/bonjour/<name>")
def bonjour(name):
    return render_template('template.html',name=name,time=strftime('%H:%M:%S'),hour=int(strftime('%H')))

if __name__ == "__main__":
    app.run(debug = True)
