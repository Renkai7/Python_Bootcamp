from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
bootstrap = Bootstrap5(app)
# SQL Alchemy setup
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///top-10-movies.db'
db = SQLAlchemy(app)

API_KEY = os.environ.get('API_KEY')


# Movie model
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


# Edit Movie form
class RateMovieForm(FlaskForm):
    rating = StringField(label="Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


# Add Movie form
class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")


@app.route('/')
def home():
    order_movies = Movie.query.order_by(Movie.rating.desc())
    num = 1
    for movie in order_movies:
        movie.ranking = num
        num += 1
    rank_movies = Movie.query.order_by(Movie.rating.asc())
    return render_template("index.html", movies=rank_movies)


@app.route('/edit', methods=['POST', 'GET'])
def rate_movie():
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    rate_form = RateMovieForm()
    print(movie_id)
    if rate_form.validate_on_submit():
        movie_to_update.rating = float(rate_form.rating.data)
        movie_to_update.review = rate_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie_to_update, form=rate_form)


@app.route('/delete', methods=['POST', 'GET'])
def delete_movie():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add', methods=['POST', 'GET'])
def add_movie():
    # Movie Database API

    movie_database_endpoint = "https://api.themoviedb.org/3/search/movie"
    add_movie_form = AddMovieForm()
    if add_movie_form.validate_on_submit():
        movie_database_response = requests.get(url=movie_database_endpoint, params={
            "api_key": API_KEY,
            "query": add_movie_form.title.data,
            "language": "en-US"
        })
        movie_database_response.raise_for_status()
        moviedb_data = movie_database_response.json()['results']

        return render_template('select.html', movies=moviedb_data)
    return render_template('add.html', form=add_movie_form)


@app.route('/find')
def find_movie():
    movie_id = request.args.get('id')
    if movie_id:
        movie_database_endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
        movie_database_response = requests.get(url=movie_database_endpoint, params={
            "api_key": API_KEY,
            "language": "en-US"
        })
        movie_database_response.raise_for_status()
        data = movie_database_response.json()
        new_movie = Movie(
            title=data['title'],
            img_url=f"https://image.tmdb.org/t/p/w500{data['backdrop_path']}",
            year=data['release_date'][:4],
            description=data['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('rate_movie', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
