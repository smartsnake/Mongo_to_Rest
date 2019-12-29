from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json

app = Flask(__name__)


with open('config.json') as json_data_file:
    data = json.load(json_data_file)
print(data)

client = MongoClient(data['mongo_url'], int(data['mongo_port']))

db = client[data['database']]
collection = db[data['collection']]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/get_all", methods = ['GET'])
def get_all_contact():
    try:
        values = collection.find()
        return dumps(values)
    except Exception as e:
        return dumps({'error' : str(e)})

if __name__ == '__main__':
    app.run()