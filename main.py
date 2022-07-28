from flask import Flask, render_template
import requests

posts = requests.get(url="https://api.npoint.io/cfe53b46bf48f290c306").json()
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
