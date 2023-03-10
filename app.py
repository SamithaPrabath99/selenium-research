from flask import Flask, request

import main

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page'


@app.route('/trending/')
def get_trending():
    return main.get_trending_videos()


@app.route('/user_search/', methods=['POST', 'GET'])
def user_search():
    keywords = request.args.get('keywords')
    return main.get_search_result(keywords=keywords)


if __name__ == '__main__':
    app.run()
