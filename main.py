from flask import Flask, jsonify
import os
import pytube

app = Flask(__name__)

path="C:/Users/Public/Downloads"
@app.route('/')
def index():
    url = 'https://www.youtube.com/watch?v=E_5d-jPeIVg'
    youtube = pytube.YouTube(url)
    r=youtube.streams.filter(res="144p").first()
    return (r)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
