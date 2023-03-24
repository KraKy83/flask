from flask import Flask, render_template, request, redirect, abort
from flask_mysqldb import MySQL
import re


app = Flask(__name__)

app.config['MYSQL_HOST'] = "127.0.0.1"
app.config['MYSQL_USER'] = "etudiant"
app.config['MYSQL_PASSWORD'] = "Promo2024"
app.config['MYSQL_DB'] = "test"

mysql = MySQL(app)


@app.route('/')
def home():
    return render_template("form.html")

@app.route('/login', methods = ['POST'])
def login():
    if request.method != "POST":
        abort(404)
    name = request.form['name']
    mail = request.form['mail']
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not(re.search(regex,mail)):
        abort(404)
    matiere = request.form['matiere']
    moyenne = request.form['moyenne']
    if float(moyenne) > 20.0:
        abort(404)
    return render_template("login.html", name=name, mail=mail, matiere=matiere, moyenne=moyenne)

@app.route('/save', methods=['POST'])
def save():
    nom = request.form['nom']
    email = request.form['email']
    matiere = request.form['matiere']
    moyenne = request.form['moyenne']

    cur = mysql.connection.cursor()
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS note (
            id INT(11) NOT NULL AUTO_INCREMENT,
            nom VARCHAR(64) NOT NULL,
            email VARCHAR(64) NOT NULL,
            matiere VARCHAR(64) NOT NULL,
            moyenne FLOAT(2) NOT NULL,
            PRIMARY KEY (id)
        );
    ''')
    cur.execute(
        'INSERT INTO note (nom, email, matiere, moyenne) VALUES (%s, %s, %s, %s)',
        (nom, email, matiere, moyenne))
    mysql.connection.commit()
    cur.close()

    return redirect("/view");

@app.route('/view', methods=['GET'])
def view():
  return render_template('notes.html', notes=get_notes())

def get_notes():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM note')
    notes = cur.fetchall()
    cur.close()
    return notes


@app.errorhandler(404)
def page_not_found(error):
   return render_template('404.html', title = '404'), 404




if __name__ == "__main__":
  app.run(debug = True)
