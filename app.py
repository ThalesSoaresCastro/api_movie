from flask import Flask, jsonify, request, Response
from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

#configuração do banco
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://127.0.0.1:27017/movies_api'
}
initialize_db(app)

@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

#adiciona um filme...
@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie = Movie(**body).save()
    id = movie.id
    return {'id':str(id)}, 200


#altera o filme...
@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body=request.get_json()
    Movie.objects.get(id=id).update(**body)
    return 'Update Complete', 200

#remove o filme
@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    Movie.objects.get(id=id).delete()
    return 'Delete OK', 200

#buscando apenas um filme
def get_movie(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)

app.run()