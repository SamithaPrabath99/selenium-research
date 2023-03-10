from flask import Flask
import main

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page'


@app.route('/trending/')
def get_trending():
    return main.get_trending_videos()


if __name__ == '__main__':
    app.run()
