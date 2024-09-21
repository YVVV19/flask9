from flask import Flask, render_template, request
import os

app = Flask(__name__)

poll_data = {
    "question" : "What hobby do you like the most?",
    "fields" : ['Football', 'Basketball', 'Volleyball', 'Fishing', 'Biking', 'Ping-pong']
}


@app.get("/")
def survey():
    return render_template("poll.html", data=poll_data)


@app.get("/poll")
def poll():
    user_vote =request.args.get('field')
    return user_vote


if __name__=="__main__":
    app.run(
        debug=True,
        port="0.0.0.1",
        host=8080,
    )