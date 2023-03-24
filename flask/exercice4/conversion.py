from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fahrenheit_to_celsius/<value>')
def f_to_c(value):
    fahrenheit = int(value)
    celsius = (fahrenheit - 32) / 1.8
    return render_template('template.html', type="deg", temp=int(celsius))

@app.route('/celsius_to_fahrenheit/<value>')
def c_to_f(value):
    celsius = int(value)
    fahrenheit = (celsius * 9/5) + 32
    return render_template('template.html', type="far", temp=int(fahrenheit))


if __name__ == "__main__":
  app.run(debug = True)