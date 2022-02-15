# app.py

from flask import Flask, request
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy

from config import Config
from schemas import MovieSchema, DirectorSchema, GenreSchema

app = Flask(__name__)
app.config.from_object(Config())
db = SQLAlchemy(app)
api = Api(app)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


movies_ns = api.namespace('movies')
directors_ns = api.namespace('directors')
genres_ns = api.namespace('genres')


# Movies
# -------------------------------------------------------------------------#
@movies_ns.route('/')
class MoviesView(Resource):

    def get(self):
        movies_schema = MovieSchema(many=True)
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')

        if director_id:
            all_movies = Movie.query.filter_by(director_id=director_id).all()
        elif genre_id:
            all_movies = Movie.query.filter_by(genre_id=genre_id).all()
        elif director_id and genre_id:
            all_movies = Movie.query.filter_by(director_id=director_id, genre_id=genre_id).all()
        else:
            all_movies = Movie.query.all()

        if all_movies:
            return movies_schema.dump(all_movies), 200
        else:
            return "", 404

    def post(self):
        req_json = request.json
        new_movie = Movie(**req_json)

        with db.session.begin():
            db.session.add(new_movie)

            return "", 201


@movies_ns.route('/<int:id>')
class MovieView(Resource):

    def get(self, id):
        movie = Movie.query.get(id)
        if movie:
            movie_schema = MovieSchema()
            return movie_schema.dump(movie), 200
        else:
            return "", 404

    def put(self, id):
        movie = Movie.query.get(id)
        if movie:
            req_json = request.json
            movie.title = req_json.get("title")
            movie.description = req_json.get("description")
            movie.trailer = req_json.get("trailer")
            movie.year = req_json.get("year")
            movie.rating = req_json.get("rating")
            movie.genre_id = req_json.get("genre_id")
            movie.director_id = req_json.get("director_id")

            db.session.add(movie)
            db.session.commit()
            return "", 204
        else:
            return "", 404

    def patch(self, id):
        movie = Movie.query.get(id)
        if movie:
            req_json = request.json
            if "title" in req_json:
                movie.title = req_json.get("title")
            if "description" in req_json:
                movie.description = req_json.get("description")
            if "trailer" in req_json:
                movie.trailer = req_json.get("trailer")
            if "year" in req_json:
                movie.year = req_json.get("year")
            if "rating" in req_json:
                movie.rating = req_json.get("rating")
            if "genre_id" in req_json:
                movie.genre_id = req_json.get("genre_id")
            if "director_id" in req_json:
                movie.director_id = req_json.get("director_id")

            db.session.add(movie)
            db.session.commit()
            return "", 204
        else:
            return "", 404

    def delete(self, id):
        movie = Movie.query.get(id)
        if movie:
            db.session.delete(movie)
            db.session.commit()
            return "", 204
        else:
            return "", 404


# Directors
# -------------------------------------------------------------------------#
@directors_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        directors_schema = DirectorSchema(many=True)
        all_directors = Director.query.all()
        if all_directors:
            return directors_schema.dump(all_directors), 200
        else:
            return "", 404

    def post(self):
        req_json = request.json
        new_director = Director(**req_json)

        with db.session.begin():
            db.session.add(new_director)

            return "", 201


@directors_ns.route('/<int:id>')
class DirectorView(Resource):

    def get(self, id):
        director = Director.query.get(id)
        if director:
            director_schema = DirectorSchema()
            return director_schema.dump(director), 200
        else:
            return "", 404

    def put(self, id):
        director = Director.query.get(id)
        if director:
            req_json = request.json
            director.name = req_json.get("name")

            db.session.add(director)
            db.session.commit()
            return "", 204
        else:
            return "", 404

    def patch(self, id):
        director = Director.query.get(id)
        if director:
            req_json = request.json
            if "name" in req_json:
                director.name = req_json.get("name")

            db.session.add(director)
            db.session.commit()
            return "", 204
        else:
            return "", 404

    def delete(self, id):
        director = Director.query.get(id)
        if director:
            db.session.delete(director)
            db.session.commit()
            return "", 204
        else:
            return "", 404


# Genres
# -------------------------------------------------------------------------#
@genres_ns.route('/')
class GenresView(Resource):

    def get(self):
        genres_schema = GenreSchema(many=True)
        all_genres = Genre.query.all()
        if all_genres:
            return genres_schema.dump(all_genres), 200
        else:
            return "", 404

    def post(self):
        req_json = request.json
        new_genre = Genre(**req_json)

        with db.session.begin():
            db.session.add(new_genre)

            return "", 201


@genres_ns.route('/<int:id>')
class GenreView(Resource):

    def get(self, id):
        genre = Genre.query.get(id)
        if genre:
            genre_schema = GenreSchema()
            return genre_schema.dump(genre), 200
        else:
            return "", 404

    def put(self, id):
        genre = Genre.query.get(id)
        if genre:
            req_json = request.json
            genre.name = req_json.get("name")

            db.session.add(genre)
            db.session.commit()
            return "", 204
        else:
            return "", 404

    def patch(self, id):
        genre = Genre.query.get(id)
        if genre:
            req_json = request.json
            if "name" in req_json:
                genre.name = req_json.get("name")

            db.session.add(genre)
            db.session.commit()
            return "", 204
        else:
            return "", 404

    def delete(self, id):
        genre = Genre.query.get(id)
        if genre:
            db.session.delete(genre)
            db.session.commit()
            return "", 204
        else:
            return "", 404


if __name__ == '__main__':
    app.run(debug=True)
