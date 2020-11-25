from flask import Flask, request, render_template


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/preferences/')
def preferences():
    return render_template("preferences.html")

@app.route('/products/')
def products():
    return render_template("products.html")


if __name__ == "__main__":
    app.run(debug=True)