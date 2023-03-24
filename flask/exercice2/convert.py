from flask import Flask
app = Flask(__name__)

@app.route('/fahrenheit_to_celsius/<value>')
def fahrenheit_to_celsius(value):
    fahrenheit = int(value)
    celsius = (fahrenheit - 32) / 1.8
    return f"{fahrenheit} °F équivaut à {celsius:.2f} °C"

@app.route('/celsius_to_fahrenheit/<value>')
def celsius_to_fahrenheit(value):
    celsius = int(value)
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius} °C équivaut à {fahrenheit:.2f} °F"

if __name__ == "__main__":
    app.run(debug=True)
