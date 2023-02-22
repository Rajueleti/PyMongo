from pymongo import MongoClient
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

client = MongoClient("mongodb+srv://RajuEleti:RajuEleti@cluster0.iz79rqq.mongodb.net/test?retryWrites=true&w=majority", tlsAllowInvalidCertificates=True)
db = client["db"]


# Insert the new movie and show.
@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.get_json()
        db.Hulu.insert_one(data)
        return "OK"
    except Exception as e:
        return str(e)


# Update the movie and show information using title.
@app.route('/api/<string:fname>', methods=['PATCH'])
def api_update(fname):
    try:
        data = request.get_json()
        db.Hulu.update_one({"title": fname}, {"$set": data})
        return "OK"
    except Exception as e:
        return str(e)


# Delete the movie and show information using title.
@app.route('/api/<string:fname>', methods=['DELETE'])
def api_delete(fname):
    try:
        db.Hulu.delete_one({"title": fname})
        return 'movie deleted'
    except Exception as e:
        return str(e)


#Retrieve all the movies and shows in database
'''@app.route('/api', methods=['GET'])
def api_get():
    try:
        data = db.Hulu.find()
        json_data=[]
        for x in data:
            x['_id'] = str(x['_id'])  # Convert ObjectId to string
            json_data.append(x)
        return jsonify(json_data)  # Return data as JSON
    except Exception as e:
        return str(e)'''



# Display the movie and show’s detail using title.
@app.route('/api/<string:fname>', methods=['GET'])
def api_get_one(fname):
    try:
        data = db.Hulu.find_one({"title": fname})
        return str(data)
    except Exception as e:
        return str(e)


# Retrieve all the movies and shows in the database
@app.route('/api', methods=['GET'])
def api_get():
    try:
        data = db.Hulu.find()
        json_data = []
        for x in data:
            x['_id'] = str(x['_id'])
            json_data.append(x)
        return jsonify(json_data)  # Return data as JSON
    except Exception as e:
        return str(e)

# Count duplicate items with given title
@app.route('/count_duplicates/<string:fname>', methods=['GET'])
def count_duplicates(fname):
    pipeline = [
        {'$match': {'title': fname}},  # Filter by title
        {'$group': {'_id': '$title', 'count': {'$sum': 1}}},
        {'$match': {'count': {'$gt': 1}}}
    ]
    cursor = collection.aggregate(pipeline)

    # Get the count of duplicate documents
    count = 0
    for doc in cursor:
        count += doc['count'] - 1

    return f'Total number of duplicate documents for title "{fname}": {count}'
    
    
    
# Search for movies by title
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        movies = db.Hulu.find({'title': {'$regex': query, '$options': 'i'}})
        return render_template('index.html', movies=movies)
        print (movies)
    else:
        return render_template('index.html')
    
    
    

# Render the HTML template
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
