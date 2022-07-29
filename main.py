import os

from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get(url="https://api.npoint.io/cfe53b46bf48f290c306").json()
my_email = os.environ['email']
password = os.environ['password']
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:Lateefah's Blog\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs='lateefahajadi@gmail.com', msg=email_message)


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
