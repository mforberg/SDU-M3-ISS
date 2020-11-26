from flask import Flask, request, render_template
import pymongo

code = ""
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
client = pymongo.MongoClient("mongodb://bobitybo:<"+code+">@<hostname>/<dbname>?ssl=true&replicaSet=atlas-123xr0-shard-0&authSource=admin&retryWrites=true&w=majority")

print(client)
@app.route('/')
def index():
    db = client.test
    return render_template("index.html")

@app.route('/preferences/')
def preferences():
    return render_template("preferences.html")

@app.route('/products/')
def products():
    return render_template("products.html")

@app.route('/insert/', methods=['POST'])
def insert_to_db():
    dbDict = {}
    if request.method == 'POST':
        for key, value in request.args.items():
            dbDict[key] = value
    client["fashion"].insert_one(dbDict)



if __name__ == "__main__":
    app.run(debug=True)

