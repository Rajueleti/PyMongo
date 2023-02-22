# PyMongo



Posting new data
To add new data to the database, use the following curl command:

curl -X POST -H "Content-Type: application/json" -d '{"id": 2506, "title": "New Show", "clips_count": 1, "description": "This is a new show", "episodes_count": 5, "genres": "[Comedy, Drama]", "score": 4.8, "seasons_count": 1, "company": "ABC", "rating": "TV-PG"}' https://rajueleti.herokuapp.com/api



Updating existing data
To update existing data in the database, use the following curl command:


curl -X PATCH -H "Content-Type: application/json" -d '{"description": "This show has been updated"}' https://rajueleti.herokuapp.com/api/New%20Show

Deleting data
To delete data from the database, use the following curl command:


curl -X DELETE \
  https://rajueleti.herokuapp.com/api/New%20Show

#Note: Replace New%20Show in the above commands with the actual title of the show you want to add/update/delete. Also, make sure to include the -H "Content-Type: application/json" header in the POST and PATCH requests, and the -d flag to include the JSON data.
