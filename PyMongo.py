from pymongo import MongoClient
from flask import Flask, request, jsonify
import ssl



app = Flask(__name__)

client = MongoClient("mongodb+srv://RajuEleti:RajuEleti@cluster0.iz79rqq.mongodb.net/test?retryWrites=true&w=majority")
db = client["db"]


#Insert the new movie and show. 
@app.route('/home/', methods=['POST'])
def api():
    try:
        data = request.get_json()
        db.Hulu.insert_one(data)
        return "OK"
    except Exception as e:
        return str(e)


#Update the movie and show information using title. 
@app.route('/home/<string:fname>', methods=['PATCH'])
def api_update(fname):
    try:
        data = request.get_json()
        db.Hulu.update_one({"title": fname}, {"$set": data})
        return "OK"
    except Exception as e:
        return str(e)


#Delete the movie and show information using title.
@app.route('/home/<string:fname>', methods=['DELETE'])
def api_delete(fname):
    try:
        db.Hulu.delete_one({"title": fname})
        return 'movie deleted'
    except Exception as e:
        return str(e)


#Retrieve all the movies and shows in database
@app.route('/home', methods=['GET'])
def api_get():
    try:
        data = db.Hulu.find()
        json_data=[]
        for x in data:
            json_data.append(x)
        return str(json_data)
    except Exception as e:
        return str(e)


#Display the movie and show’s detail using title.
@app.route('/home/<string:fname>', methods=['GET'])
def api_get_one(fname):
    try:
        data = db.Hulu.find_one({"title": fname})
        return str(data)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
