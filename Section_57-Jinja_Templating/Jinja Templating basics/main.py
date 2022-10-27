from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = date.today().year
    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    agify_params = {
        "name": name
    }

    genderize_params = {
        "name": name
    }

    agify_response = requests.get("https://api.agify.io/", params=agify_params)
    genderize_response = requests.get("https://api.genderize.io", params=genderize_params)

    agify_data = agify_response.json()
    genderize_data = genderize_response.json()

    return render_template("guess.html", name=agify_data['name'], gender=genderize_data['gender'],
                           age=agify_data['age'])


@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
