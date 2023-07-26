from threading import Thread

from flask import Flask

app = Flask('')


@app.route('/')
def home():
    return "hi i am alive" # put any string here (like HTML) and do not change anything else here


def run():
    app.run(host='0.0.0.0', port=8080)


def server():
    t = Thread(target=run)
    t.start()
