from flask import Flask, render_template, request
import requests
from post import Post
import smtplib
import os

blog_url = "https://api.npoint.io/46f289398d104c3409ce"
posts = requests.get(blog_url).json()
post_objects = []

for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["author"], post["date"])
    post_objects.append(post_obj)

app = Flask(__name__)


def send_email(name, email, phone, message):
    my_email = "pythonemailtest106@gmail.com"
    password = os.environ.get("PASSWORD")
    message = f"Subject: New message\n\n" \
              f"Name: {name}\n" \
              f"Email: {email}\n" \
              f"Phone: {phone}\n" \
              f"Message: {message}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tonystark53150@gmail.com",
            msg=message
        )


@app.route('/')
def home():
    return render_template("index.html", all_posts=posts)


@app.route('/about')
def about():
    return render_template("about.html")


# @app.route('/contact')
# def contact():
#     return render_template("contact.html")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)

        return render_template("contact.html", msg_sent=True)

    return render_template("contact.html", msg_sent=False)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
